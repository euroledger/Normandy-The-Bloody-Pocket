from core.models import *
from core.enums import *
from core.allied_armies import BRITISH_SECOND_ARMY

# =========================================================
# CARD #23
# SHERMAN FIREFLY
# =========================================================

card = Card(card_id=23, title="Sherman Firefly")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(BRITISH_SECOND_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Gain 1 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=1,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Gain 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=1,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=BRITISH_SECOND_ARMY))
