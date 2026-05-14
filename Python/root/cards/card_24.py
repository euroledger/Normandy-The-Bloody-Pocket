from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #24
# OPERATION SPRING
# =========================================================

card = Card(
    card_id=24,
    title="Operation Spring"
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

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
    ),

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    )
])


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-2,
        resource_type=ResourceType.SUPPLY
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # +1 Attack Strength 2nd BRIT

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=second_brit
    ),

    # +1 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    )
])