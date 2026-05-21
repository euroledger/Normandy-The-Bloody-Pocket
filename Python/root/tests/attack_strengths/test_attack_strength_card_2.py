import unittest
from cards.card_2 import card as card_2
from tests.attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies

class TestAttackStrengthCard2(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies(card_2)

    def test_attack_strength(self):
        self.assertEqual(len(self.armies), 3)
        expected_attack_strengths = {
            "1st US": 1,
            "2nd BRIT": 0,
            "1st CAN": 0
        }
            
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_2,
            print_modifiers=True
        )
