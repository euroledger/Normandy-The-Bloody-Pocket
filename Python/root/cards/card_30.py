from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)


# =========================================================
# CARD #30
# OPERATION BLUECOAT
# =========================================================

card = Card(
    card_id=30,
    title="Operation Bluecoat"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(second_brit)


# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +2 Jabos 2nd BRIT

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=2,
        target=second_brit
    )
)


# =========================================================
# RESOURCES
# =========================================================

card.resources.display_text = "NONE"


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.extend([

    # +1 Attack Strength 2nd BRIT

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=1,
        target=second_brit
    ),

    # +2 Montgomery 2nd BRIT

    Effect(
        modifier_type=ModifierType.COMMANDER,
        value=2,
        label="Montgomery",
        target=second_brit
    )
])