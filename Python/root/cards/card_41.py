from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #41
# FALAISE POCKET
# =========================================================

card = Card(card_id=41, title="Falaise Pocket")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

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

card.actions.actions_available = 1

card.actions.effects.extend([

    # +1 Attack Strength 1st CAN
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY),

    # +1 Defense Strength 2nd BRIT
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=1,
           target=BRITISH_SECOND_ARMY)
])
