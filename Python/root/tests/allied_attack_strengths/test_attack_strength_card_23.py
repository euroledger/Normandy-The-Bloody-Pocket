import unittest
from cards.card_23 import card as card_23
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard23(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_23)

    def test_01_attack_strength_overcast(self):
        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("ARMIES:", self.armies)
        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {"BRITISH XXX CORPS": 1}
        expected_has_air_support = {
            "BRITISH XXX CORPS": False,
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_23, expected_has_air_support=expected_has_air_support)

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(weather.available_jabos, 1)
        print("\n  PARTLY CLEAR")
        print("  ============")

        expected_attack_strengths = {
            "BRITISH XXX CORPS": 2,
        }
        expected_has_air_support = {
            "BRITISH XXX CORPS": True,
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_23, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)

    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)
        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        print("\n  CLEAR")
        print("  =====")
        expected_attack_strengths = {
            "BRITISH XXX CORPS": 2,
        }
        expected_has_air_support = {
            "BRITISH XXX CORPS": True,
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_23, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)
