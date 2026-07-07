import unittest

from cards.card_14 import card as card_14
from cards.card_18 import card as card_18
from cards.card_20 import card as card_20
from cards.card_15 import card as card_15
from cards.card_23 import card as card_23


class TestAirPower(unittest.TestCase):

    # =====================================================
    # CARPET BOMBING
    # =====================================================

    def test_card_14_has_carpet_bombing(self):

        self.assertTrue(
            card_14.air_power.has_carpet_bombing()
        )

    def test_card_18_has_carpet_bombing(self):

        self.assertTrue(
            card_18.air_power.has_carpet_bombing()
        )
        
    def test_card_20_has_carpet_bombing(self):

        self.assertTrue(
            card_20.air_power.has_carpet_bombing()
        )
        
    def test_card_15_does_not_have_carpet_bombing(self):

        self.assertFalse(
            card_15.air_power.has_carpet_bombing()
        )

    # =====================================================
    # AIR POWER VALUES
    # =====================================================

    def test_card_23_has_one_jabos(self):

        total_air_power = sum(
            effect.value
            for effect in card_23.air_power.effects
        )

        self.assertEqual(total_air_power, 1)


if __name__ == "__main__":
    unittest.main()