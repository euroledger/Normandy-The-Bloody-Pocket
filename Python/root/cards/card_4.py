from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, BRITISH_SECOND_ARMY,
                                CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #4
# 21st Panzer Counterattack
# =========================================================

card = Card(card_id=4, title="21st Panzer Counterattack")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, BRITISH_SECOND_ARMY])

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

card.actions.actions_available = 2

card.actions.effects.extend([

    # -1 Defense Strength BRIT 2nd Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-1,
           target=BRITISH_SECOND_ARMY),

    # +1 Defense Strength CAN 1st Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY),

    # +1 Defense Strength US 1st Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=1,
           target=US_FIRST_ARMY)
])
