"""Chargement des référentiels du SMSI (data/*.yaml) et des métadonnées documentaires."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

import yaml

from . import ROOT

GENERATED_MARKER = "<!-- Document généré"


class _Loader(yaml.SafeLoader):
    """Chargeur YAML qui conserve les dates sous forme de chaînes (validation par schéma)."""


_Loader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.load(fh, Loader=_Loader)


def parse_date(value: str) -> date:
    return date.fromisoformat(value)


def parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


@dataclass
class Document:
    path: Path
    meta: dict | None
    body: str
    generated: bool

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


@dataclass
class Isms:
    root: Path
    actifs: dict
    risques: dict
    soa: dict
    incidents: dict
    sensibilisation: dict
    historique: dict = field(default_factory=lambda: {"releves": []})
    documents: list[Document] = field(default_factory=list)

    @property
    def controls(self) -> dict[str, dict]:
        return {c["id"]: c for c in self.soa["controles"]}

    @property
    def risks(self) -> list[dict]:
        return self.risques["risques"]

    @property
    def assets(self) -> dict[str, dict]:
        return {a["id"]: a for a in self.actifs["actifs"]}

    @property
    def actions(self) -> list[dict]:
        return [dict(a, risque=r["id"]) for r in self.risks for a in r.get("actions", [])]

    def risks_for_control(self, control_id: str) -> list[str]:
        return [r["id"] for r in self.risks if control_id in r["controles"]]


_FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def load_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    if text.startswith(GENERATED_MARKER):
        return Document(path, None, text, generated=True)
    match = _FRONT_MATTER.match(text)
    if not match:
        return Document(path, None, text, generated=False)
    return Document(path, yaml.load(match.group(1), Loader=_Loader) or {}, text[match.end():], generated=False)


def load(root: Path = ROOT) -> Isms:
    data = root / "data"
    return Isms(
        root=root,
        actifs=load_yaml(data / "actifs.yaml"),
        risques=load_yaml(data / "risques.yaml"),
        soa=load_yaml(data / "soa.yaml"),
        incidents=load_yaml(data / "incidents.yaml"),
        sensibilisation=load_yaml(data / "sensibilisation.yaml"),
        historique=(load_yaml(data / "historique-kpi.yaml") if (data / "historique-kpi.yaml").exists()
                    else {"releves": []}),
        documents=[load_document(p) for p in sorted((root / "docs").rglob("*.md"))],
    )
