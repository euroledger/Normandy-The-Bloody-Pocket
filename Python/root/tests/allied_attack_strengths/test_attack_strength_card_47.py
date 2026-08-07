import unittest
from cards.card_47 import card as card_47
from core.allied_armies import US_THIRD_ARMY
from core.tables.weather import get_weather_result
from core.tables.weather import ALL_JABOS_AVAILABLE
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard47(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_47)

    def test_01_attack_strength_overcast(self):
        self.assertEqual(len(self.armies), 3)

        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")
        expected_attack_strengths = {
            "US 1st ARMY": 0,
            "US 3rd ARMY": 2,
            "US VIII CORPS": 2,
            "US XV CORPS": 2
        }
        expected_has_air_support = {
            "US 1st ARMY": False,
            "US 3rd ARMY": False,
            "US VIII CORPS": False,
            "US XV CORPS": False
        }


        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_47, expected_has_air_support=expected_has_air_support)

    def test_02_attack_strength_partly_clear(self):
        weather = get_weather_result(2)
        self.assertEqual(weather.available_jabos, 1)

        print("\n  PARTLY CLEAR")
        print("  ============")
        expected_attack_strengths = {
            "US 1st ARMY": 1,
            "US 3rd ARMY": 2,
            "US VIII CORPS": 2,
            "US XV CORPS": 2
        }
        expected_has_air_support = {
            "US 1st ARMY": True,
            "US 3rd ARMY": False,
            "US VIII CORPS": False,
            "US XV CORPS": False
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_47, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)


    def test_03_attack_strength_clear(self):
        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        print("\n  CLEAR")
        print("  =====")

        weather = get_weather_result(4)

        self.assertEqual(weather.available_jabos, ALL_JABOS_AVAILABLE)

        expected_attack_strengths = {
            "US 1st ARMY": 1,
            "US 3rd ARMY": 2,
            "US VIII CORPS": 2,
            "US XV CORPS": 2
        }
        expected_has_air_support = {
            "US 1st ARMY": True,
            "US 3rd ARMY": False,
            "US VIII CORPS": False,
            "US XV CORPS": False
        }

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_47, num_jabos=weather.available_jabos, expected_has_air_support=expected_has_air_support)

    def test_04_attack_strength_overcast_us_third_army_broken_down(self):
        # break US 3rd Army down into its two corps
        # attack values should always be the same for both corps
        US_THIRD_ARMY.merged = False
        self.armies = get_armies_as_objects(card_47)
        self.assertEqual(len(self.armies), 3)

        weather = get_weather_result(1)
        self.assertEqual(weather.available_jabos, 0)

        print("\n  OVERCAST -> NO AIR POWER")
        print("  =================================")

        expected_attack_strengths = {"US 1st ARMY": 0, "US VIII CORPS": 2, "US XV CORPS": 2}
        expected_has_air_support = {"US 1st ARMY": False, "US VIII CORPS": False, "US XV CORPS": False}

        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_47, expected_has_air_support=expected_has_air_support)
