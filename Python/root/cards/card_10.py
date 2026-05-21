from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #10
# V1 ROCKETS
# =========================================================

card = Card(
    card_id=10,
    title="V1 Rockets"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    second_brit,
    first_can
])


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    ),

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
    )
])


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=2,
        resource_type=ResourceType.HITLER_APPROVAL
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3