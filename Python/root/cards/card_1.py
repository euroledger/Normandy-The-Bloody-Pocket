from core.models import *
from core.enums import *
from core.german_units import PZ_LEHR, SS_12
from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY
)

card = Card(
    card_id=1,
    title="D-Day Landings: First Wave"
)

card.military.formations.extend([
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY
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