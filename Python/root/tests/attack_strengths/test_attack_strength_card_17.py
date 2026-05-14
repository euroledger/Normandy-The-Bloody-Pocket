import unittest

from cards.card_17 import card as card_17
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from tests.attack_strengths.attack_strength_test_utilities import get_armies

class TestAttackStrengthCard17(unittest.TestCase):

    def setUp(self):
        self.armies = get_armies(card_17)
        
    def test_attack_strength(self):
        print("\n  CARD 17 -> NO AIR POWER")
        print("  ======================")

        expected_attack_strengths = {
            "1st US": 0,
            "2nd BRIT": 0
        }
        expected_has_air_support = {
            "1st US": False,
            "2nd BRIT": False
        }
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_17,
            expected_has_air_support=expected_has_air_support
        )