import unittest
from cards.card_38 import card as card_038
from cards.card_48 import card as card_048
from cards.card_45 import card as card_045
from cards.card_41 import card as card_041
from cards.card_43 import card as card_043
from cards.card_29 import card as card_029

from core.allied_armies import US_VIII_CORPS
from core.german_units import SS_1, SS_12
from core.map.map_utilities import add_units_to_space
from core.tables.weather import WEATHER_TABLE
from core.allied_advances_phase import do_allied_attacks
from core.map.map_spaces_us_3 import st_malo, brest
from core.map.map_model import hitler_approval_track
from core.global_game_state import GlobalGameState
from core.models import Strategy
from tests.core_mechanics.testing_utilities import setup_units_for_tests


class TestSiegeBrest(unittest.TestCase):
    def setUp(self):
        setup_units_for_tests()
        GlobalGameState.german_casualty_strategy = Strategy.UNIT_TEST
        self.weather = WEATHER_TABLE[1]
        brest.under_siege = False
        add_units_to_space(brest, [SS_1, SS_12])

    def test_us_viii_corps_begins_siege_of_brest(self):
        self.assertEqual(len(brest.units), 3)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertFalse(brest.under_siege)

        do_allied_attacks([US_VIII_CORPS], card_038, self.weather, die_roll=1)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(len(brest.units), 3)

    def test_us_viii_corps_begins_siege_of_brest_successive_die_rolls_6(self):
        self.assertEqual(len(brest.units), 3)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertFalse(brest.under_siege)

        do_allied_attacks([US_VIII_CORPS], card_038, self.weather, die_roll=6)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(len(brest.units), 1)

    def test_us_viii_corps_begins_siege_of_brest_with_air_power(self):
        # clear weather - VIII Corps gets Air Support
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(len(brest.units), 3)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertFalse(brest.under_siege)

        do_allied_attacks([US_VIII_CORPS], card_048, self.weather, die_roll=4)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(len(brest.units), 2)

    def test_us_viii_corps_resolve_siege(self):
        # clear weather - VIII Corps gets Air Support

        # SIEGE FIRST ROUND
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(len(brest.units), 3)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertFalse(brest.under_siege)

        do_allied_attacks([US_VIII_CORPS], card_038, self.weather, die_roll=6)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        # Two combat units eliminated by modified die roll of 4
        self.assertEqual(len(brest.units), 1)

        # SIEGE SECOND ROUND
        self.assertTrue(brest.under_siege)
        do_allied_attacks([US_VIII_CORPS], card_045, self.weather, die_roll=3)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        # No Combat Units Eliminated by modified die roll of 1
        self.assertEqual(len(brest.units), 1)

        # SIEGE THIRD ROUND
        self.assertTrue(brest.under_siege)
        do_allied_attacks([US_VIII_CORPS], card_041, self.weather, die_roll=6)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        # One Combat Unit Eliminated
        self.assertEqual(len(brest.units), 0)

        # SIEGE FOURTH ROUND
        self.assertTrue(brest.under_siege)
        do_allied_attacks([US_VIII_CORPS], card_043, self.weather, die_roll=4)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        # 3 Combat Units Eliminated, None left in Fortress
        self.assertEqual(len(brest.units), 0)

        # SIEGE FIFTH ROUND -Brest Falls
        self.assertTrue(brest.under_siege)
        do_allied_attacks([US_VIII_CORPS], card_029, self.weather, die_roll=6)
        self.assertFalse(brest.under_siege)
        self.assertEqual(US_VIII_CORPS.location, brest)

        # Brest capture costs 2 Hitler Approval
        self.assertEqual(hitler_approval_track.value, 4)
