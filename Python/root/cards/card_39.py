from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #39
# TACTICAL REDEPLOYMENT
# =========================================================

card = Card(card_id=39, title="Tactical Redeployment")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1
