from core.models import *
from core.enums import *
from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY
)

# =========================================================
# CARD #2
# D-DAY LANDINGS: SECOND WAVE
# =========================================================

card = Card(card_id=2, title="D-Day Landings: Second Wave")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY
])

# =========================================================
# AIR POWER
# =========================================================
# N/A

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([
    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    ),

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
])

# =========================================================
# RESOURCE DRMS
# =========================================================

card.resources.effects.extend([
    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    ),
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([
    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=US_FIRST_ARMY
    )
])