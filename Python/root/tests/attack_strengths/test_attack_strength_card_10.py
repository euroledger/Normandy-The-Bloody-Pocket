import unittest
from cards.card_10 import card as card_10
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from core.carpet_bombing import get_carpet_bombing_result
from core.carpet_bombing import ATTACK_CANCELLED
from core.card_utlities import calculate_attack_modifiers
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from tests.attack_strengths.attack_strength_test_utilities import get_armies



# =========================================================
# TEST OPERATION EPSOM ATTACK STRENGTH
# =========================================================


class TestAttackStrengthCard10(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_10)

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
            "1st CAN": 0
        }
            
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_10
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
            "2nd BRIT": 0,
            "1st CAN": 1
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_10,
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
            "2nd BRIT": 1,
            "1st CAN": 1
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_10,
            num_jabos=weather.available_jabos,
        )

      
