from core.models import *
from core.enums import *
from core.german_units import PZ_116
from core.allied_armies import US_FIRST_ARMY

# =========================================================
# CARD #16
# BATTLE OF THE BOCAGE
# =========================================================

card = Card(card_id=16, title="Battle of the Bocage")

# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(US_FIRST_ARMY)

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # 116th Panzer reinforcement
    Effect(modifier_type=ModifierType.REINFORCEMENT, value=1, target=PZ_116),

    # Lose 1 Transport
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.TRANSPORT),
    Effect(modifier_type=ModifierType.DRM,
           value=-1,
           resource_type=ResourceType.TRANSPORT)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 2

card.actions.effects.extend([

    # +1 Attack Strength US 1st Army
    Effect(modifier_type=ModifierType.ATTACK_STRENGTH,
           value=1,
           target=US_FIRST_ARMY)
])
