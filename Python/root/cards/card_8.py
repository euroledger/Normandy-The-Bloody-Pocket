from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

first_ss_panzer = GermanUnit(
    ReinforcementType.PZ_DIV,
    "1st SS Panzer"
)


# =========================================================
# CARD #8
# VILLERS-BOCAGE
# =========================================================

card = Card(
    card_id=8,
    title="Villers-Bocage"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(second_brit)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=2,
        target=second_brit
    )
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=first_ss_panzer
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # -1 Defense Strength US 1st Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=first_us
    ),

    # -2 Defense Strength BRIT 2nd Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-2,
        target=second_brit
    ),

    # -1 Defense Strength CAN 1st Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=first_can
    )
])