from core.models import *
from core.enums import *
from core.german_units import SS_2

# =========================================================
# CARD #13
# THE GREAT STORM
# =========================================================

card = Card(card_id=13, title="The Great Storm")

# =========================================================
# MILITARY
# =========================================================

card.military.text.append("Weather automatically Overcast")

# =========================================================
# AIR POWER
# =========================================================
# N/A

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Reinforcement
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=SS_2),

    # Gain 2 Supply
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=2,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4
