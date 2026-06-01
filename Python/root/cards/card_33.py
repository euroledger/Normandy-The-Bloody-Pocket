from core.models import *
from core.enums import *
from core.german_units import create_flak88
from core.allied_armies import (BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #33
# OPERATION TOTALIZE
# =========================================================

card = Card(card_id=33, title="Operation Totalize")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st CAN
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=CANADIAN_FIRST_ARMY))

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Flak 88 #1
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description=
        "Each marker can be immediately deployed to the map or placed in Strategic Reserve box"
    ),

    # Flak 88 #2
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=create_flak88(),
        description=
        "Each marker can be immediately deployed to the map or placed in Strategic Reserve box"
    ),

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +1 Defense Strength 1st CAN
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY),

    # +2 Montgomery 1st CAN
    Effect(modifier_type=ModifierType.COMMANDER,
           value=2,
           label="Montgomery",
           target=CANADIAN_FIRST_ARMY)
])
