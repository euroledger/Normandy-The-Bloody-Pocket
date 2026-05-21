from core.models import *
from core.enums import *

# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)

# =========================================================
# CARD #2
# D-DAY LANDINGS: SECOND WAVE
# =========================================================

card = Card(card_id=2, title="D-Day Landings: Second Wave")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([first_us, second_brit, first_can])

# =========================================================
# AIR POWER
# =========================================================
# N/A

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY)
])


# =========================================================
# RESOURCES
# =========================================================
card.resources.effects.extend([
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL),
])

# =========================================================
# ACTIONS
# =========================================================
card.actions.actions_available = 3

card.actions.effects.extend([
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=first_us)
])
