from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, CANADIAN_FIRST_ARMY,
                                BRITISH_SECOND_ARMY)

# =========================================================
# CARD #6
# FRENCH RESISTANCE
# =========================================================

card = Card(card_id=6, title="French Resistance")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================
# N/A

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Hitler Approval loss
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Supply loss
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY),

    # Transport loss
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1

card.actions.effects.extend([

    # +1 Attack Strength US 1st Army
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=US_FIRST_ARMY),

    # -1 Defense Strength BRIT 2nd Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-1,
           target=BRITISH_SECOND_ARMY),

    # -1 Defense Strength CAN 1st Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-1,
           target=CANADIAN_FIRST_ARMY)
])
