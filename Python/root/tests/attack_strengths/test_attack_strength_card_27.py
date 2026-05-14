import unittest

from cards.card_9 import card as card_27
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from tests.attack_strengths.attack_strength_test_utilities import get_armies

# =========================================================
# TEST ATTACK STRENGTH CARD 27
# =========================================================

class TestAttackStrengthCard27(unittest.TestCase):

    def setUp(self):
        self.armies = get_armies(card_27)
        
    def test_attack_strength(self):
        print("\n  CARD 27 -> NO ARMIES OR AIR POWER")
        print("  ================================")

        expected_attack_strengths = {
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_27
        )