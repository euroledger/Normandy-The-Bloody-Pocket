from core.models import *
from core.enums import *
from core.allied_armies import BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY
from core.german_units import SS_9

# =========================================================
# CARD #14
# OPERATION EPSOM
# =========================================================

card = Card(card_id=14, title="Operation Epsom")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY),

    # +1 Jabos 1st CAN
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=CANADIAN_FIRST_ARMY)
])

# Carpet Bombing

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=SS_9),

    # +1 DRM Transport
    Effect(modifier_type=ModifierType.DRM,
           value=1,
           resource_type=ResourceType.TRANSPORT),
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4

card.actions.effects.extend([

    # +1 Attack Strength BRIT 2nd Army
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=BRITISH_SECOND_ARMY),

    # +1 Attack Strength CAN 1st Army
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY),

    # +2 Montgomery BRIT 2nd Army
    Effect(modifier_type=ModifierType.COMMANDER,
           value=2,
           label="Montgomery",
           target=BRITISH_SECOND_ARMY)
])
