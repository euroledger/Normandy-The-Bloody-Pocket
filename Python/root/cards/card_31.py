from core.models import *
from core.enums import *
from core.german_units import create_flak88
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY)

card = Card(card_id=31, title="US Third Army Elan")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([US_FIRST_ARMY, US_THIRD_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY))

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 2 x Flak 88
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description=
        "Can be immediately deployed to the map or placed in Strategic Reserve box"
    ),
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description=
        "Can be immediately deployed to the map or placed in Strategic Reserve box"
    ),

    # Lose 1 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    # +2 Patton 3rd US Army
    Effect(modifier_type=ModifierType.COMMANDER,
           value=2,
           label="Patton",
           target=US_THIRD_ARMY))
