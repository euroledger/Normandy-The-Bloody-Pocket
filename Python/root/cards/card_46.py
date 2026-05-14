from core.models import *
from core.enums import *
from core.conditions import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)


# =========================================================
# CARD #46
# HITLER INTERVENTION:
# ALENCON COUNTER ATTACK
# =========================================================

card = Card(
    card_id=46,
    title="Hitler Intervention: Alencon Counter Attack"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_us)

card.military.text.append(
    "Hitler redeploys 2 pz divs/kampfgruppen "
    "(player's choice) and attacks the "
    "3rd US Army "
    "(*ignore if player passes Hitler roll)"
)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st US

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

card.actions.effects.append(

    # +1 Defense Strength 3rd US

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=1,
        target=third_us,
        condition=HitlerApprovalCheck(True)
    )
)