import unittest
from cards.card_28 import card as card_28
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies


class TestAttackStrengthCard28(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_28)
        
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
            "3rd US": 0,
            "2nd BRIT": 0,
            "1st CAN": 1
        }
        expected_has_air_support = {
            "1st US": False,
            "3rd US": False,
            "2nd BRIT": False,
            "1st CAN": False          
        }
            
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_28,
            expected_has_air_support=expected_has_air_support
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
            "1st US": 1,
            "3rd US": 0,
            "2nd BRIT": 0,
            "1st CAN": 1
        }
        expected_has_air_support = {
            "1st US": True,
            "3rd US": False,
            "2nd BRIT": False,
            "1st CAN": False          
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_28,
            num_jabos=weather.available_jabos,
            expected_has_air_support=expected_has_air_support
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
            "1st US": 1,
            "3rd US": 1,
            "2nd BRIT": 0,
            "1st CAN": 1
        }
        expected_has_air_support = {
            "1st US": True,
            "3rd US": True,
            "2nd BRIT": False,
            "1st CAN": False          
        }        
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_28,
            num_jabos=weather.available_jabos,
            expected_has_air_support=expected_has_air_support
        )

