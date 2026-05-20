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

flak_88 = GermanUnit(
    ReinforcementType.FLAK_88,
    "88mm Flak"
)


# =========================================================
# CARD #33
# OPERATION TOTALIZE
# =========================================================

card = Card(
    card_id=33,
    title="Operation Totalize"
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

card.air_power.effects.append(

    # +1 Jabos 1st CAN

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_can
    )
)

card.air_power.text.append(
    "Carpet Bombing"
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 2 x Flak 88

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=2,
        target=flak_88,
        description="Each marker can be immediately deployed to the map or placed in Strategic Reserve box"
    ),

    # Lose 1 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +1 Defense Strength 1st CAN

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=1,
        target=first_can
    ),

    # +2 Montgomery 1st CAN

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=2,
        label="Montgomery",
        target=first_can
    )
])