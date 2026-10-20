"""Échelle de cotation des risques (docs/02-risques/methodologie-risques.md)."""

APPETITE = 6  # au-delà, acceptation formelle du Directeur Général

LEVELS = [  # (seuil haut inclus, libellé)
    (3, "faible"),
    (6, "modéré"),
    (9, "élevé"),
    (16, "critique"),
]


def score(rating: dict) -> int:
    return rating["V"] * rating["I"]


def level(value: int) -> str:
    for upper, label in LEVELS:
        if value <= upper:
            return label
    raise ValueError(f"score hors échelle : {value}")


def needs_acceptance(risk: dict) -> bool:
    return score(risk["residuel"]) > APPETITE
