from core.models import *
from core.enums import *
from core.german_units import PZ_9
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY)

# =========================================================
# CARD #47
# RED BALL EXPRESS
# =========================================================

card = Card(card_id=47, title="Red Ball Express")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, US_THIRD_ARMY])

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
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=PZ_9),
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4

card.actions.effects.extend([
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-1,
           target=US_THIRD_ARMY),
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=2,
           target=US_THIRD_ARMY)
])
