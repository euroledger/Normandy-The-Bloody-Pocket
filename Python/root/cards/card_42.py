from core.models import *
from core.enums import *
from core.allied_armies import (US_THIRD_ARMY, BRITISH_SECOND_ARMY,
                                CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #42
# BRADLEY HALT ORDER
# =========================================================

card = Card(card_id=42, title="Bradley Halt Order")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

card.military.text.extend([
    "RETREAT 3rd Army.", "Applies if 3rd Army has reached "
    "Le Mans or further otherwise "
    "return card to draw pile."
])

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

# =========================================================
# RESOURCES
# =========================================================

card.resources.display_text = "NONE"

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # -2 Defense Strength 2nd BRIT
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-2,
           target=BRITISH_SECOND_ARMY),

    # -2 Defense Strength 1st CAN
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=-2,
           target=CANADIAN_FIRST_ARMY)
])
