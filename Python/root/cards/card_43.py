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
# CARD #43
# ALLIED ARTILLERY
# =========================================================

card = Card(
    card_id=43,
    title="Allied Artillery"
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

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    ),

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
    )
])


# =========================================================
# RESOURCES
# =========================================================

card.resources.display_text = "NONE"


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +2 Attack Strength 1st US

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=2,
        target=first_us
    ),

    # +2 Attack Strength 3rd US

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=2,
        target=third_us
    ),

    # +2 Attack Strength 2nd BRIT

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=2,
        target=second_brit
    ),

    # +2 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=2,
        target=first_can
    )
])