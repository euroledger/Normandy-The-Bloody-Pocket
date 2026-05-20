import unittest
from cards.card_4 import card as card_4
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies


# =========================================================
# TEST OPERATION EPSOM ATTACK STRENGTH
# =========================================================


class TestAttackStrengthCard4(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_4)

    def test_01_attack_strength_overcast(self):
        weather = get_weather_result(1)
        self.assertEqual(
            weather.available_jabos,
            0
        )

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {
            "1st US": 0,
            "2nd BRIT": 0
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_4
        )

    def test_02_attack_strength_partly_clear(self):
        print("\n  PARTLY CLEAR")
        print("  ============")
        weather = get_weather_result(2)
        self.assertEqual(
            weather.available_jabos,
            1
        )

        expected_attack_strengths = {
            "1st US": 1,
            "2nd BRIT": 0
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_4,
            num_jabos=weather.available_jabos,
        )

    def test_03_attack_strength_clear(self):
        print("\n  CLEAR")
        print("  =====")
        weather = get_weather_result(4)
        self.assertEqual(
            weather.available_jabos,
            ALL_JABOS_AVAILABLE
        )

        expected_attack_strengths = {
            "1st US": 1,
            "2nd BRIT": 0
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_4,
            num_jabos=weather.available_jabos,
        )
