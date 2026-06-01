from core.models import *
from core.enums import *
from core.german_units import create_nebelwerfer
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY)

# =========================================================
# CARD #37
# PATTON
# =========================================================

card = Card(card_id=37, title="Patton")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, US_THIRD_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 3rd US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_THIRD_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 2 x Nebelwerfer
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_nebelwerfer(),
        description=
        "Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_nebelwerfer(),
        description=
        "Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    ),

    # Lose 1 Transport
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # +1 Attack Strength 1st US
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=US_FIRST_ARMY),

    # +2 Patton 3rd US Army
    Effect(modifier_type=ModifierType.COMMANDER,
           value=2,
           label="Patton",
           target=US_THIRD_ARMY)
])
