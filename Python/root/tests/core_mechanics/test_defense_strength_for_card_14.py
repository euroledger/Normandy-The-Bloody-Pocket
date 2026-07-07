import unittest
from cards.card_14 import card as card_014
from core.card_utilities import calculate_defense_modifiers
from core.map.map_spaces_us_1 import cherbourg
from core.map.map_spaces_brit_2 import tilly
from core.map.map_spaces_can_1 import lebisey_wood
from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY
from core.weather import WEATHER_TABLE


class TestDefenseStrengthsForCard14(unittest.TestCase):
    def setUp(self):
        self.weather = WEATHER_TABLE[1]

        BRITISH_SECOND_ARMY.flipped = False
        CANADIAN_FIRST_ARMY.flipped = False
        US_FIRST_ARMY.flipped = False

    def test_british_second_army_in_tilly_card_14(self):
        BRITISH_SECOND_ARMY.location = tilly
        result = calculate_defense_modifiers(card=card_014, army=BRITISH_SECOND_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 6)

    def test_canadian_first_army_in_lebisey_wood_card_14(self):
        CANADIAN_FIRST_ARMY.location = lebisey_wood
        result = calculate_defense_modifiers(card=card_014, army=CANADIAN_FIRST_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 4)

    def test_british_second_army_in_tilly_card_14_with_air_support(self):
        BRITISH_SECOND_ARMY.location = tilly
        result = calculate_defense_modifiers(card=card_014, army=BRITISH_SECOND_ARMY, weather=WEATHER_TABLE[6])
        self.assertEqual(result["defense_strength"], 7)

    def test_canadian_first_army_in_lebisey_wood_card_14_with_air_support(self):
        CANADIAN_FIRST_ARMY.location = lebisey_wood
        result = calculate_defense_modifiers(card=card_014, army=CANADIAN_FIRST_ARMY, weather=WEATHER_TABLE[6])
        self.assertEqual(result["defense_strength"], 5)

    def test_us_first_army_in_cherbourg_card_14(self):
        US_FIRST_ARMY.location = cherbourg
        result = calculate_defense_modifiers(card=card_014, army=US_FIRST_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 4)

