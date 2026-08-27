# tests/test_actions.py

import unittest

from cards.card_1 import card as card_1
from cards.card_10 import card as card_10
from cards.card_25 import card as card_25
from cards.card_35 import card as card_35


# =========================================================
# TEST GAME STATE
# =========================================================

class MockGameState:

    def __init__(self, hitler_approval_check_passed=False):

        self.hitler_approval_check_passed = (
            hitler_approval_check_passed
        )


class TestActions(unittest.TestCase):

    # =====================================================
    # STANDARD ACTION CARDS
    # =====================================================

    def test_card_1_actions(self):

        self.assertEqual(
            card_1.total_actions(),
            1
        )

    def test_card_10_actions(self):

        self.assertEqual(
            card_10.total_actions(),
            3
        )

    def test_card_25_actions(self):

        self.assertEqual(
            card_25.total_actions(),
            2
        )





if __name__ == "__main__":
    unittest.main()