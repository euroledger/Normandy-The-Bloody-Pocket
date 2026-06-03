import unittest

from cards.card_6 import card as card_6
from tests.allied_attack_strengths.attack_strength_test_utilities import assert_attack_strengths
from core.card_utilities import get_armies, get_armies_as_objects  # =========================================================
# TEST ATTACK STRENGTH CARD 6
# =========================================================


class TestAttackStrengthCard6(unittest.TestCase):
    def setUp(self):
        self.armies = get_armies_as_objects(card_6)

    def test_attack_strength(self):
        print("\n  CARD 6 -> NO AIR POWER")
        print("  ======================")

        expected_attack_strengths = {"US 1st ARMY": 1, "BRITISH I CORPS": 0}
        expected_has_air_support = {"US 1st ARMY": False, "BRITISH I CORPS": False}

        assert_attack_strengths(
            test_case=self,
            armies=self.armies,
            expected_attack_strengths=expected_attack_strengths,
            expected_has_air_support=expected_has_air_support,
            card=card_6,
        )

