import unittest
from cards.card_38 import card as card_038
from cards.card_5 import card as card_005
from cards.card_45 import card as card_045
from cards.card_41 import card as card_041
from cards.card_14 import card as card_014
from cards.card_18 import card as card_018
from core.allied_armies import CANADIAN_FIRST_ARMY
from core.german_units import SS_1, SS_12
from core.map.map_utilities import add_units_to_space, remove_units_from_space
from core.tables.weather import WEATHER_TABLE
from core.allied_advances_phase import do_allied_attacks, get_carpet_bombing_modifier
from core.map.map_spaces_can_1 import lebisey_wood, caen
from core.global_game_state import GlobalGameState
from core.map.map_model import hitler_approval_track
from core.models import Strategy
from tests.core_mechanics.testing_utilities import setup_units_for_tests


class TestSiegeCaen(unittest.TestCase):
    def setUp(self):
        setup_units_for_tests()
        remove_units_from_space(caen, CANADIAN_FIRST_ARMY)
        add_units_to_space(lebisey_wood, CANADIAN_FIRST_ARMY)
        GlobalGameState.german_casualty_strategy = Strategy.UNIT_TEST
        self.weather = WEATHER_TABLE[1]
        caen.under_siege = False
        add_units_to_space(caen, [SS_1, SS_12])

    def test_no_siege_caen(self):
        # Not > 6 differential - normal attack
        remove_units_from_space(caen, [SS_1, SS_12])
        self.assertEqual(len(caen.units), 1)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertFalse(caen.under_siege)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_038, self.weather, die_roll=6)
        self.assertFalse(caen.under_siege)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, caen)

    def test_canadian_first_army_begins_siege_of_caen(self):
        self.assertEqual(len(caen.units), 3)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertFalse(caen.under_siege)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_038, self.weather, die_roll=1)
        self.assertTrue(caen.under_siege)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertEqual(len(caen.units), 3)

    def test_canadian_first_army_begins_siege_of_caen_successive_die_rolls_6(self):
        self.assertEqual(len(caen.units), 3)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertFalse(caen.under_siege)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_038, self.weather, die_roll=6)
        self.assertTrue(caen.under_siege)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertEqual(len(caen.units), 1)

    def test_canadian_first_army_begins_siege_of_caen_with_air_power(self):
        # clear weather - Canadian First Army gets Air Support
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(len(caen.units), 3)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertFalse(caen.under_siege)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_005, self.weather, die_roll=4)
        self.assertTrue(caen.under_siege)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertEqual(len(caen.units), 2)

    def test_canadian_first_army_resolve_siege(self):
        # clear weather - Canadian First Army gets Air Support

        # SIEGE FIRST ROUND
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(len(caen.units), 3)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertFalse(caen.under_siege)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_038, self.weather, die_roll=6)
        self.assertTrue(caen.under_siege)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        # Two combat units eliminated by modified die roll of 4
        self.assertEqual(len(caen.units), 1)

        # SIEGE SECOND ROUND - +1 Attack Strength to 1st CAN
        self.assertTrue(caen.under_siege)
        do_allied_attacks([CANADIAN_FIRST_ARMY], card_045, self.weather, die_roll=3)
        self.assertTrue(caen.under_siege)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        # One Combat Units Eliminated by modified die roll of 1
        self.assertEqual(len(caen.units), 1)

        # SIEGE THIRD ROUND
        self.assertTrue(caen.under_siege)
        do_allied_attacks([CANADIAN_FIRST_ARMY], card_041, self.weather, die_roll=5)
        self.assertTrue(caen.under_siege)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertEqual(len(caen.units), 0)

        # SIEGE FOURTH ROUND -Caen Falls
        self.assertTrue(caen.under_siege)
        do_allied_attacks([CANADIAN_FIRST_ARMY], card_018, self.weather, die_roll=5)
        self.assertFalse(caen.under_siege)
        self.assertEqual(CANADIAN_FIRST_ARMY.location, caen)

        # Caen capture costs 1 Hitler Approval
        self.assertEqual(hitler_approval_track.value, 5)

    def test_canadian_first_army_carpet_bombing_counts_as_air_support(self):
        self.weather = WEATHER_TABLE[3]  # PARTLY CLEAR
        self.assertFalse(caen.under_siege)

        carpet_bombing = get_carpet_bombing_modifier(card_014, self.weather, die_roll=1)
        do_allied_attacks([CANADIAN_FIRST_ARMY], card_014, self.weather, carpet_bombing, die_roll=4)

        self.assertTrue(caen.under_siege)
