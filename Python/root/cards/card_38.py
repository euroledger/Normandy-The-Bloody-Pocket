from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)

kampfgruppe = GermanReinforcement(
    ReinforcementType.KAMPFGRUPPE,
    "Kampfgruppe"
)


# =========================================================
# CARD #38
# MODEL TAKES COMMAND
# =========================================================

card = Card(
    card_id=38,
    title="Model Takes Command"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    third_us,
    second_brit,
    first_can
])


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_us
    ),

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
    )
])


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

    # -1 DRM Transport

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    ),

    # +1 Model

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=1,
        label="Model"
    )
])