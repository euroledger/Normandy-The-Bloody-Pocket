from core.global_game_state import GlobalGameState
from core.map.map_utilities import add_units_to_space, reset_german_panzer_divisions, reset_map
from core.german_units import SS_9, create_flak88, create_kampfgruppe, create_nebelwerfer
from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_THIRD_ARMY, US_VIII_CORPS, US_XV_CORPS
from core.map.map_spaces_us_1 import avranches, mortain
from core.map.map_spaces_brit_2 import villers_bocage, mont_pincon
from core.map.map_spaces_can_1 import caen, cagny
from core.map.map_spaces_us_3 import st_malo, rennes, brest, le_mans


def flip_all_allied_armies():
    for army in [
        US_FIRST_ARMY,
        BRITISH_SECOND_ARMY,
        CANADIAN_FIRST_ARMY,
        US_VIII_CORPS,
        US_XV_CORPS,
        US_THIRD_ARMY
    ]:
        army.flipped = True

def test_setup_units():
    reset_map()
    flip_all_allied_armies()
    reset_german_panzer_divisions()
    GlobalGameState.bocage_defense_modifier = -1


    # =========================================================
    # TEST SETUP - ALLIES
    # =========================================================

    add_units_to_space(avranches,US_FIRST_ARMY)
    add_units_to_space(villers_bocage,BRITISH_SECOND_ARMY)
    add_units_to_space(caen, CANADIAN_FIRST_ARMY)
    add_units_to_space(st_malo, US_VIII_CORPS)
    add_units_to_space(rennes, US_XV_CORPS)

    # =========================================================
    # TEST SETUP - GERMANS
    # =========================================================

    add_units_to_space(mortain, [create_kampfgruppe(), create_flak88()])
    add_units_to_space(mont_pincon, [create_nebelwerfer()])
    add_units_to_space(cagny, [SS_9, create_flak88()])
    add_units_to_space(brest, [create_kampfgruppe()])
    add_units_to_space(caen, [create_kampfgruppe()])
    add_units_to_space(le_mans, [create_kampfgruppe()])

    # FORTIFIED VILLAGES IN MORTAIN AND CAGNY
    mortain.fortified_village_modifier = 1
    cagny.fortified_village_modifier = 1
