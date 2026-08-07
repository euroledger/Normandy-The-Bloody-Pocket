import unittest
from cards.card_37 import card as card_37
from core.tables.weather import get_weather_result
from core.tables.weather import ALL_JABOS_AVAILABLE
from core.tables.carpet_bombing import get_carpet_bombing_result
from core.tables.carpet_bombing import ATTACK_CANCELLED
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard37(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_37)

    def test_01_attack_strength_overcast(self):

        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {
            "US 1st ARMY": 1,
            "US 3rd ARMY": 2,
            "US VIII CORPS": 2,
            "US XV CORPS": 2,
        }
        expected_has_air_support = {
            "US 1st ARMY": False,
            "US 3rd ARMY": False,
            "US VIII CORPS": False,
            "US XV CORPS": False,
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_37, expected_has_air_support=expected_has_air_support)

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(weather.available_jabos, 1)

        print("\n  PARTLY CLEAR")
        print("  ============")
        expected_attack_strengths = {
            "US 1st ARMY": 1,
            "US 3rd ARMY": 3,
            "US VIII CORPS": 3,
            "US XV CORPS": 3,
        }
        expected_has_air_support = {
            "US 1st ARMY": False,
            "US 3rd ARMY": True,
            "US VIII CORPS": True,
            "US XV CORPS": True,
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_37, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)

    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        print("\n  CLEAR")
        print("  =====")

        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        expected_attack_strengths = {
            "US 1st ARMY": 1,
            "US 3rd ARMY": 3,
            "US VIII CORPS": 3,
            "US XV CORPS": 3,
        }
        expected_has_air_support = {
            "US 1st ARMY": False,
            "US 3rd ARMY": True,
            "US VIII CORPS": True,
            "US XV CORPS": True,
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_37, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)
