from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# CARD #21
# OPERATION JUPITER
# =========================================================

card = Card(
    card_id=21,
    title="Operation Jupiter"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_can)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=2,
        target=first_can
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
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    )
)