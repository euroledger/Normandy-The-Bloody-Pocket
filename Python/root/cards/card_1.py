from core.models import *
from core.enums import *
from core.german_units import PZ_LEHR, SS_12

first_us = AlliedArmy("1st US", Nation.US_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)

card = Card(
    card_id=1,
    title="D-Day Landings: First Wave"
)

card.military.formations.extend([
    first_us,
    second_brit,
    first_can
])

card.resources.effects.extend([
    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=PZ_LEHR
    ),

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=SS_12
    )
])

card.actions.actions_available = 1

card.resources.effects.append(
    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
)