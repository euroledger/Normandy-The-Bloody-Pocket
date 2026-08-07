from cards.card_20 import card as card_020
from cards.card_3 import card as card_003
from cards.card_4 import card as card_004
from cards.decks import draw_deck
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    eliminated_units_box,
    hitler_approval_track,
    in_transit_box,
    strategic_reserve_box,
    supply_track,
    transport_track,
)
from core.map.map_utilities import add_units_to_space, do_opening_setup, reset_german_panzer_divisions, reset_map
from core.german_units import SS_9, create_flak88, create_kampfgruppe, create_nebelwerfer
from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY,
    US_THIRD_ARMY,
    US_VIII_CORPS,
    US_XV_CORPS,
)
from core.map.map_spaces_us_1 import avranches, mortain
from core.map.map_spaces_brit_2 import villers_bocage, mont_pincon
from core.map.map_spaces_can_1 import caen, cagny
from core.map.map_spaces_us_3 import st_malo, rennes, brest, le_mans


def flip_all_allied_armies():
    for army in [US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_VIII_CORPS, US_XV_CORPS, US_THIRD_ARMY]:
        army.flipped = True


def setup_units_for_tests():
    reset_map()
    flip_all_allied_armies()
    reset_german_panzer_divisions()
    GlobalGameState.bocage_defense_modifier = -1
    hitler_approval_track.value = 6

    # =========================================================
    # TEST SETUP - ALLIES
    # =========================================================

    add_units_to_space(avranches, US_FIRST_ARMY)
    add_units_to_space(villers_bocage, BRITISH_SECOND_ARMY)
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


def reset_game_state_for_tests():
    do_opening_setup()

    draw_deck[:] = [
        card_003,
        card_004,
        card_020,
    ]

    GlobalGameState.cards_drawn = 0
    GlobalGameState.drawn_cards = []
    GlobalGameState.mid_deck_added = False
    GlobalGameState.late_deck_added = False
    GlobalGameState.current_card = None
    GlobalGameState.current_weather = None
    GlobalGameState.current_carpet_bombing = 0
    GlobalGameState.current_step = 1

    GlobalGameState.us_1_front_line = 11
    GlobalGameState.brit_2_front_line = 7
    GlobalGameState.can_1_front_line = 7
    GlobalGameState.us_3_front_line = 8
    GlobalGameState.us_viii_front_line = 7
    GlobalGameState.us_xv_front_line = 4

    transport_track.value = 5
    supply_track.value = 4
    hitler_approval_track.value = 6

    in_transit_box.units.clear()
    strategic_reserve_box.units.clear()
    eliminated_units_box.units.clear()
