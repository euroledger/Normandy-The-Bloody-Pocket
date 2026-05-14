from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_can = AlliedArmy("1st CAN", Nation.CAN_1)

kampfgruppe = GermanReinforcement(
    ReinforcementType.KAMPFGRUPPE,
    "Kampfgruppe"
)


# =========================================================
# CARD #44
# POLISH 1ST ARMORED DIVISION
# =========================================================

card = Card(
    card_id=44,
    title="Polish 1st Armored Division"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_can)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
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

    # +1 Defense Strength 1st CAN

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
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