from core.models import *
from core.enums import *

first_us = AlliedArmy("1st US", Nation.US_1)
third_us = AlliedArmy("3rd US", Nation.US_3)

panzer_9 = GermanUnit(
    ReinforcementType.PZ_DIV,
    "9th Panzer"
)

card = Card(
    card_id=47,
    title="Red Ball Express"
)

card.military.formations.extend([
    first_us,
    third_us
])

card.air_power.effects.append(

    Effect(
        modifier_type=ModifierType.AIR_POWER,
        value=1,
        target=first_us
    )
)

card.resources.effects.extend([

    Effect(
        modifier_type=ModifierType.REINFORCEMENT,
        value=1,
        target=panzer_9
    ),

    Effect(
        modifier_type=ModifierType.RESOURCE_LOSS,
        value=-1,
        resource_type=ResourceType.SUPPLY
    )
])

card.actions.actions_available = 4

card.actions.effects.extend([

    Effect(
        modifier_type=ModifierType.DEFENSE_STRENGTH,
        value=-1,
        target=third_us
    ),

    Effect(
        modifier_type=ModifierType.ATTACK_STRENGTH,
        value=2,
        target=third_us
    )
])