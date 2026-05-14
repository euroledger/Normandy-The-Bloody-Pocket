from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)


# =========================================================
# CARD #25
# OPERATION COBRA
# =========================================================

card = Card(
    card_id=25,
    title="Operation Cobra"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_us)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +2 Jabos 1st US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=2,
        target=first_us
    )
)

# Carpet Bombing

card.air_power.text.append(
    "Carpet Bombing"
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Lose 1 Transport

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    ),

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

card.actions.actions_available = 2

card.actions.effects.append(

    # +1 Attack Strength 1st US

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_us
    )
)