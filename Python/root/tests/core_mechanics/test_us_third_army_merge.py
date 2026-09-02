import unittest

from cards.card_42 import retreat_formation
from core.allied_advances_phase import advance_army_one_space
from core.allied_armies import US_THIRD_ARMY, US_VIII_CORPS, US_XV_CORPS
from core.global_game_state import GlobalGameState
from core.map.map_spaces_us_3 import us_3_start_box, st_malo, lorient, rennes, le_mans
from core.map.map_utilities import add_units_to_space, do_opening_setup, remove_units_from_space


class TestUsThirdArmyMerge(unittest.TestCase):
    def setUp(self):
        do_opening_setup()
        US_THIRD_ARMY.merged = False

    def assert_merged_at(self, space):
        self.assertTrue(US_THIRD_ARMY.merged)
        self.assertEqual(US_THIRD_ARMY.location, space)
        self.assertIn(US_THIRD_ARMY, space.units)
        self.assertNotIn(US_VIII_CORPS, space.units)
        self.assertNotIn(US_XV_CORPS, space.units)
        self.assertIsNone(US_VIII_CORPS.location)
        self.assertIsNone(US_XV_CORPS.location)
        self.assertEqual(GlobalGameState.us_3_front_line, space.track_number)

    def test_viii_corps_advance_into_xv_corps_merges(self):
        remove_units_from_space(st_malo, US_VIII_CORPS)
        add_units_to_space(lorient, US_VIII_CORPS)
        add_units_to_space(rennes, US_XV_CORPS)

        self.assertEqual(US_VIII_CORPS.location, lorient)
        self.assertEqual(US_XV_CORPS.location, rennes)
        advance_army_one_space(US_VIII_CORPS)
        self.assert_merged_at(rennes)
        self.assertNotIn(US_VIII_CORPS, lorient.units)

    def test_xv_corps_advance_into_viii_corps_merges(self):
        remove_units_from_space(rennes, US_XV_CORPS)
        add_units_to_space(us_3_start_box, US_XV_CORPS)
        self.assertEqual(US_XV_CORPS.location, us_3_start_box)
        remove_units_from_space(st_malo, US_VIII_CORPS)
        add_units_to_space(rennes, US_VIII_CORPS)


    def test_xv_corps_retreat_into_viii_corps_merges(self):
        remove_units_from_space(st_malo, US_VIII_CORPS)
        add_units_to_space(rennes, US_VIII_CORPS)
        remove_units_from_space(rennes, US_XV_CORPS)
        add_units_to_space(le_mans, US_XV_CORPS)
        self.assertEqual(US_VIII_CORPS.location, rennes)
        self.assertEqual(US_XV_CORPS.location, le_mans)
        result = retreat_formation(US_XV_CORPS)
        self.assertTrue(result)
        self.assert_merged_at(rennes)
        self.assertNotIn(US_XV_CORPS, le_mans.units)


if __name__ == "__main__":
    unittest.main()
