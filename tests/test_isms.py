import copy
from datetime import date

import pytest

from checks.registry import REGISTRY
from checks.repository import SECRET_PATTERNS
from isms import ROOT, annexe_a, kpi, render, risk
from isms.data import load
from isms.validate import check_incidents, check_risks, check_soa, validate

TODAY = date(2026, 10, 20)


@pytest.fixture(scope="module")
def isms():
    return load()


def test_repository_is_consistent(isms):
    assert validate(isms, set(REGISTRY), TODAY) == []


def test_annex_a_has_93_controls():
    assert len(annexe_a.CONTROL_IDS) == 93
    assert annexe_a.CONTROL_IDS[36] == "5.37" and annexe_a.CONTROL_IDS[-1] == "8.34"


def test_missing_control_is_reported(isms):
    broken = copy.deepcopy(isms)
    broken.soa["controles"] = [c for c in broken.soa["controles"] if c["id"] != "8.24"]
    assert "SoA : mesure 8.24 de l'annexe A absente" in check_soa(broken, set(REGISTRY))


def test_partial_control_requires_gap_description(isms):
    broken = copy.deepcopy(isms)
    control = next(c for c in broken.soa["controles"] if c["id"] == "5.13")
    del control["ecart"]
    assert any("5.13 : statut partiel sans description" in e for e in check_soa(broken, set(REGISTRY)))


def test_unknown_automated_check_is_reported(isms):
    broken = copy.deepcopy(isms)
    broken.soa["controles"][0]["checks"] = ["CHK-XYZ-99"]
    assert any("CHK-XYZ-99" in e for e in check_soa(broken, set(REGISTRY)))


def test_residual_risk_above_appetite_needs_acceptance(isms):
    broken = copy.deepcopy(isms)
    r08 = next(r for r in broken.risks if r["id"] == "R08")
    del r08["acceptation"]
    errors = check_risks(broken, TODAY)
    assert any(e.startswith("Risque R08 : résiduel 8 > appétence 6") for e in errors)


def test_incident_chronology_is_checked(isms):
    broken = copy.deepcopy(isms)
    broken.incidents["incidents"][0]["detection"] = "2026-02-01T00:00:00Z"
    assert "Incident INC-2026-001 : detection antérieur à debut" in check_incidents(broken)


@pytest.mark.parametrize("value, label", [(1, "faible"), (3, "faible"), (4, "modéré"), (6, "modéré"),
                                          (8, "élevé"), (9, "élevé"), (12, "critique"), (16, "critique")])
def test_risk_levels(value, label):
    assert risk.level(value) == label


def test_kpis(isms):
    values = {k.id: k for k in kpi.compute(isms, TODAY, checks_report=None)}
    assert values["KPI-01"].valeur == pytest.approx(100 * 86 / 93, abs=0.1)
    assert values["KPI-02"].valeur is None and values["KPI-02"].atteint is None
    assert values["KPI-03"].valeur == 0 and values["KPI-03"].atteint
    assert values["KPI-08"].valeur == pytest.approx(6.1, abs=0.1) and values["KPI-08"].atteint
    assert values["KPI-07"].atteint is False  # campagne agents à 75 % : écart assumé et suivi


def test_late_actions_are_counted(isms):
    later = date(2027, 1, 1)
    values = {k.id: k for k in kpi.compute(isms, later, checks_report=None)}
    assert values["KPI-04"].detail == "PA-01, PA-02, PA-05, PA-07, PA-08"


def test_generated_soa_is_up_to_date(isms):
    path = ROOT / "docs/03-soa/declaration-applicabilite.md"
    assert path.read_text(encoding="utf-8") == render.soa(isms, path)


# Échantillons découpés pour ne pas déclencher CHK-SECRET-01 sur ce fichier lui-même.
@pytest.mark.parametrize("text", [
    "pass" + "word = 'S3cr3tValue!'",
    '"api' + '_key": "abcd1234efgh"',
    "DATABASE_URL=postgresql://app:" + "hunter2hunter2@db:5432/x",
    "-----BEGIN " + "PRIVATE KEY-----",
])
def test_secret_patterns_detect(text):
    assert any(p.search(text) for p in SECRET_PATTERNS.values())


@pytest.mark.parametrize("text", [
    "PASSWORD :'app_password';",
    "postgresql://kamapay_app:${APP_DB_PASSWORD}@db:5432/kamapay",
    "POSTGRES_PASSWORD: ${DB_ADMIN_PASSWORD}",
])
def test_secret_patterns_ignore_references(text):
    assert not any(p.search(text) for p in SECRET_PATTERNS.values())
