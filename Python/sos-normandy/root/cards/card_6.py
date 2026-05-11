from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)


# =========================================================
# CARD #6
# FRENCH RESISTANCE
# =========================================================

card = Card(
    card_id=6,
    title="French Resistance"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    first_can
])


# =========================================================
# AIR POWER
# =========================================================
# N/A


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Hitler Approval loss

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    ),

    # Supply loss

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    ),

    # Transport loss

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1

card.actions.effects.extend([

    # +1 Attack Strength US 1st Army

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_us
    ),

    # -1 Defense Strength BRIT 2nd Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=second_brit
    ),

    # -1 Defense Strength CAN 1st Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=first_can
    )
])