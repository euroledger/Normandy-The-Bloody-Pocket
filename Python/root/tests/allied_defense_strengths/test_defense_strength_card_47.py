import unittest
from cards.card_47 import card as card_047
from core.card_utilities import calculate_defense_modifiers
from core.map.map_spaces_us_3 import st_malo
from core.allied_armies import US_VIII_CORPS
from core.tables.weather import WEATHER_TABLE


class TestDefenseStrengthsCard47(unittest.TestCase):
    def setUp(self):
        self.weather = WEATHER_TABLE[1]

    def test_us_viii_corps_in_st_malo(self):
        # WEATHER OVERCAST - NO AIR POWER
        US_VIII_CORPS.location = st_malo
        result = calculate_defense_modifiers(
            card=card_047, army=US_VIII_CORPS, weather=self.weather, print_modifiers=True
        )
        self.assertEqual(result["defense_strength"], 2)

    def test_us_viii_corps_in_st_malo_clear(self):
        # WEATHER CLEAR
        US_VIII_CORPS.location = st_malo
        self.weather = WEATHER_TABLE[6]
        result = calculate_defense_modifiers(
            card=card_047, army=US_VIII_CORPS, weather=self.weather, print_modifiers=True
        )
        self.assertEqual(result["defense_strength"], 2)
