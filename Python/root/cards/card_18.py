from core.models import *
from core.enums import *

# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)

# =========================================================
# CARD #18
# OPERATION CHARNWOOD
# =========================================================

card = Card(card_id=18, title="Operation Charnwood")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([second_brit, first_can])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st CAN
    Effect(modifier_type=ModifierType.AIR_POWER, value=1, target=first_can),

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER, value=1, target=second_brit)
])

# Carpet Bombing

card.air_power.text.append("Carpet Bombing")

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3
