# Lab KamaPay : SMSI ISO/IEC 27001 outillé. `make help` liste les cibles.
PYTHON  ?= python3
COMPOSE := docker compose -f lab/docker-compose.yml --env-file lab/.env
TRIVY   := aquasec/trivy:0.58.1

.PHONY: help install validate render test lab-up lab-down scan restore-test checks kpi history all

help: ## Affiche cette aide
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-14s %s\n", $$1, $$2}'

install: ## Installe les dépendances Python
	$(PYTHON) -m pip install -r requirements-dev.txt

validate: ## Vérifie la cohérence du SMSI (schémas, SoA, risques, incidents, documents)
	$(PYTHON) -m isms validate

render: ## Régénère la SoA, le registre des risques et le tableau de bord
	$(PYTHON) -m isms render

test: ## Lance les tests unitaires de l'outillage
	$(PYTHON) -m pytest -q

lab-up: ## Génère les secrets puis démarre le lab (proxy TLS, API, base)
	lab/scripts/init-secrets.sh
	$(COMPOSE) up -d --build --wait

lab-down: ## Arrête le lab et supprime ses données
	$(COMPOSE) down -v

scan: ## Analyse l'image de l'API avec Trivy (reports/trivy.json)
	@mkdir -p reports
	docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v trivy-cache:/root/.cache \
	  $(TRIVY) image --quiet --format json --ignore-unfixed --severity HIGH,CRITICAL \
	  kamapay-lab-api:latest > reports/trivy.json

restore-test: ## Sauvegarde, chiffre, restaure et vérifie l'intégrité de la base
	lab/scripts/test-restauration.sh

checks: ## Exécute les contrôles automatisés (reports/checks.json)
	$(PYTHON) -m checks --strict

kpi: ## Affiche les indicateurs du SMSI
	$(PYTHON) -m isms kpi

history: ## Enregistre un relevé daté des indicateurs (data/historique-kpi.yaml)
	$(PYTHON) -m isms history

all: validate test lab-up scan restore-test checks render kpi ## Chaîne complète
