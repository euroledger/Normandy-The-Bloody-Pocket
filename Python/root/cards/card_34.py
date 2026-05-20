from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_can = AlliedArmy("1st CAN", Nation.CAN_1)

kampfgruppe = GermanUnit(
    ReinforcementType.KAMPFGRUPPE,
    "Kampfgruppe"
)


# =========================================================
# CARD #34
# OPERATION TRACTABLE
# =========================================================

card = Card(
    card_id=34,
    title="Operation Tractable"
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

card.air_power.text.append(
    "Carpet Bombing"
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

    # -1 Defense Strength 1st CAN

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=first_can
    ),

    # +1 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    )
])