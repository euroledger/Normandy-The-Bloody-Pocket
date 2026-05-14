from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

third_us = AlliedArmy("3rd US", Nation.US_3)


# =========================================================
# CARD #29
# BRITTANY OFFENSIVE
# =========================================================

card = Card(
    card_id=29,
    title="Brittany Offensive"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(third_us)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=third_us
    )
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Lose 1 Hitler Approval

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    ),

    # Lose 1 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    # +2 Patton 3rd US Army

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=2,
        label="Patton",
        target=third_us
    )
)