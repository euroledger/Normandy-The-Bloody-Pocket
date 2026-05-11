from core.models import *
from core.enums import *


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

second_ss_panzer = GermanReinforcement(
    ReinforcementType.PZ_DIV,
    "2nd SS Panzer"
)


# =========================================================
# CARD #13
# THE GREAT STORM
# =========================================================

card = Card(
    card_id=13,
    title="The Great Storm"
)


# =========================================================
# MILITARY
# =========================================================

card.military.text.append(
    "Weather automatically Overcast"
)


# =========================================================
# AIR POWER
# =========================================================
# N/A


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Reinforcement

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=second_ss_panzer
    ),

    # Gain 2 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=2,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4