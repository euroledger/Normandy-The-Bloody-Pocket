import unittest
from core.map.map_utilities import add_units_to_space
from core.tables.weather import WEATHER_TABLE
from core.allied_advances_phase import do_allied_attacks
from cards.card_46 import card as card_046
from cards.card_37 import card as card_037
from core.allied_armies import US_FIRST_ARMY, US_VIII_CORPS
from core.map.map_spaces_us_1 import avranches, mortain, flers, vire
from core.global_game_state import GlobalGameState
from core.models import Strategy
from tests.core_mechanics.testing_utilities import setup_units_for_tests
from core.map.map_spaces_us_3 import st_malo, brest


class TestCombatLateGame(unittest.TestCase):
    def setUp(self):
        setup_units_for_tests()
        GlobalGameState.german_casualty_strategy = Strategy.UNIT_TEST
        self.weather = WEATHER_TABLE[1]

    def test_us_first_army_attack_mortain_natural_6(self):
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertEqual(len(mortain.units), 2)
        do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=6)
        self.assertEqual(US_FIRST_ARMY.location, mortain)
        self.assertGreater(len(vire.units), 0)

    def test_us_first_army_attack_mortain_natural_1(self):
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=1)
        self.assertEqual(US_FIRST_ARMY.location, avranches)


    # AIR SUPPORT APPLIED - ALLIED VICTORY WITH ROLL OF 5
    def test_us_first_army_attack_mortain_clear_die_roll_5(self):
        self.weather = WEATHER_TABLE[6]
        self.assertEqual(US_FIRST_ARMY.location, avranches)
        self.assertEqual(len(mortain.units), 2)
        do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=5)
        self.assertEqual(US_FIRST_ARMY.location, mortain)
        self.assertGreater(len(vire.units), 0)
        

    def test_us_first_army_reaches_falaise_gap_natural_6_game_over(self):
        avranches.units.remove(US_FIRST_ARMY)        
        add_units_to_space(flers, US_FIRST_ARMY)
        result = do_allied_attacks([US_FIRST_ARMY], card_046, self.weather, die_roll=6)
        self.assertTrue(result)
        self.assertEqual(US_FIRST_ARMY.location.name, "FALAISE GAP")
        

    def test_falaise_gap_ends_allied_attacks_immediately(self):
        avranches.units.remove(US_FIRST_ARMY)
        add_units_to_space(flers, US_FIRST_ARMY)

        result = do_allied_attacks([US_FIRST_ARMY, US_VIII_CORPS], card_046, self.weather, die_roll=6)

        self.assertTrue(result)
        self.assertEqual(US_FIRST_ARMY.location.name, "FALAISE GAP")

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
