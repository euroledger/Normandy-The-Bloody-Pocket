from core.models import *
from core.enums import *
from core.allied_armies import (BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #10
# V1 ROCKETS
# =========================================================

card = Card(card_id=10, title="V1 Rockets")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st CAN
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=CANADIAN_FIRST_ARMY),

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY)
])

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=2,
           resource_type=ResourceType.HITLER_APPROVAL))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3
