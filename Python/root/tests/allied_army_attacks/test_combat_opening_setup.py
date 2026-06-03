import unittest

from cards.card_3 import card as card_003

from core.weather import WEATHER_TABLE
from core.military import do_allied_attacks, advance_army_one_space
from core.map.map_utilities import do_opening_setup
from core.map.map_spaces_us_1 import utah_omaha, carentan
from core.map.map_spaces_brit_2 import gold_juno_sword_brit, bayeux
from core.map.map_spaces_can_1 import gold_juno_sword_can, lebisey_wood
from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY
from core.global_game_state import GlobalGameState
from core.models import Strategy


class TestAlliedAttacks(unittest.TestCase):
    def setUp(self):
        do_opening_setup()

        GlobalGameState.german_casualty_strategy = Strategy.RANDOM

        advance_army_one_space(US_FIRST_ARMY)
        self.weather = WEATHER_TABLE[1]

    def test_us_first_army_attack_carentan_natural_6(self):
        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)
        self.assertEqual(len(carentan.units), 1)

        do_allied_attacks([US_FIRST_ARMY], card_003, self.weather, die_roll=6)

        self.assertEqual(US_FIRST_ARMY.location, carentan)
        self.assertEqual(len(carentan.units), 1)

    def test_us_first_army_attack_carentan_natural_1(self):
        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)
        self.assertEqual(len(carentan.units), 1)

        do_allied_attacks([US_FIRST_ARMY], card_003, self.weather, die_roll=1)

        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)
        self.assertEqual(len(carentan.units), 1)
        self.assertEqual(carentan.units[0].combat_value, 1)

    # Allied Defeat

    def test_us_first_army_attack_carentan_roll_2(self):
        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)
        self.assertEqual(len(carentan.units), 1)

        do_allied_attacks([US_FIRST_ARMY], card_003, self.weather, die_roll=2)

        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)
        self.assertEqual(len(carentan.units), 1)
        self.assertEqual(carentan.units[0].combat_value, 1)

    # Allied Victory

    def test_us_first_army_attack_carentan_roll_3(self):
        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)
        self.assertEqual(len(carentan.units), 1)

        do_allied_attacks([US_FIRST_ARMY], card_003, self.weather, die_roll=3)

        self.assertEqual(US_FIRST_ARMY.location, carentan)
        self.assertEqual(len(carentan.units), 1)

    def test_british_second_army_attack_bayeux_natural_6(self):
        advance_army_one_space(BRITISH_SECOND_ARMY)

        self.assertEqual(BRITISH_SECOND_ARMY.location, gold_juno_sword_brit)
        self.assertEqual(len(bayeux.units), 4)

        do_allied_attacks([BRITISH_SECOND_ARMY], card_003, self.weather, die_roll=6)

        self.assertEqual(BRITISH_SECOND_ARMY.location, bayeux)
        self.assertEqual(len(bayeux.units), 1)


    def test_british_second_army_attack_bayeux_natural_1(self):
        advance_army_one_space(BRITISH_SECOND_ARMY)

        self.assertEqual(BRITISH_SECOND_ARMY.location, gold_juno_sword_brit)
        self.assertEqual(len(bayeux.units), 4)

        do_allied_attacks([BRITISH_SECOND_ARMY], card_003, self.weather, die_roll=1)

        self.assertEqual(BRITISH_SECOND_ARMY.location, gold_juno_sword_brit)
        self.assertEqual(len(bayeux.units), 4)

        self.assertEqual(bayeux.units[0].name, "21st Panzer")
        self.assertEqual(bayeux.units[1].name, "Nebelwerfer")
        self.assertEqual(bayeux.units[2].name, "Nebelwerfer")
        self.assertEqual(bayeux.units[3].name, "Flak 88")

        self.assertEqual(bayeux.units[0].combat_value, 2)
        self.assertEqual(bayeux.units[1].combat_value, 1)
        self.assertEqual(bayeux.units[2].combat_value, 1)
        self.assertEqual(bayeux.units[3].combat_value, 2)


    def test_canadian_first_army_attack_lebisey_wood_natural_6(self):
        advance_army_one_space(CANADIAN_FIRST_ARMY)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, gold_juno_sword_can)
        self.assertEqual(len(lebisey_wood.units), 3)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_003, self.weather, die_roll=6)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
        self.assertEqual(len(lebisey_wood.units), 1)

    def test_canadian_first_army_attack_lebisey_wood_natural_1(self):
        advance_army_one_space(CANADIAN_FIRST_ARMY)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, gold_juno_sword_can)
        self.assertEqual(len(lebisey_wood.units), 3)

        do_allied_attacks([CANADIAN_FIRST_ARMY], card_003, self.weather, die_roll=1)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, gold_juno_sword_can)
        self.assertEqual(len(lebisey_wood.units), 3)

        self.assertEqual(lebisey_wood.units[0].combat_value, 1)
        self.assertEqual(lebisey_wood.units[1].combat_value, 1)
        self.assertEqual(lebisey_wood.units[2].combat_value, 2)
