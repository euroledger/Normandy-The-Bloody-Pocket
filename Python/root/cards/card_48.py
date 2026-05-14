from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #48
# FALAISE GAP CLOSED
# =========================================================

card = Card(
    card_id=48,
    title="Falaise Gap Closed"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    third_us,
    second_brit,
    first_can
])


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_us
    ),

    # +1 Jabos 3rd US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=third_us
    ),

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
    ),

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    )
])


# =========================================================
# RESOURCES
# =========================================================

card.resources.display_text = "NONE"


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4

card.actions.effects.append(

    # +1 Model

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=1,
        label="Model"
    )
)