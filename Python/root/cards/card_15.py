from core.models import *
from core.enums import *
from core.german_units import SS_10
from core.allied_armies import (BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #15
# OPERATION WINDSOR
# =========================================================

card = Card(card_id=15, title="Operation Windsor")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY),

    # +1 Jabos 1st CAN
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=CANADIAN_FIRST_ARMY)
])

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 10th SS Panzer reinforcement
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=SS_10),

    # Lose 1 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Lose 2 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-2,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4

card.actions.effects.extend([

    # +1 Attack Strength BRIT 2nd Army
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=BRITISH_SECOND_ARMY),

    # +1 Attack Strength CAN 1st Army
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY)
])
