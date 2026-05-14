from core.models import *
from core.enums import *


# =========================================================
# COMMON OBJECTS
# =========================================================

first_us = AlliedArmy("1st US", Nation.US_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)


# =========================================================
# GERMAN REINFORCEMENTS
# =========================================================

nebelwerfer = GermanReinforcement(
    ReinforcementType.NEBELWERFER,
    "Nebelwerfer"
)


# =========================================================
# CARD #17
# NEBELWERFERS
# =========================================================

card = Card(
    card_id=17,
    title="Nebelwerfers"
)


# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend([
    first_us,
    second_brit
])


# =========================================================
# AIR POWER
# =========================================================
# No Modifiers


# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=3,
        target=nebelwerfer,
        description="Each marker can be immediately deployed to map or placed in Strategic Reserve box"
    )
)


# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
)