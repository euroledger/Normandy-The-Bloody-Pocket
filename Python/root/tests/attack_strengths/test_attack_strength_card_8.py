import unittest
from cards.card_8 import card as card_8
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies


# =========================================================
# TEST OPERATION EPSOM ATTACK STRENGTH
# =========================================================


class TestAttackStrengthCard8(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_8)
        
    def test_01_attack_strength_overcast(self):
        weather = get_weather_result(1)
        self.assertEqual(
            weather.available_jabos,
            0
        )

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {
            "2nd BRIT": 0,
        }
            
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_8
        )

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(
            weather.available_jabos,
            1
        )
        print("\n  PARTLY CLEAR")
        print("  ============")

        expected_attack_strengths = {
            "2nd BRIT": 1,
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_8,
            num_jabos=weather.available_jabos,
        )

    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)
        self.assertEqual(
            weather.available_jabos,
            ALL_JABOS_AVAILABLE
        )

        print("\n  CLEAR")
        print("  =====")
        expected_attack_strengths = {
            "2nd BRIT": 2,
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_8,
            num_jabos=weather.available_jabos,
        )
