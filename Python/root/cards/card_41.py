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
# CARD #41
# FALAISE POCKET
# =========================================================

card = Card(
    card_id=41,
    title="Falaise Pocket"
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

card.actions.actions_available = 1

card.actions.effects.extend([

    # +1 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    ),

    # +1 Defense Strength 2nd BRIT

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=1,
        target=second_brit
    )
])