from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

ninth_ss_panzer = GermanReinforcement(
    ReinforcementType.PZ_DIV,
    "9th SS Panzer"
)


# =========================================================
# CARD #14
# OPERATION EPSOM
# =========================================================

card = Card(
    card_id=14,
    title="Operation Epsom"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    second_brit,
    first_can
])


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=second_brit
    ),

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    )
])

# Carpet Bombing

card.air_power.text.append(
    "Carpet Bombing"
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=ninth_ss_panzer
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 4

card.actions.effects.extend([

    # +1 Attack Strength BRIT 2nd Army

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=second_brit
    ),

    # +1 Attack Strength CAN 1st Army

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=first_can
    ),

    # +1 DRM Transport

    Effect(
        modifier_type=ModifierType.DRM,
        value=1,
        resource_type=ResourceType.TRANSPORT
    ),

    # +2 Montgomery BRIT 2nd Army

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=2,
        label="Montgomery",
        target=second_brit
    )
])