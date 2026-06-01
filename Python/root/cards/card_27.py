from core.models import *
from core.enums import *

# =========================================================
# CARD #27
# HITLER ASSASSINATION ATTEMPT
# =========================================================

card = Card(card_id=27, title="Hitler Assassination Attempt")

# =========================================================
# MILITARY
# =========================================================

card.military.text.append("Flip Hitler Approval marker from 3 side to 4 side")

# =========================================================
# AIR POWER
# =========================================================
# N/A

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-3,
           resource_type=ResourceType.HITLER_APPROVAL))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1
