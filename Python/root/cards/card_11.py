from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)


# =========================================================
# CARD #11
# SIEGE OF CHERBOURG
# =========================================================

card = Card(
    card_id=11,
    title="Siege of Cherbourg"
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
        value=2,
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
        resource_type=ResourceType.TRANSPORT
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=2,
        target=first_us
    )
)