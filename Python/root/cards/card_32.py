from core.models import *
from core.enums import *
from core.allied_armies import US_FIRST_ARMY

# =========================================================
# CARD #32
# MORTAIN COUNTER ATTACK
# =========================================================

card = Card(card_id=32, title="Mortain Counter Attack")

# =========================================================
# MILITARY
# =========================================================

card.military.display_text = "NONE"

card.military.text.extend([
    "If 3rd Army has not taken St Malo, No Effect.",
    "2 panzer divs (player’s choice) placed in "
    "Liittich space.", "No Hitler roll; attack cannot be cancelled, "
    "even if supply level is 0.", "Must attack US 1st Army."
])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.display_text = "NONE"

# =========================================================
# RESOURCES
# =========================================================

card.resources.effects.extend([

    # Gain 2 Hitler Approval
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=2,
           resource_type=ResourceType.HITLER_APPROVAL),

    # Gain 2 Supply
    Effect(modifier_type=ModifierType.RESOURCE_GAIN,
           value=2,
           resource_type=ResourceType.SUPPLY)
])

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 3

card.actions.effects.append(

    # +2 Defense Strength 1st US
    Effect(modifier_type=ModifierType.DEFENSE_STRENGTH,
           value=2,
           target=US_FIRST_ARMY))
