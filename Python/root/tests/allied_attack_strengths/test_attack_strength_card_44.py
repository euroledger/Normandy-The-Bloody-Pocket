import unittest
from cards.card_44 import card as card_44
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard44(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_44)

    def test_01_attack_strength_overcast(self):
        self.assertEqual(len(self.armies), 1)

        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {"BRITISH I CORPS": 0}
        expected_has_air_support = {"BRITISH I CORPS": False}

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_44, expected_has_air_support=expected_has_air_support)

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(weather.available_jabos, 1)
        print("\n  PARTLY CLEAR")
        print("  ============")
        expected_attack_strengths = {"BRITISH I CORPS": 1}
        expected_has_air_support = {"BRITISH I CORPS": True}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_44, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)

    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        print("\n  CLEAR")
        print("  =====")

        expected_attack_strengths = {"BRITISH I CORPS": 1}
        expected_has_air_support = {"BRITISH I CORPS": True}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_44, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)
