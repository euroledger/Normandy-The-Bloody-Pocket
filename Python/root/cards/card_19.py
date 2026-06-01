from core.models import *
from core.enums import *
from core.german_units import create_flak88

# =========================================================
# CARD #19
# 88MM FLAK
# =========================================================

card = Card(card_id=19, title="88mm Flak")

# =========================================================
# MILITARY
# =========================================================
# No Modifiers

# =========================================================
# AIR POWER
# =========================================================
# No Modifiers

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
])
# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2
