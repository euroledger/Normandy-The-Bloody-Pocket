from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #39
# TACTICAL REDEPLOYMENT
# =========================================================

card = Card(
    card_id=39,
    title="Tactical Redeployment"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    third_us,
    second_brit,
    first_can
])


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

card.resources.effects.append(

    # Lose 1 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1