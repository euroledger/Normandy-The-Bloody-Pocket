from core.enums import ReinforcementType
from core.models import GermanUnit


PZ_LEHR = GermanUnit(
    ReinforcementType.PZ_DIV,
    "Panzer Lehr",
    combat_value=2
)

SS_12 = GermanUnit(
    ReinforcementType.PZ_DIV,
    "12th SS Panzer",
    combat_value=2
)

PZ_21 = GermanUnit(
    ReinforcementType.PZ_DIV,
    "21st Panzer",
    combat_value=2
)

def create_nebelwerfer():
    return GermanUnit(
        ReinforcementType.NEBELWERFER,
        "Nebelwerfer",
        combat_value=1
)

def create_flak88():
    return GermanUnit(
        ReinforcementType.FLAK_88,
        "Flak 88",
        combat_value=2
)
