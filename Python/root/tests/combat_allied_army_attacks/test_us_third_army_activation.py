import unittest

from core.allied_armies import US_FIRST_ARMY,US_VIII_CORPS, US_XV_CORPS
from core.allied_advances_phase import do_allied_victory
from core.global_game_state import GlobalGameState
from core.map.map_utilities import add_units_to_space, do_opening_setup, reset_map
from core.map.map_spaces_us_1 import valognes, cherbourg, st_lo, coutances, avranches, mortain
from core.map.map_spaces_us_3 import st_malo, rennes

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

        do_allied_victory(US_FIRST_ARMY, cherbourg)

        self.assertEqual(US_FIRST_ARMY.location, cherbourg)
        self.assertFalse(GlobalGameState.us_third_army_activated)

    def test_activation_fails_at_st_lo(self):
        add_units_to_space(cherbourg, US_FIRST_ARMY)
        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=8)

        self.assertEqual(US_FIRST_ARMY.location, st_lo)
        self.assertFalse(GlobalGameState.us_third_army_activated)

    def test_activation_fails_at_coutances(self):
        add_units_to_space(st_lo, US_FIRST_ARMY)
        do_allied_victory(US_FIRST_ARMY, coutances, activation_die_roll=8)

        self.assertEqual(US_FIRST_ARMY.location, coutances)
        self.assertFalse(GlobalGameState.us_third_army_activated)

    def test_activation_fails_at_avranches(self):
        add_units_to_space(coutances, US_FIRST_ARMY)

        do_allied_victory(US_FIRST_ARMY, avranches, activation_die_roll=6)

        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertFalse(GlobalGameState.us_third_army_activated)


    # =========================================================
    # ACTIVATION SUCCESSES
    # =========================================================
    def test_activation_succeeds_at_st_lo(self):
        add_units_to_space(coutances, US_FIRST_ARMY)

        do_allied_victory(US_FIRST_ARMY, st_lo, activation_die_roll=10)

        self.assertTrue(GlobalGameState.us_third_army_activated)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(US_XV_CORPS.location, rennes)

    def test_activation_succeeds_at_coutances(self):
        add_units_to_space(avranches, US_FIRST_ARMY)

        do_allied_victory(US_FIRST_ARMY, coutances, activation_die_roll=9)

        self.assertTrue(GlobalGameState.us_third_army_activated)

    def test_activation_succeeds_at_avranches(self):
        add_units_to_space(mortain, US_FIRST_ARMY)

        do_allied_victory(US_FIRST_ARMY, avranches, activation_die_roll=7)

        self.assertTrue(GlobalGameState.us_third_army_activated)

    def test_activation_is_automatic_at_mortain(self):
        add_units_to_space(avranches, US_FIRST_ARMY)

        do_allied_victory(US_FIRST_ARMY, mortain)

        self.assertEqual(US_FIRST_ARMY.location, mortain)
        self.assertTrue(GlobalGameState.us_third_army_activated)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(US_XV_CORPS.location, rennes)