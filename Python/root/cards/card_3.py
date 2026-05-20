from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

ss_17_pz_grd = GermanUnit(
    ReinforcementType.PZ_DIV,
    "17 SS Pz Grd"
)


# =========================================================
# CARD #3
# CARENTAN
# =========================================================

card = Card(
    card_id=3,
    title="Carentan"
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

    # 17 SS Pz Grd reinforcement

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=ss_17_pz_grd
    ),

    # Truck icon = Transport loss

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    ),

    # Barrel icon = Supply loss

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_us
    ),

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
])