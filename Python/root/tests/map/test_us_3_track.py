# tests/map/test_us_3_tracks.py

import unittest

from core.map.map_spaces_us_3 import (
    us_viii_track,
    us_xv_track
)

from core.enums import SideType
from core.map.map_model import TerrainType

class TestUs3Tracks(unittest.TestCase):
    def test_us_viii_track_has_4_spaces(self):
        self.assertEqual(
            len(us_viii_track),
            4
        )

    def test_us_xv_track_has_5_spaces(self):
        self.assertEqual(
            len(us_xv_track),
            5
        )

    def test_st_malo(self):
        st_malo = us_viii_track[0]

        self.assertEqual(
            st_malo.name,
            "ST. MALO"
        )

        self.assertEqual(
            st_malo.terrain,
            TerrainType.TOWN
        )

        self.assertEqual(
            st_malo.track_number,
            7
        )

    def test_brest_is_fortified(self):
        brest = us_viii_track[1]

        self.assertEqual(
            brest.name,
            "BREST"
        )

        self.assertTrue(
            brest.fortified
        )

    def test_lorient_is_fortified(self):
        lorient = us_viii_track[2]

        self.assertEqual(
            lorient.name,
            "LORIENT"
        )

        self.assertTrue(
            lorient.fortified
        )

    def test_rennes_is_shared_space(self):
        self.assertIs(
            us_viii_track[-1],
            us_xv_track[0]
        )

    def test_xv_track_ends_at_falaise_gap(self):
        falaise_gap = us_xv_track[-1]

        self.assertEqual(
            falaise_gap.name,
            "FALAISE GAP"
        )

        self.assertEqual(
            falaise_gap.track_number,
            0
        )

    def test_xv_track_progression(self):
        expected_track_numbers = [
            4,
            3,
            2,
            1,
            0
        ]

        actual_track_numbers = [
            space.track_number
            for space in us_xv_track
        ]

        self.assertEqual(
            actual_track_numbers,
            expected_track_numbers
        )

    def test_all_spaces_start_german_controlled(self):
        all_spaces = (
            us_viii_track
            + us_xv_track[1:]
        )

        for space in all_spaces:
            self.assertEqual(
                space.controlling_player,
                SideType.GERMAN
            )

    def test_all_spaces_start_empty(self):
        all_spaces = (
            us_viii_track
            + us_xv_track[1:]
        )

        for space in all_spaces:
            self.assertEqual(
                len(space.units),
                0
            )