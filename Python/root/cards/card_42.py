from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

third_us = AlliedArmy("3rd US", Nation.US_3)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #42
# BRADLEY HALT ORDER
# =========================================================

card = Card(
    card_id=42,
    title="Bradley Halt Order"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    third_us,
    second_brit,
    first_can
])

card.military.text.extend([

    "RETREAT 3rd Army.",

    "Applies if 3rd Army has reached "
    "Le Mans or further otherwise "
    "return card to draw pile."
])


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

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

card.actions.actions_available = 2

card.actions.effects.extend([

    # -2 Defense Strength 2nd BRIT

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-2,
        target=second_brit
    ),

    # -2 Defense Strength 1st CAN

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-2,
        target=first_can
    )
])