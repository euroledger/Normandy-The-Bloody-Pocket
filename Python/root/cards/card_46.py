from core.models import *
from core.enums import *
from core.conditions import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY)

# =========================================================
# CARD #46
# HITLER INTERVENTION:
# ALENCON COUNTER ATTACK
# =========================================================

card = Card(
    card_id=46,
    title="Hitler Intervention: Alencon Counter Attack",
    hitler_intervention=True,
    hitler_intervention_target_armies=[US_THIRD_ARMY],
    hitler_intervention_panzer_count=2,
)
# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(US_FIRST_ARMY)

card.military.text.append("Hitler redeploys 2 pz divs/kampfgruppen "
                          "(player's choice) and attacks the "
                          "3rd US Army "
                          "(*ignore if player passes Hitler roll)")

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 1st US
    Effect(modifier_type=ModifierType.AIR_POWER, value=1,
           target=US_FIRST_ARMY))

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Gain 1 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=1,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Gain 2 Supply
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=2,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 0

card.actions.conditional_actions.append(
    Effect(modifier_type=None, value=2, condition=HitlerInterventionNoEffect(True)))

card.actions.effects.append(

    # +1 Defense Strength 3rd US
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=1,
           target=US_THIRD_ARMY,
           condition=HitlerInterventionNoEffect(True)))
