"""Registre des contrôles automatisés.

Chaque contrôle est rattaché aux mesures de l'annexe A qu'il vérifie. Il renvoie
un Result ; il lève Skip lorsque sa cible (lab, rapport d'outil) est indisponible.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


class Skip(Exception):
    """La cible du contrôle est indisponible : le contrôle n'a pas pu être exécuté."""


@dataclass
class Result:
    ok: bool
    detail: str


@dataclass
class Check:
    id: str
    controles: list[str]
    titre: str
    cible: str  # "lab" (lab démarré), "depot" (fichiers du dépôt) ou "rapport" (sortie d'outil)
    func: Callable[..., Result]


REGISTRY: dict[str, Check] = {}


def check(id: str, controles: list[str], titre: str, cible: str):
    def decorator(func):
        if id in REGISTRY:
            raise ValueError(f"contrôle {id} déclaré deux fois")
        REGISTRY[id] = Check(id, controles, titre, cible, func)
        return func
    return decorator


def _load_all():
    from . import lab, repository  # noqa: F401  (enregistrement par effet de bord)


_load_all()
