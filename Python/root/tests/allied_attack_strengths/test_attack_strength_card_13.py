import unittest

from cards.card_13 import card as card_13
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects  # =========================================================
# TEST ATTACK STRENGTH CARD 6
# =========================================================


class TestAttackStrengthCard13(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_13)

    def test_attack_strength(self):
        print("\n  CARD 13 -> NO ARMIES OR AIR POWER")
        print("  ================================")

        expected_attack_strengths = {}
        assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_13)
