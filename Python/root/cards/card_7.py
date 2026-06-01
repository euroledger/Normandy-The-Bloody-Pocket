from core.models import *
from core.enums import *
from core.allied_armies import US_FIRST_ARMY

# =========================================================
# CARD #7
# COTENTIN OFFENSIVE
# =========================================================

card = Card(card_id=7, title="Cotentin Offensive")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(US_FIRST_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER, value=2,
           target=US_FIRST_ARMY))

# =========================================================
# RESOURCES
# =========================================================
# None

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=US_FIRST_ARMY))
