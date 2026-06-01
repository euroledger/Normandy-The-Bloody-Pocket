from core.enums import ReinforcementType
from core.models import GermanUnit

PZ_LEHR = GermanUnit(ReinforcementType.PZ_DIV, "Panzer Lehr", combat_value=2)

SS_12 = GermanUnit(ReinforcementType.PZ_DIV, "12th SS Panzer", combat_value=2)

SS_1 = GermanUnit(ReinforcementType.PZ_DIV, "1st SS Panzer", combat_value=2)
SS_9 = GermanUnit(ReinforcementType.PZ_DIV, "9th SS Panzer", combat_value=2)
SS_10 = GermanUnit(ReinforcementType.PZ_DIV, "10th SS Panzer", combat_value=2)
SS_2 = GermanUnit(ReinforcementType.PZ_DIV, "2nd SS Panzer", combat_value=2)

TIGER_101 = GermanUnit(ReinforcementType.MARKER,
                       "101st Tiger Battalion",
                       combat_value=3)

PZ_21 = GermanUnit(ReinforcementType.PZ_DIV, "21st Panzer", combat_value=2)
PZ_116 = GermanUnit(ReinforcementType.PZ_DIV, "116th Panzer", combat_value=2)

SS_21_PZGRD = GermanUnit(ReinforcementType.PZ_DIV,
                         "17th SS Panzergrenadier",
                         combat_value=2)

PZ_2 = GermanUnit(ReinforcementType.PZ_DIV, "2nd Panzer", combat_value=2)

PZ_9 = GermanUnit(ReinforcementType.PZ_DIV, "9th Panzer", combat_value=2)


def create_nebelwerfer():
    return GermanUnit(ReinforcementType.NEBELWERFER,
                      "Nebelwerfer",
                      combat_value=1)


def create_flak88():
    return GermanUnit(ReinforcementType.FLAK_88, "Flak 88", combat_value=2)


def create_kampfgruppe():
    return GermanUnit(ReinforcementType.KAMPFGRUPPE,
                      "Kampfgruppe",
                      combat_value=1)
