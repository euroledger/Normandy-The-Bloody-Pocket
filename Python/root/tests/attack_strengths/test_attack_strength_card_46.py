import unittest
from cards.card_46 import card as card_46
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from core.carpet_bombing import get_carpet_bombing_result
from core.carpet_bombing import ATTACK_CANCELLED
from core.card_utlities import calculate_attack_modifiers
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from tests.attack_strengths.attack_strength_test_utilities import get_armies



class TestAttackStrengthCard46(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_46)
        
    def test_01_attack_strength_overcast(self):
        self.assertEqual(len(self.armies), 1)
        
        weather = get_weather_result(1)
        self.assertEqual(
            weather.available_jabos,
            0
        )

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {
            "1st US": 0
        }
        expected_has_air_support = {
            "1st US": False          
        }
            
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_46,
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
            "1st US": 1
        }
        expected_has_air_support = {
            "1st US": True         
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_46,
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
            "1st US": 1
        }
        expected_has_air_support = {
            "1st US": True          
        }        
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_46,
            num_jabos=weather.available_jabos,
            expected_has_air_support=expected_has_air_support
        )

