from core.models import *
from core.enums import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)

# =========================================================
# CARD #28
# UPGRADE ARMIES
# =========================================================

card = Card(card_id=28, title="Upgrade Armies")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

card.military.text.append(
    "Flip all armies (increasing their combat power by 1). "
    "Replace British XXXX Corps with British 2nd Army and "
    "British I Corps with Canadian 1st Army")


def event():
    US_FIRST_ARMY.flip()
    BRITISH_SECOND_ARMY.flip()
    CANADIAN_FIRST_ARMY.flip()


card.event = event
# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.extend([

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY),

    # +1 Jabos 3rd US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1, target=US_THIRD_ARMY)
])

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.append(
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.HITLER_APPROVAL))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    # +1 Attack Strength 1st CAN
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=CANADIAN_FIRST_ARMY))
