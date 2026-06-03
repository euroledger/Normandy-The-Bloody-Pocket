import unittest

from cards.card_9 import card as card_9
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects  # =========================================================
# TEST ATTACK STRENGTH CARD 9
# =========================================================


class TestAttackStrengthCard9(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_9)

    def test_attack_strength(self):
        print("\n  CARD 9 -> NO ARMIES OR AIR POWER")
        print("  ================================")

        expected_attack_strengths = {}
        expected_has_air_support= {}
        # assert_attack_strengths(test_case=self, armies=self.armies, expected_attack_strengths=expected_attack_strengths, card=card_9)
        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            card=card_9,
            expected_has_air_support=expected_has_air_support
)