from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)

kampfgruppe = GermanUnit(
    ReinforcementType.KAMPFGRUPPE,
    "Kampfgruppe"
)


# =========================================================
# CARD #45
# DESPERATE DEFENSE
# =========================================================

card = Card(
    card_id=45,
    title="Desperate Defense"
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

    # +1 Jabos 1st US

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

    # 1 x Kampfgruppe

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=kampfgruppe,
        description="Deploy to map or Strategic Reserve (costs no action)"
    ),

    # Lose 1 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +1 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    ),

    # +1 Model

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=1,
        label="Model"
    )
])