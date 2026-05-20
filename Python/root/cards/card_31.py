from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

flak_88 = GermanUnit(
    ReinforcementType.FLAK_88,
    "88mm Flak"
)


# =========================================================
# CARD #31
# BRITTANY OFFENSIVE II
# =========================================================

card = Card(
    card_id=31,
    title="Brittany Offensive II"
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

card.air_power.effects.append(

    # +1 Jabos 1st US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_us
    )
)

card.air_power.text.append(
    "Carpet Bombing"
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 2 x Flak 88

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=2,
        target=flak_88,
        description="Each marker can be immediately deployed to the map or placed in Strategic Reserve box"
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