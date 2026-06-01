from core.models import *
from core.enums import *
from core.german_units import SS_1
from core.allied_armies import BRITISH_SECOND_ARMY
                                

# =========================================================
# CARD #8
# VILLERS-BOCAGE
# =========================================================

card = Card(card_id=8, title="Villers-Bocage")

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

# =========================================================
