from core.models import *
from core.enums import *
from core.allied_armies import US_THIRD_ARMY

# =========================================================
# CARD #29
# BRITTANY OFFENSIVE
# =========================================================

card = Card(card_id=29, title="Brittany Offensive")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(US_THIRD_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_THIRD_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Lose 1 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    # +2 Patton 3rd US Army
    Effect(modifier_type=ModifierType.COMMANDER,
           value=2,
           label="Patton",
           target=US_THIRD_ARMY))
