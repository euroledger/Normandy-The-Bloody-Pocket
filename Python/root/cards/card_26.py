from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)


# =========================================================
# CARD #26
# SHERMAN "RHINO"
# =========================================================

card = Card(
    card_id=26,
    title='Sherman "Rhino"'
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    third_us
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
    )
])


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=1,
        resource_type=ResourceType.HITLER_APPROVAL
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(

    # +1 Attack Strength 1st US

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_us
    )
)