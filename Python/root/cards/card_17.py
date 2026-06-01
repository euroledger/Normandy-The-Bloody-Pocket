from core.models import *
from core.enums import *
from core.german_units import create_nebelwerfer
from core.allied_armies import (US_FIRST_ARMY, BRITISH_SECOND_ARMY)

# =========================================================
# CARD #17
# NEBELWERFERS
# =========================================================

card = Card(card_id=17, title="Nebelwerfers")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, BRITISH_SECOND_ARMY])

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
        target=create_nebelwerfer(),
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_nebelwerfer(),
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_nebelwerfer(),
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
])
# =========================================================
# RESOURCE DRMS
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.TRANSPORT))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3
