from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

tiger_101 = GermanReinforcement(
    ReinforcementType.MARKER,
    "101st Tiger Battalion"
)


# =========================================================
# CARD #9
# MICHAEL WITTMANN
# =========================================================

card = Card(
    card_id=9,
    title="Michael Wittmann"
)


# =========================================================
# MILITARY
# =========================================================
# NONE


# =========================================================
# AIR POWER
# =========================================================
# N/A


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 101st Tiger Battalion

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=tiger_101,
        description="Available to deploy immediately"
    ),

    # Gain 2 Hitler Approval

    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=2,
        resource_type=ResourceType.HITLER_APPROVAL
    ),

    # Gain 1 Supply

    Effect(
        modifier_type=ModifierType.RESOURCE_GAIN,
        value=1,
        resource_type=ResourceType.SUPPLY
    )
])


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=1,
        target=second_brit
    )
)