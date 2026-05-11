from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)


# =========================================================
# CARD #7
# COTENTIN OFFENSIVE
# =========================================================

card = Card(
    card_id=7,
    title="Cotentin Offensive"
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
# None


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_us
    )
)