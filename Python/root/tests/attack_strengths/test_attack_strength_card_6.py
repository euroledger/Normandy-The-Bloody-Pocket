import unittest

from cards.card_6 import card as card_6
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies
# =========================================================
# TEST ATTACK STRENGTH CARD 6
# =========================================================

class TestAttackStrengthCard6(unittest.TestCase):

    def setUp(self):
        self.armies = get_armies(card_6)
        
    def test_attack_strength(self):
        print("\n  CARD 6 -> NO AIR POWER")
        print("  ======================")

        expected_attack_strengths = {
            "1st US": 1,
            "1st CAN": 0
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_6
        )