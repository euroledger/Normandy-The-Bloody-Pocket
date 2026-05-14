import unittest
from cards.card_21 import card as card_21
from core.weather import get_weather_result
from core.weather import ALL_JABOS_AVAILABLE
from core.carpet_bombing import get_carpet_bombing_result
from core.carpet_bombing import ATTACK_CANCELLED
from core.card_utlities import calculate_attack_modifiers
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from tests.attack_strengths.attack_strength_test_utilities import get_armies


class TestAttackStrengthCard21(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_21)
        
    def test_01_attack_strength_overcast(self):

        weather = get_weather_result(1)
        self.assertEqual(
            weather.available_jabos,
            0
        )

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {
            "1st CAN": 1
        }
        expected_has_air_support = {
            "1st CAN": False          
        }
            
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            expected_has_air_support=expected_has_air_support
        )

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(
            weather.available_jabos,
            1
        )
        # +2 CARPET BOMBING
        print("\n  PARTLY CLEAR -> +2 CARPET BOMBING")
        print("  =================================")
        carpet_bombing = get_carpet_bombing_result(
            die_roll=1,
            drm=weather.carpet_bombing_drm
        )
        self.assertEqual(carpet_bombing.attack_modifier, 2)

        expected_attack_strengths = {
            "1st CAN": 4
        }
        expected_has_air_support = {
            "1st CAN": True          
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing.attack_modifier,
            expected_has_air_support=expected_has_air_support
        )
        
        # +1 CARPET BOMBING
        print("\n  PARTLY CLEAR -> +1 CARPET BOMBING")
        print("  =================================")
        carpet_bombing = get_carpet_bombing_result(
            die_roll=4,
            drm=weather.carpet_bombing_drm
        )
        self.assertEqual(carpet_bombing.attack_modifier, 1)
        expected_attack_strengths = {
            "2nd CAN": 3,
        }
        expected_has_air_support = {
            "1st CAN": True          
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing.attack_modifier,
            expected_has_air_support = expected_has_air_support
        )
        carpet_bombing = get_carpet_bombing_result(
            die_roll=6,
            drm=weather.carpet_bombing_drm
        )

        self.assertEqual(
            carpet_bombing.attack_modifier,
            ATTACK_CANCELLED
        )

        print("\n  PARTLY CLEAR -> NO CARPET BOMBING")
        print("  =================================")
        expected_attack_strengths = {
            "1st CAN": 2
        }
        expected_has_air_support = {
            "1st CAN": True         
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing.attack_modifier,
            expected_has_air_support=expected_has_air_support
        )

    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)

        self.assertEqual(
            weather.available_jabos,
            ALL_JABOS_AVAILABLE
        )

        # +2 CARPET BOMBING
        carpet_bombing = get_carpet_bombing_result(
            die_roll=1,
            drm=weather.carpet_bombing_drm
        )
        print("\n  CLEAR -> +2 CARPET BOMBING")
        print("  ==========================")

        self.assertEqual(carpet_bombing.attack_modifier, 2)
        expected_attack_strengths = {
            "1st CAN": 5
        }
        expected_has_air_support = {
            "1st CAN": True         
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing.attack_modifier,
            expected_has_air_support=expected_has_air_support
        )

        # +1 CARPET BOMBING
        carpet_bombing = get_carpet_bombing_result(
            die_roll=5,
            drm=weather.carpet_bombing_drm
        )

        self.assertEqual(carpet_bombing.attack_modifier, 1)
        print("\n  CLEAR -> +1 CARPET BOMBING")
        print("  ==========================")
        expected_attack_strengths = {
            "1st CAN": 4
        }
        expected_has_air_support = {
            "1st CAN": True         
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing.attack_modifier,
            expected_has_air_support=expected_has_air_support
        )
        # ATTACK CANCELLED
        carpet_bombing = get_carpet_bombing_result(
            die_roll=6,
            drm=weather.carpet_bombing_drm
        )

        self.assertEqual(
            carpet_bombing.attack_modifier,
            ATTACK_CANCELLED
        )

        print("\n  CLEAR -> NO CARPET BOMBING")
        print("  ==========================")

        expected_attack_strengths = {
            "1st CAN": 3
        }
        expected_has_air_support = {
            "1st CAN": True          
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_21,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing.attack_modifier,
            expected_has_air_support=expected_has_air_support
        )
