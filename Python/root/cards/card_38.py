from core.models import *
from core.enums import *
from core.german_units import create_kampfgruppe
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #38
# MODEL TAKES COMMAND
# =========================================================

card = Card(card_id=38, title="Model Takes Command")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY),

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY)
])

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 1 x Kampfgruppe
    Effect(modifier_type=ModifierType.REINFORCEMENT,
           value=1,
           target=create_kampfgruppe(),
           description="Deploy to map or Strategic Reserve (costs no action)"),

    # -1 DRM Transport
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +1 Model
    Effect(modifier_type=ModifierType.COMMANDER, value=1, label="Model")
])
