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

tenth_ss_panzer = GermanReinforcement(
    ReinforcementType.PZ_DIV,
    "10th SS Panzer"
)


# =========================================================
# CARD #15
# OPERATION WINDSOR
# =========================================================

card = Card(
    card_id=15,
    title="Operation Windsor"
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


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 10th SS Panzer reinforcement

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=tenth_ss_panzer
    ),

    # Lose 1 Hitler Approval

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.HITLER_APPROVAL
    ),

    # Lose 2 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-2,
        resource_type=ResourceType.SUPPLY
    )
])


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
    )
])