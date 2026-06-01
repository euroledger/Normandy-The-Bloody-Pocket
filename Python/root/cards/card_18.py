from core.models import *
from core.enums import *
from core.allied_armies import (BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #18
# OPERATION CHARNWOOD
# =========================================================

card = Card(card_id=18, title="Operation Charnwood")

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

# Carpet Bombing

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3
