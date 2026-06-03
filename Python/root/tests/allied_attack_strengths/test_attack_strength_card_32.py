import unittest

from cards.card_9 import card as card_9
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects


class TestAttackStrengthCard32(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_9)

    def test_attack_strength(self):
        self.assertEqual(len(self.armies), 0)

        print("\n  CARD 32 -> NO ARMIES OR AIR POWER")
        print("  ================================")

        expected_attack_strengths = {}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_9)
