#!/usr/bin/env bash
# Test de restauration des sauvegardes (contrôles 8.13 et 5.30, risque R14).
#
# 1. sauvegarde logique de la base de production du lab (pg_dump, format custom) ;
# 2. chiffrement AES-256 de la sauvegarde (clé BACKUP_ENCRYPTION_KEY de lab/.env) ;
# 3. déchiffrement et restauration dans une instance PostgreSQL vierge et isolée ;
# 4. comparaison d'empreintes d'intégrité calculées sur la source et la copie ;
# 5. écriture du résultat mesuré dans reports/restauration.json.
set -euo pipefail

LAB_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ROOT_DIR="$(dirname "$LAB_DIR")"
REPORT="$ROOT_DIR/reports/restauration.json"
WORK="$(mktemp -d)"
RESTORE_CT="kamapay-restore-test-$$"
trap 'docker rm -f "$RESTORE_CT" >/dev/null 2>&1 || true; rm -rf "$WORK"' EXIT

set -a; source "$LAB_DIR/.env"; set +a
compose() { docker compose -f "$LAB_DIR/docker-compose.yml" --env-file "$LAB_DIR/.env" "$@"; }

INTEGRITY_SQL="SELECT
  (SELECT count(*) FROM customers) || ':' ||
  (SELECT count(*) FROM wallets) || ':' ||
  (SELECT coalesce(sum(balance), 0) FROM wallets) || ':' ||
  (SELECT count(*) FROM transactions) || ':' ||
  (SELECT md5(coalesce(string_agg(id || '|' || from_wallet || '|' || to_wallet || '|' || amount, ',' ORDER BY id), ''))
     FROM transactions)"

now_ms() { date +%s%3N; }

echo "[1/4] Sauvegarde de la base du lab"
t0=$(now_ms)
compose exec -T db pg_dump -U kamapay_admin -d kamapay -Fc > "$WORK/kamapay.dump"
source_fp=$(compose exec -T db psql -U kamapay_admin -d kamapay -At -c "$INTEGRITY_SQL")
t_backup=$(now_ms)

echo "[2/4] Chiffrement de la sauvegarde (AES-256-CBC, PBKDF2)"
openssl enc -aes-256-cbc -pbkdf2 -iter 200000 -salt -pass env:BACKUP_ENCRYPTION_KEY \
  -in "$WORK/kamapay.dump" -out "$WORK/kamapay.dump.enc"
backup_sha256=$(sha256sum "$WORK/kamapay.dump.enc" | cut -d' ' -f1)
rm "$WORK/kamapay.dump"

echo "[3/4] Restauration dans une instance vierge"
t_restore_start=$(now_ms)
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -pass env:BACKUP_ENCRYPTION_KEY \
  -in "$WORK/kamapay.dump.enc" -out "$WORK/kamapay.dump"
docker run -d --name "$RESTORE_CT" --network none \
  -e POSTGRES_PASSWORD="$(openssl rand -hex 16)" -e POSTGRES_DB=kamapay \
  postgres:16-alpine >/dev/null
until docker exec "$RESTORE_CT" pg_isready -U postgres -d kamapay >/dev/null 2>&1; do sleep 1; done
sleep 2   # l'image redémarre le serveur après l'initialisation
until docker exec "$RESTORE_CT" pg_isready -U postgres -d kamapay >/dev/null 2>&1; do sleep 1; done
docker exec "$RESTORE_CT" psql -U postgres -q -c "CREATE ROLE kamapay_app NOLOGIN; CREATE ROLE kamapay_admin NOLOGIN;"
docker cp "$WORK/kamapay.dump" "$RESTORE_CT:/tmp/kamapay.dump" >/dev/null
docker exec "$RESTORE_CT" pg_restore -U postgres -d kamapay --exit-on-error /tmp/kamapay.dump
restored_fp=$(docker exec "$RESTORE_CT" psql -U postgres -d kamapay -At -c "$INTEGRITY_SQL")
t_end=$(now_ms)

echo "[4/4] Contrôle d'intégrité"
if [[ "$source_fp" == "$restored_fp" ]]; then success=true; else success=false; fi
echo "  source   : $source_fp"
echo "  restauré : $restored_fp"

mkdir -p "$(dirname "$REPORT")"
python3 - "$REPORT" <<PY
import json, sys
from datetime import datetime, timezone
json.dump({
    "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "succes": "$success" == "true",
    "empreinte_source": "$source_fp",
    "empreinte_restauree": "$restored_fp",
    "sha256_sauvegarde_chiffree": "$backup_sha256",
    "duree_sauvegarde_s": round(($t_backup - $t0) / 1000, 2),
    "duree_restauration_s": round(($t_end - $t_restore_start) / 1000, 2),
    "duree_totale_s": round(($t_end - $t0) / 1000, 2),
    "methode": "pg_dump -Fc, chiffrement AES-256-CBC/PBKDF2, pg_restore sur instance isolée (--network none)",
}, open(sys.argv[1], "w"), indent=2, ensure_ascii=False)
PY
echo "Résultat écrit dans reports/restauration.json"
$success
