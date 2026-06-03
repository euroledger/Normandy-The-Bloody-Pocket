import unittest

from cards.card_40 import card as card_40
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard40(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_40)

    def test_attack_strength(self):
        print("\n  CARD 40 -> NO AIR POWER")
        print("  ======================")

        expected_attack_strengths = {
            "BRITISH I CORPS": -2,
        }
        expected_has_air_support = {
            "BRITISH I CORPS": False,
        }
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_40, expected_has_air_support=expected_has_air_support)
