#!/usr/bin/env bash
# Génère les secrets du lab (lab/.env) et le certificat TLS autosigné.
# Aucun secret n'est versionné (contrôles 5.17 et 8.24) : voir .gitignore.
set -euo pipefail
cd "$(dirname "$0")/.."

rand() { openssl rand -base64 32 | tr -d '/+=' | cut -c1-32; }

if [[ ! -f .env ]]; then
  (umask 077; cat > .env <<ENV
DB_ADMIN_PASSWORD=$(rand)
APP_DB_PASSWORD=$(rand)
API_SECRET_KEY=$(rand)$(rand)
BACKUP_ENCRYPTION_KEY=$(rand)$(rand)
ENV
  )
  echo "lab/.env créé"
fi

if [[ ! -f proxy/certs/server.crt ]]; then
  mkdir -p proxy/certs
  openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes -days 90 \
    -subj "/CN=api.kamapay.lab/O=KamaPay SA (fictif)" \
    -addext "subjectAltName=DNS:api.kamapay.lab,DNS:localhost,IP:127.0.0.1" \
    -keyout proxy/certs/server.key -out proxy/certs/server.crt 2>/dev/null
  # Lisibles par l'utilisateur nginx (UID 101) du conteneur : acceptable pour un lab
  # local ; en production la clé reste sur un HSM ou un coffre de secrets.
  chmod 755 proxy/certs
  chmod 644 proxy/certs/server.crt proxy/certs/server.key
  echo "certificat TLS du lab créé (90 jours)"
fi
