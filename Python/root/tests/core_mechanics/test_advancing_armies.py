# tests/test_advancing_armies.py

import unittest

from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY,
                         CANADIAN_FIRST_ARMY)

from cards.card_1 import card as card_1
from cards.card_5 import card as card_5
from cards.card_11 import card as card_11
from cards.card_14 import card as card_14
from cards.card_22 import card as card_22
from cards.card_47 import card as card_47


class TestAdvancingArmies(unittest.TestCase):

    def test_card_1_advancing_armies(self):
        self.assertEqual(
            card_1.advancing_armies(),
            [US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

    def test_card_5_advancing_armies(self):
        self.assertEqual(card_5.advancing_armies(), [CANADIAN_FIRST_ARMY])

    def test_card_11_advancing_armies(self):
        self.assertEqual(card_11.advancing_armies(), [US_FIRST_ARMY])

    def test_card_14_advancing_armies(self):
        self.assertEqual(card_14.advancing_armies(),
                         [BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

    def test_card_22_advancing_armies(self):
        self.assertEqual(
            card_22.advancing_armies(),
            [US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

    def test_card_47_advancing_armies(self):
        self.assertEqual(card_47.advancing_armies(),
                         [US_FIRST_ARMY, US_THIRD_ARMY])

    def test_canadian_army_advances_on_card_14(self):
        self.assertTrue(card_14.is_army_advancing(CANADIAN_FIRST_ARMY))

    def test_canadian_army_does_not_advance_on_card_11(self):
        self.assertFalse(card_11.is_army_advancing(CANADIAN_FIRST_ARMY))


if __name__ == "__main__":
    unittest.main()
