import unittest

from cards.card_17 import card as card_17
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard17(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_17)

    def test_attack_strength(self):
        print("\n  CARD 17 -> NO AIR POWER")
        print("  ======================")

        expected_attack_strengths = {"US 1st ARMY": 0, "BRITISH XXX CORPS": 0}
        expected_has_air_support = {"US 1st ARMY": False, "BRITISH XXX CORPS": False}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_17, expected_has_air_support=expected_has_air_support)
