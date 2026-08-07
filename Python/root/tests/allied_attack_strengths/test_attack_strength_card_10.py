import unittest
from cards.card_10 import card as card_10
from core.tables.weather import get_weather_result
from core.tables.weather import ALL_JABOS_AVAILABLE
from core.tables.carpet_bombing import ATTACK_CANCELLED
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects

# =========================================================
# TEST OPERATION EPSOM ATTACK STRENGTH
# =========================================================


class TestAttackStrengthCard10(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_10)

    def test_01_attack_strength_overcast(self):

        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {"BRITISH XXX CORPS": 0, "BRITISH I CORPS": 0}

        expected_has_air_support = {"BRITISH XXX CORPS": False, "BRITISH I CORPS": False}
        assert_attack_strengths(test_case=self, armies=self.armies,
                                expected_attack_strengths=expected_attack_strengths, card=card_10,
                                num_jabos=weather.available_jabos,
                                expected_has_air_support=expected_has_air_support)
    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(weather.available_jabos, 1)
        print("\n  PARTLY CLEAR")
        print("  ============")

        expected_attack_strengths = {"BRITISH XXX CORPS": 0, "BRITISH I CORPS": 1}

        expected_has_air_support = {"BRITISH XXX CORPS": False, "BRITISH I CORPS": True}
        assert_attack_strengths(test_case=self, armies=self.armies,
                                expected_attack_strengths=expected_attack_strengths, card=card_10,
                                num_jabos=weather.available_jabos,
                                expected_has_air_support=expected_has_air_support)


    def test_03_attack_strength_clear(self):
        print("\n  CLEAR")
        print("  =====")

        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        expected_attack_strengths = {"BRITISH XXX CORPS": 1, "BRITISH I CORPS": 1}

        expected_has_air_support = {"BRITISH XXX CORPS": True, "BRITISH I CORPS": True}
        assert_attack_strengths(test_case=self, armies=self.armies,
                                expected_attack_strengths=expected_attack_strengths, card=card_10,
                                num_jabos=weather.available_jabos,
                                expected_has_air_support=expected_has_air_support)

