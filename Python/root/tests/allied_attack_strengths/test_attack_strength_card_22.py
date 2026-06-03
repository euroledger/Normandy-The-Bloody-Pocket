import unittest
from cards.card_22 import card as card_22
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from core.carpet_bombing import get_carpet_bombing_result
from core.carpet_bombing import ATTACK_CANCELLED
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard22(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_22)

    def test_01_attack_strength_overcast(self):

        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {"US 1st ARMY": 2, "BRITISH XXX CORPS": 2, "BRITISH I CORPS": 2}
        expected_has_air_support = {"US 1st ARMY": False, "BRITISH XXX CORPS": False, "BRITISH I CORPS": False}

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_22, expected_has_air_support=expected_has_air_support)

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(weather.available_jabos, 1)
        print("\n  PARTLY CLEAR")
        print("  ============")
        expected_attack_strengths = {"US 1st ARMY": 2, "BRITISH XXX CORPS": 2, "BRITISH I CORPS": 3}
        expected_has_air_support = {"US 1st ARMY": False, "BRITISH XXX CORPS": False, "BRITISH I CORPS": True}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_22, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)

    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        print("\n  CLEAR")
        print("  =====")

        expected_attack_strengths = {"US 1st ARMY": 2, "BRITISH XXX CORPS": 3, "BRITISH I CORPS": 3}
        expected_has_air_support = {"US 1st ARMY": False, "BRITISH XXX CORPS": True, "BRITISH I CORPS": True}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_22, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)
