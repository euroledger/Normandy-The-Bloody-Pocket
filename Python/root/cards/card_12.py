from core.models import *
from core.enums import *
from core.allied_armies import US_FIRST_ARMY

# =========================================================
# CARD #12
# OPERATION BAGRATION
# =========================================================

card = Card(card_id=12, title="Operation Bagration")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(US_FIRST_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Lose 2 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-2,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY),
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1
