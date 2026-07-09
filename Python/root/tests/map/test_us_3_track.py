import unittest

from core.map.map_spaces_us_3 import us_viii_track, us_xv_track
from core.enums import SideType
from core.map.map_model import TerrainType


class TestUs3Tracks(unittest.TestCase):

    def test_us_viii_track_has_9_spaces(self):
        self.assertEqual(len(us_viii_track), 9)

    def test_us_xv_track_has_6_spaces(self):
        self.assertEqual(len(us_xv_track), 6)

    def test_st_malo(self):
        st_malo = us_viii_track[1]  # index shifted due to start box

        self.assertEqual(st_malo.name, "ST. MALO")
        self.assertEqual(st_malo.terrain, TerrainType.TOWN)
        self.assertEqual(st_malo.track_number, 7)

    def test_brest_is_fortified(self):
        brest = us_viii_track[2]

        self.assertEqual(brest.name, "BREST")
        self.assertTrue(brest.fortified)

    def test_lorient_is_fortified(self):
        lorient = us_viii_track[3]

        self.assertEqual(lorient.name, "LORIENT")
        self.assertTrue(lorient.fortified)

    def test_xv_track_ends_at_falaise_gap(self):
        falaise_gap = us_xv_track[-1]

        self.assertEqual(falaise_gap.name, "FALAISE GAP")

    def test_xv_track_order(self):
        expected_names = [
            "3RD US START BOX",
            "RENNES",
            "LE MANS",
            "ALENCON",
            "ARGENTAN",
            "FALAISE GAP",
        ]

        actual_names = [space.name for space in us_xv_track]

        self.assertEqual(actual_names, expected_names)

    def test_all_spaces_start_german_controlled(self):
        all_spaces = us_viii_track[1:] + us_xv_track[1:]

        for space in all_spaces:
            self.assertEqual(space.controlling_player, SideType.GERMAN)