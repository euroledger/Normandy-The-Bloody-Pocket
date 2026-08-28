from core.global_game_state import GlobalGameState
from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY)

# =========================================================
# CARD #26
# SHERMAN "RHINO"
# =========================================================

card = Card(card_id=26, title='Sherman "Rhino"')

card.military.text.append("Bocage Defense Value reduced from 2 to 1")

def event():
    GlobalGameState.bocage_defense_modifier = -1
 

card.event = event
# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, US_THIRD_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY),

    # +1 Jabos 3rd US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1, target=US_THIRD_ARMY)
])

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=1,
           resource_type=ResourceType.HITLER_APPROVAL))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(

    # +1 Attack Strength 1st US
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=US_FIRST_ARMY))
