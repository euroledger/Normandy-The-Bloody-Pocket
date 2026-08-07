from core.models import *
from core.enums import *
from core.german_units import PZ_2
from core.allied_armies import (CANADIAN_FIRST_ARMY, BRITISH_SECOND_ARMY)

# =========================================================
# CARD #5
# PANZER MEYER
# =========================================================

card = Card(card_id=5, title="Panzer Meyer")

# =========================================================
# MILITARY
# =========================================================

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
