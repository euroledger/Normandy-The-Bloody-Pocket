from core.models import *
from core.enums import *
from core.german_units import ROMMEL, SS_1
from core.allied_armies import BRITISH_SECOND_ARMY
from core.map.map_model import strategic_reserve_box


# =========================================================
# CARD #8
# ROMMEL
# =========================================================

card = Card(card_id=8, title="Rommel")


def event():
    strategic_reserve_box.units.append(ROMMEL)


card.event = event
# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(BRITISH_SECOND_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=2,
           target=BRITISH_SECOND_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=SS_1))

card.actions.effects.append(
    # +2 Rommel
    Effect(modifier_type=ModifierType.COMMANDER, value=2, label="Rommel")
)
# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3
