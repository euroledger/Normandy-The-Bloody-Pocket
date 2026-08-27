from core.german_units import MODEL
from core.global_game_state import GlobalGameState
from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)
from core.map.map_model import strategic_reserve_box

# =========================================================
# CARD #48
# FALAISE GAP CLOSED
# =========================================================

card = Card(card_id=48, title="Falaise Gap Closed")


def event():
    if GlobalGameState.model_in_command == True:
        strategic_reserve_box.units.append(MODEL)


card.event = event
# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY),

    # +1 Jabos 3rd US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_THIRD_ARMY),

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

card.resources.display_text = "NONE"

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4

card.actions.effects.append(

    # +1 Model
    Effect(modifier_type=ModifierType.COMMANDER, value=1, label="Model"))
