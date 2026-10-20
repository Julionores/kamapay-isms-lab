#!/bin/sh
# Crée le rôle applicatif avec le mot de passe fourni par l'environnement
# (lab/.env, généré par lab/scripts/init-secrets.sh). Contrôles 8.2 et 5.17.
set -eu
: "${APP_DB_PASSWORD:?APP_DB_PASSWORD doit être défini}"
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -v app_password="$APP_DB_PASSWORD" <<'SQL'
CREATE ROLE kamapay_app LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION
  PASSWORD :'app_password';
SQL
