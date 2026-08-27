from core.actions.actions_helper import get_unit_location
from core.global_game_state import GlobalGameState
from core.models import *
from core.enums import *
from core.german_units import MEYER, PZ_2, SS_12
from core.map.map_model import strategic_reserve_box, eliminated_units_box
from core.allied_armies import (CANADIAN_FIRST_ARMY, BRITISH_SECOND_ARMY)

# =========================================================
# CARD #5
# PANZER MEYER
# =========================================================

card = Card(card_id=5, title="Panzer Meyer")


def event():
    ss12_location = get_unit_location(SS_12)

    if ss12_location is None or ss12_location is eliminated_units_box:
        print("12th SS PANZER ELIMINATED - MEYER HAS NO EFFECT")
        return

    GlobalGameState.meyer_available = True

    if ss12_location is strategic_reserve_box:
        print("12th SS PANZER IN STRATEGIC RESERVE - MEYER WAITS FOR ACTIONS PHASE")
        return


    ss12_location.units.append(MEYER)
    print(f"MEYER PLACED IN {ss12_location.name} WITH 12th SS PANZER")

card.event = event

# =========================================================
# MILITARY
# =========================================================
card.military.text.append("Meyer marker available for any combat involving 12th SS Panzer Division")

card.military.formations.append(CANADIAN_FIRST_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=CANADIAN_FIRST_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=PZ_2))

card.actions.effects.append(
    # +1 Meyer for 12th SS only
    Effect(modifier_type=ModifierType.COMMANDER, value=1, label="Meyer")
)

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-1,
           target=BRITISH_SECOND_ARMY))
