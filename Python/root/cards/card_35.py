from core.models import *
from core.enums import *
from core.conditions import *
from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY,
                                BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_VIII_CORPS, US_XV_CORPS)

# =========================================================
# CARD #35
# HITLER INTERVENTION - ULTRA
# =========================================================

card = Card(card_id=35, title="Hitler Intervention - ULTRA")

card = Card(
    card_id=35,
    title="Hitler Intervention - ULTRA",
    hitler_intervention=True,
    hitler_intervention_target_armies=[US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY],
    hitler_intervention_panzer_count=2,
)
# =========================================================
# MILITARY
# =========================================================

card.military.formations.append(BRITISH_SECOND_ARMY)

card.military.text.append("Hitler redeploys two Panzer Divisions "
                          "(player's choice) and attacks any Allied Army "
                          "(*ignore if player passes Hitler Approval Check)")

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

card.actions.effects.extend([

    # +2 Defense Strength 1st US Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=2,
           target=US_FIRST_ARMY,
           condition=HitlerInterventionNoEffect(True)),

    # +2 Defense Strength 2nd BRIT Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=2,
           target=BRITISH_SECOND_ARMY,
           condition=HitlerInterventionNoEffect(True)),

    # +2 Defense Strength 1st CAN Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=2,
           target=CANADIAN_FIRST_ARMY,
           condition=HitlerInterventionNoEffect(True)),

    # +2 Defense Strength 3rd US Army
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=2,
           target=US_THIRD_ARMY,
           condition=HitlerInterventionNoEffect(True))
])
