from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

one_hundred_sixteenth_panzer = GermanUnit(
    ReinforcementType.PZ_DIV,
    "116th Panzer"
)


# =========================================================
# CARD #16
# BATTLE OF THE BOCAGE
# =========================================================

card = Card(
    card_id=16,
    title="Battle of the Bocage"
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

    # 116th Panzer reinforcement

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=one_hundred_sixteenth_panzer
    ),

    # Lose 1 Transport

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # +1 Attack Strength US 1st Army

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_us
    ),

    # -1 DRM Transport

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
])