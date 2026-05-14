from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_can = AlliedArmy("1st CAN", Nation.CAN_1)

kampfgruppe = GermanReinforcement(
    ReinforcementType.KAMPFGRUPPE,
    "Kampfgruppe"
)


# =========================================================
# CARD #40
# CANADIAN 4TH ARMORED DIVISION
# =========================================================

card = Card(
    card_id=40,
    title="Canadian 4th Armored Division"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(first_can)


# =========================================================
# AIR POWER
# =========================================================
# N/A


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    # 1 x Kampfgruppe

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=kampfgruppe,
        description="Deploy to map or Strategic Reserve (costs no action)"
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # -2 Attack Strength 1st CAN

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=-2,
        target=first_can
    ),

    # -1 DRM Transport

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
])