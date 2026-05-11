from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #4
# 21st Panzer Counterattack
# =========================================================

card = Card(
    card_id=4,
    title="21st Panzer Counterattack"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    second_brit
])


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

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # -1 Defense Strength BRIT 2nd Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=second_brit
    ),

    # +1 Defense Strength CAN 1st Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=1,
        target=first_can
    ),

    # +1 Defense Strength US 1st Army

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
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