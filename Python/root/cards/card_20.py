from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #20
# OPERATION GOODWOOD
# =========================================================

card = Card(
    card_id=20,
    title="Operation Goodwood"
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

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=2,
        target=second_brit
    )
)

card.air_power.text.append(
    "Carpet Bombing"
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-2,
        resource_type=ResourceType.HITLER_APPROVAL
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

    # +2 Montgomery 1st CAN

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=2,
        label="Montgomery",
        target=first_can
    )
])