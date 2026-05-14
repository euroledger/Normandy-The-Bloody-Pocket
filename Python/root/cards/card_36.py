from core.models import *
from core.enums import *
from core.conditions import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #36
# HITLER INTERVENTION
# =========================================================

card = Card(
    card_id=36,
    title="Hitler Intervention"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_can)

card.military.text.append(
    "Hitler redeploys a Panzer Division "
    "(player's choice) and attacks the "
    "1st Canadian Army "
    "(*ignore if player passes Hitler Approval Check)"
)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    )
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Gain 1 Hitler Approval

    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=1,
        resource_type=ResourceType.HITLER_APPROVAL
    ),

    # Gain 2 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=2,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 0

card.actions.conditional_actions.append(

    Effect(
        modifier_type=None,
        value=2,
        condition=HitlerApprovalCheck(True)
    )
)