import unittest

from core.models import AlliedArmy
from core.enums import Nation


class TestAlliedArmyCounters(unittest.TestCase):
    def setUp(self):
        self.first_canadian_army = AlliedArmy(
            name="BRITISH I CORPS",
            nation=Nation.CAN_1,
            reverse_name="CANADIAN 1st ARMY",
            strength=2,
            reverse_strength=4
        )

        self.second_british_army = AlliedArmy(
            name="BRITISH XXX CORPS",
            nation=Nation.BRIT_2,
            reverse_name="BRITISH 2nd ARMY",
            strength=2,
            reverse_strength=4
        )

        self.first_us_army = AlliedArmy(
            name="US 1st ARMY",
            nation=Nation.US_1,
            reverse_name="US 1st ARMY",
            strength=3,
            reverse_strength=4
        )

        self.us_viii_corps = AlliedArmy(
            name="US VIII CORPS",
            nation=Nation.US_3,
            strength=2
        )

        self.us_xv_corps = AlliedArmy(
            name="US XV CORPS",
            nation=Nation.US_3,
            strength=2
        )

        self.third_us_army = AlliedArmy(
            name="US 3rd ARMY",
            nation=Nation.US_3,
            strength=4
        )

    def test_first_canadian_army_front_side(self):
        self.assertEqual(
            self.first_canadian_army.display_name,
            "BRITISH I CORPS"
        )
        self.assertEqual(
            self.first_canadian_army.strength,
            2
        )
        self.assertFalse(
            self.first_canadian_army.flipped
        )

    def test_first_canadian_army_back_side(self):
        self.first_canadian_army.flip()

        self.assertEqual(
            self.first_canadian_army.display_name,
            "CANADIAN 1st ARMY"
        )
        self.assertEqual(
            self.first_canadian_army.strength,
            4
        )
        self.assertTrue(
            self.first_canadian_army.flipped
        )

    def test_second_british_army_front_side(self):
        self.assertEqual(
            self.second_british_army.display_name,
            "BRITISH XXX CORPS"
        )
        self.assertEqual(
            self.second_british_army.strength,
            2
        )
        self.assertFalse(
            self.second_british_army.flipped
        )

    def test_second_british_army_back_side(self):
        self.second_british_army.flip()

        self.assertEqual(
            self.second_british_army.display_name,
            "BRITISH 2nd ARMY"
        )
        self.assertEqual(
            self.second_british_army.strength,
            4
        )
        self.assertTrue(
            self.second_british_army.flipped
        )

    def test_first_us_army_front_side(self):
        self.assertEqual(
            self.first_us_army.display_name,
            "US 1st ARMY"
        )
        self.assertEqual(
            self.first_us_army.strength,
            3
        )
        self.assertFalse(
            self.first_us_army.flipped
        )

    def test_first_us_army_back_side(self):
        self.first_us_army.flip()

        self.assertEqual(
            self.first_us_army.display_name,
            "US 1st ARMY"
        )
        self.assertEqual(
            self.first_us_army.strength,
            4
        )
        self.assertTrue(
            self.first_us_army.flipped
        )

    def test_us_viii_corps(self):
        self.assertEqual(
            self.us_viii_corps.display_name,
            "US VIII CORPS"
        )
        self.assertEqual(
            self.us_viii_corps.strength,
            2
        )
        self.assertFalse(
            self.us_viii_corps.flipped
        )

    def test_us_xv_corps(self):
        self.assertEqual(
            self.us_xv_corps.display_name,
            "US XV CORPS"
        )
        self.assertEqual(
            self.us_xv_corps.strength,
            2
        )
        self.assertFalse(
            self.us_xv_corps.flipped
        )

    def test_third_us_army(self):
        self.assertEqual(
            self.third_us_army.display_name,
            "US 3rd ARMY"
        )
        self.assertEqual(
            self.third_us_army.strength,
            4
        )
        self.assertFalse(
            self.third_us_army.flipped
        )