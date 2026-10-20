"""Référentiel des 93 mesures de l'annexe A d'ISO/IEC 27001:2022."""

THEMES = {
    "5": ("Mesures organisationnelles", 37),
    "6": ("Mesures liées aux personnes", 8),
    "7": ("Mesures physiques", 14),
    "8": ("Mesures technologiques", 34),
}

CONTROL_IDS = [f"{theme}.{n}" for theme, (_, count) in THEMES.items() for n in range(1, count + 1)]

assert len(CONTROL_IDS) == 93


def theme_of(control_id: str) -> str:
    return control_id.split(".")[0]


def sort_key(control_id: str) -> tuple[int, int]:
    theme, number = control_id.split(".")
    return int(theme), int(number)
