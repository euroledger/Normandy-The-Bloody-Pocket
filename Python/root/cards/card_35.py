from core.models import *
from core.enums import *
from core.conditions import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #35
# HITLER INTERVENTION - ULTRA
# =========================================================

card = Card(
    card_id=35,
    title="Hitler Intervention - ULTRA"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(second_brit)

card.military.text.append(
    "Hitler redeploys two Panzer Divisions "
    "(player's choice) and attacks any Allied Army "
    "(*ignore if player passes Hitler Approval Check)"
)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
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

card.actions.effects.extend([

    # +2 Defense Strength 1st US Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=2,
        target=first_us,
        condition=HitlerApprovalCheck(True)
    ),

    # +2 Defense Strength 2nd BRIT Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=2,
        target=second_brit,
        condition=HitlerApprovalCheck(True)
    ),

    # +2 Defense Strength 1st CAN Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=2,
        target=first_can,
        condition=HitlerApprovalCheck(True)
    ),

    # +2 Defense Strength 3rd US Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=2,
        target=third_us,
        condition=HitlerApprovalCheck(True)
    )
])