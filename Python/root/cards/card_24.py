from core.models import *
from core.enums import *
from core.allied_armies import (BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #24
# OPERATION SPRING
# =========================================================

card = Card(card_id=24, title="Operation Spring")

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

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-2,
           resource_type=ResourceType.SUPPLY))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # +1 Attack Strength 2nd BRIT
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=BRITISH_SECOND_ARMY),

    # +1 Attack Strength 1st CAN
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY)
])
