from core.models import *
from core.enums import *

first_us = AlliedArmy("1st US", Nation.US_1)
second_brit = AlliedArmy("2nd BRIT", Nation.BRIT_2)
first_can = AlliedArmy("1st CAN", Nation.CAN_1)

pz_lehr = GermanReinforcement(
    ReinforcementType.PZ_DIV,
    "Pz Lehr"
)

ss_12 = GermanReinforcement(
    ReinforcementType.PZ_DIV,
    "12 SS Pz"
)

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
        target=pz_lehr
    ),

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=ss_12
    )
])

card.actions.actions_available = 1

card.actions.effects.append(

    Effect(
        modifier_type=ModifierType.DRM,
        value=-1,
        resource_type=ResourceType.TRANSPORT
    )
)