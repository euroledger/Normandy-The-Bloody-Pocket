from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_can = AlliedArmy("1st CAN", Nation.CAN_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

second_pz = GermanUnit(
    ReinforcementType.PZ_DIV,
    "2nd Panzer"
)


# =========================================================
# CARD #5
# PANZER MEYER
# =========================================================

card = Card(
    card_id=5,
    title="Panzer Meyer"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_can)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    )
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=second_pz
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=second_brit
    )
)