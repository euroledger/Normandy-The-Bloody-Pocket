from core.models import *
from core.enums import *
from core.allied_armies import CANADIAN_FIRST_ARMY

# =========================================================
# CARD #21
# OPERATION JUPITER
# =========================================================

card = Card(card_id=21, title="Operation Jupiter")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(CANADIAN_FIRST_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=2,
           target=CANADIAN_FIRST_ARMY))

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.append(
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY))
