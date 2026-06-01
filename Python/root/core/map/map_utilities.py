from core.german_units import PZ_21, create_flak88, create_nebelwerfer
from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_THIRD_ARMY, US_VIII_CORPS, US_XV_CORPS
from core.map.map_spaces_us_1 import us_1_start_box, carentan
from core.map.map_spaces_brit_2 import brit_2_start_box, bayeux
from core.map.map_spaces_can_1 import can_1_start_box, lebisey_wood
from core.map.map_spaces_us_3 import us_3_start_box
from core.models import AlliedArmy

def add_units_to_space(space, units):
    if not isinstance(units, list):
        units = [units]
    for unit in units:
        space.units.append(unit)
        if isinstance(unit, AlliedArmy):
            unit.location = space


def do_opening_setup():
    # =========================================================
    # OPENING SETUP - ALLIES
    # =========================================================

    add_units_to_space(us_1_start_box,US_FIRST_ARMY)
    add_units_to_space(brit_2_start_box,BRITISH_SECOND_ARMY)
    add_units_to_space(can_1_start_box, CANADIAN_FIRST_ARMY)
    add_units_to_space(us_3_start_box,[US_THIRD_ARMY, US_VIII_CORPS, US_XV_CORPS])

    # =========================================================
    # OPENING SETUP - GERMANS
    # =========================================================

    add_units_to_space(bayeux, [PZ_21, create_nebelwerfer(), create_nebelwerfer(), create_flak88()])
    add_units_to_space(lebisey_wood, [create_nebelwerfer(), create_nebelwerfer(), create_flak88()])
    add_units_to_space(carentan, [create_nebelwerfer()])
