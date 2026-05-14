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
# CARD #28
# UPGRADE ARMIES
# =========================================================

card = Card(
    card_id=28,
    title="Upgrade Armies"
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

card.military.text.append(
    "Flip all armies (increasing their combat power by 1). "
    "Replace British XXXX Corps with British 2nd Army and "
    "British I Corps with Canadian 1st Army"
)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_us
    ),

    # +1 Jabos 3rd US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=third_us
    )
])


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    # +1 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    )
)