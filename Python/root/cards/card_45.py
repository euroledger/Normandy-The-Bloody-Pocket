from core.models import *
from core.enums import *
from core.german_units import create_kampfgruppe
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #45
# DESPERATE DEFENSE
# =========================================================

card = Card(card_id=45, title="Desperate Defense")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 1 x Kampfgruppe
    Effect(modifier_type=ModifierType.REINFORCEMENT,
           value=1,
           target=create_kampfgruppe(),
           description="Deploy to map or Strategic Reserve (costs no action)"),

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +1 Attack Strength 1st CAN
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY),

    # +1 Model
    Effect(modifier_type=ModifierType.COMMANDER, value=1, label="Model")
])
