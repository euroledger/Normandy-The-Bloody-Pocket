from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)


# =========================================================
# CARD #12
# OPERATION BAGRATION
# =========================================================

card = Card(
    card_id=12,
    title="Operation Bagration"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_us)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_us
    )
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Lose 2 Hitler Approval

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-2,
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

card.actions.actions_available = 1

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
)