from core.models import *
from core.enums import *
from core.german_units import create_kampfgruppe
from core.allied_armies import CANADIAN_FIRST_ARMY

# =========================================================
# CARD #40
# CANADIAN 4TH ARMORED DIVISION
# =========================================================

card = Card(card_id=40, title="Canadian 4th Armored Division")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(CANADIAN_FIRST_ARMY)

# =========================================================
# AIR POWER
# =========================================================
# N/A

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

    # -2 Attack Strength 1st CAN
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=-2,
           target=CANADIAN_FIRST_ARMY)
])
