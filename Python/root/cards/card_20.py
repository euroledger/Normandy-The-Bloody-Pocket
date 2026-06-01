from core.models import *
from core.enums import *
from core.allied_armies import (BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #20
# OPERATION GOODWOOD
# =========================================================

card = Card(card_id=20, title="Operation Goodwood")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=2,
           target=BRITISH_SECOND_ARMY))

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-2,
           resource_type=ResourceType.HITLER_APPROVAL))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # +1 Attack Strength 2nd BRIT
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=BRITISH_SECOND_ARMY),

    # +2 Montgomery 1st CAN
    Effect(modifier_type=ModifierType.COMMANDER,
           value=2,
           label="Montgomery",
           target=CANADIAN_FIRST_ARMY)
])
