import unittest

from cards.card_9 import card as card_9
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies
# =========================================================
# TEST ATTACK STRENGTH CARD 9
# =========================================================

class TestAttackStrengthCard9(unittest.TestCase):

    def setUp(self):
        self.armies = get_armies(card_9)
        
    def test_attack_strength(self):
        print("\n  CARD 9 -> NO ARMIES OR AIR POWER")
        print("  ================================")

        expected_attack_strengths = {
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_9
        )