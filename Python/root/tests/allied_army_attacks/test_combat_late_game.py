import unittest
from core.weather import WEATHER_TABLE
from core.military import do_allied_attacks
from cards.card_46 import card as card_046
from cards.card_37 import card as card_037
from core.allied_armies import US_FIRST_ARMY, US_VIII_CORPS
from core.map.map_spaces_us_1 import avranches, mortain, flers
from core.global_game_state import GlobalGameState
from core.models import Strategy
from tests.testing_utilities import test_setup_units
from core.map.map_spaces_us_3 import st_malo, brest

class TestCombatLateGame(unittest.TestCase):
    def setUp(self):
        test_setup_units()
        GlobalGameState.german_casualty_strategy = Strategy.RANDOM
        self.weather = WEATHER_TABLE[1]

    @unittest.skip
    def test_us_first_army_attack_mortain_natural_6(self):
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertEqual(len(mortain.units), 2)
        do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=6)
        self.assertEqual(US_FIRST_ARMY.location, mortain)
        self.assertGreater(len(flers.units), 0)

    def test_us_first_army_attack_mortain_natural_1(self):
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=1)
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertEqual(len(mortain.units), 2)
        self.assertEqual(mortain.units[0].name, "Kampfgruppe")
        self.assertEqual(mortain.units[1].name, "Flak 88")
        self.assertEqual(len(flers.units), 0)

    # AIR SUPPORT APPLIED - ALLIED VICTORY WITH ROLL OF 5
    # @unittest.skip
    def test_us_first_army_attack_mortain_clear_die_roll_5(self):
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertEqual(len(mortain.units), 2)
        do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=5)
        self.assertEqual(US_FIRST_ARMY.location, mortain)
        self.assertGreater(len(flers.units), 0)

    # US VIII CORPS ATTACK ON BREST, OVERCAST -> NO AIR SUPPORT
    def test_us_viii_corps_attack_brest_natural_6(self):
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(len(brest.units), 1)
        do_allied_attacks([US_VIII_CORPS], card_037, self.weather, die_roll=6)
        self.assertEqual(US_VIII_CORPS.location, brest)

    # US VIII CORPS ATTACK ON BREST, CLEAR -> AIR SUPPORT
    def test_us_viii_corps_attack_brest_clear_die_roll_3(self):
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(US_VIII_CORPS.location, st_malo)
        self.assertEqual(len(brest.units), 1)
        do_allied_attacks([US_VIII_CORPS], card_037, self.weather, die_roll=3)
        self.assertEqual(US_VIII_CORPS.location, brest)