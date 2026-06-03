import unittest
from cards.card_38 import card as card_038
from core.allied_armies import US_VIII_CORPS
from core.german_units import SS_1, SS_12
from core.map.map_utilities import add_units_to_space
from core.weather import WEATHER_TABLE
from core.military import do_allied_attacks
from core.map.map_spaces_us_3 import st_malo, brest
from core.global_game_state import GlobalGameState
from core.models import Strategy
from tests.testing_utilities import test_setup_units


class TestSiegeBrest(unittest.TestCase):
    def setUp(self):
        test_setup_units()
        GlobalGameState.german_casualty_strategy = Strategy.RANDOM
        self.weather = WEATHER_TABLE[1]
        add_units_to_space(brest, [SS_1, SS_12])

    def test_us_viii_corps_begins_siege_of_brest(self):
        self.assertEqual(len(brest.units), 3)
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertFalse(brest.under_siege)

        do_allied_attacks([US_VIII_CORPS], card_038, self.weather, die_roll=1)
        self.assertTrue(brest.under_siege)

        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(len(brest.units), 3)



