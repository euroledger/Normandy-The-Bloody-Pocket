import unittest
from cards.card_2 import card as card_2
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies_as_objects


class TestAttackStrengthCard2(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_2)

    def test_attack_strength(self):
        self.assertEqual(len(self.armies), 3)
        expected_attack_strengths = {"US 1st ARMY": 1, "BRITISH XXX CORPS": 0, "BRITISH I CORPS": 0}

        expected_has_air_support = {
           "US 1st ARMY": False, "BRITISH XXX CORPS": False, "BRITISH I CORPS": False
        }

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            expected_has_air_support=expected_has_air_support,
            card=card_2,
            print_modifiers=True
        )