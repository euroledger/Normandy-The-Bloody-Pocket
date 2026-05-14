from core.models import *
from core.enums import *


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

flak_88 = GermanReinforcement(
    ReinforcementType.FLAK_88,
    "88mm Flak"
)


# =========================================================
# CARD #19
# 88MM FLAK
# =========================================================

card = Card(
    card_id=19,
    title="88mm Flak"
)


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

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=3,
        target=flak_88,
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2