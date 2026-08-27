import unittest

from core.allied_armies import US_FIRST_ARMY,US_VIII_CORPS, US_XV_CORPS
from core.allied_advances_phase import do_allied_victory
from core.global_game_state import GlobalGameState
from core.map.map_utilities import add_units_to_space, do_opening_setup, reset_map
from core.map.map_spaces_us_1 import valognes, cherbourg, st_lo, coutances, avranches, mortain
from core.map.map_spaces_us_3 import st_malo, rennes, us_3_start_box

class TestUsThirdArmyActivation(unittest.TestCase):
    def setUp(self):
        GlobalGameState.us_third_army_activated = False

    def tearDown(self):
        reset_map()
        do_opening_setup()

    # =========================================================
    # ACTIVATION FAILURES
    # =========================================================

    def test_capture_cherbourg_no_activation_roll(self):
        add_units_to_space(valognes, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 8

        do_allied_victory(US_FIRST_ARMY, cherbourg)

        self.assertEqual(US_FIRST_ARMY.location, cherbourg)
        self.assertFalse(GlobalGameState.us_third_army_activated)

    def test_activation_fails_at_st_lo(self):
        add_units_to_space(cherbourg, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 7

        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=8)

        self.assertEqual(US_FIRST_ARMY.location, st_lo)
        self.assertFalse(GlobalGameState.us_third_army_activated)

    def test_activation_fails_at_coutances(self):
        add_units_to_space(st_lo, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 6

        do_allied_victory(US_FIRST_ARMY, coutances, activation_die_roll=8)

        self.assertEqual(US_FIRST_ARMY.location, coutances)
        self.assertFalse(GlobalGameState.us_third_army_activated)

    def test_activation_fails_at_avranches(self):
        add_units_to_space(coutances, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 5

        do_allied_victory(US_FIRST_ARMY, avranches, activation_die_roll=6)

        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertFalse(GlobalGameState.us_third_army_activated)


    # =========================================================
    # ACTIVATION SUCCESSES
    # =========================================================
    def test_activation_succeeds_at_st_lo(self):
        add_units_to_space(cherbourg, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 7

        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=10)

        self.assertTrue(GlobalGameState.us_third_army_activated)
        self.assertEqual(US_VIII_CORPS.location, us_3_start_box)
        self.assertEqual(US_XV_CORPS.location, us_3_start_box)
        self.assertEqual(GlobalGameState.us_viii_front_line, st_malo.track_number)
        self.assertEqual(GlobalGameState.us_xv_front_line, rennes.track_number)


    def test_activation_is_automatic_at_mortain(self):
        add_units_to_space(avranches, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 4

        do_allied_victory(US_FIRST_ARMY, mortain)

        self.assertEqual(US_FIRST_ARMY.location, mortain)
        self.assertTrue(GlobalGameState.us_third_army_activated)
        self.assertEqual(US_VIII_CORPS.location, us_3_start_box)
        self.assertEqual(US_XV_CORPS.location, us_3_start_box)
        self.assertEqual(GlobalGameState.us_viii_front_line, st_malo.track_number)
        self.assertEqual(GlobalGameState.us_xv_front_line, rennes.track_number)

    def test_activation_succeeds_at_coutances(self):
        add_units_to_space(st_lo, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 6
        do_allied_victory(US_FIRST_ARMY, coutances, activation_die_roll=9)
        self.assertTrue(GlobalGameState.us_third_army_activated)

    def test_activation_succeeds_at_avranches(self):
        add_units_to_space(coutances, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 5
        do_allied_victory(US_FIRST_ARMY, avranches, activation_die_roll=7)
        self.assertTrue(GlobalGameState.us_third_army_activated)

        
    def test_us_first_army_new_furthest_advance_triggers_activation_roll(self):
        add_units_to_space(cherbourg, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 7
        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=8)
        self.assertEqual(US_FIRST_ARMY.location, st_lo)
        self.assertEqual(GlobalGameState.us_first_army_furthest_advance, 6)
        self.assertFalse(GlobalGameState.us_third_army_activated)


    def test_us_first_army_recaptures_same_space_does_not_trigger_activation_roll(self):
        add_units_to_space(cherbourg, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 7

        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=8)
        self.assertEqual(GlobalGameState.us_first_army_furthest_advance, 6)

        st_lo.units.remove(US_FIRST_ARMY)
        cherbourg.units.append(US_FIRST_ARMY)
        US_FIRST_ARMY.location = cherbourg

        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=10)

        self.assertEqual(US_FIRST_ARMY.location, st_lo)
        self.assertEqual(GlobalGameState.us_first_army_furthest_advance, 6)
        self.assertFalse(GlobalGameState.us_third_army_activated)


    def test_activation_initializes_eighth_and_fifteenth_corps_front_lines(self):
        add_units_to_space(cherbourg, US_FIRST_ARMY)
        GlobalGameState.us_first_army_furthest_advance = 7

        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=10)

        self.assertEqual(GlobalGameState.us_viii_front_line, st_malo.track_number)
        self.assertEqual(GlobalGameState.us_xv_front_line, rennes.track_number)
