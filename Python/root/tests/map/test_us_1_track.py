# tests/map/test_us_1_track.py

import unittest
from core.map.map_spaces_us_1 import us_1_track
from core.enums import SideType
from core.map.map_model import TerrainType

class TestUs1Track(unittest.TestCase):
    def test_track_has_12_spaces(self):
        self.assertEqual(
            len(us_1_track),
            12
        )

    def test_start_box(self):
        start_box = us_1_track[0]

        self.assertEqual(
            start_box.name,
            "1ST US START BOX"
        )

        self.assertEqual(
            start_box.terrain,
            TerrainType.START_BOX
        )

        self.assertEqual(
            start_box.controlling_player,
            SideType.ALLIED
        )

    def test_falaise_gap(self):
        falaise_gap = us_1_track[-1]

        self.assertEqual(
            falaise_gap.name,
            "FALAISE GAP"
        )

        self.assertEqual(
            falaise_gap.track_number,
            0
        )

    def test_track_numbers_descend(self):
        expected_track_numbers = [
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0
        ]

        actual_track_numbers = [
            space.track_number
            for space in us_1_track
        ]

        self.assertEqual(
            actual_track_numbers,
            expected_track_numbers
        )

    def test_cherbourg_exists(self):
        cherbourg = us_1_track[4]

        self.assertEqual(
            cherbourg.name,
            "CHERBOURG"
        )

        self.assertEqual(
            cherbourg.terrain,
            TerrainType.TOWN
        )

    def test_german_controlled_spaces(self):
        german_spaces = [
            space
            for space in us_1_track
            if space.controlling_player == SideType.GERMAN
        ]

        self.assertEqual(
            len(german_spaces),
            10
        )

    def test_next_space_after_st_lo(self):
        current_space = 6

        space = us_1_track[current_space]

        self.assertEqual(
            space.name,
            "ST. LO"
        )

        current_space += 1

        space = us_1_track[current_space]

        self.assertEqual(
            space.name,
            "AVRANCHES"
        )

    def test_next_space_after_mortain(self):
        current_space = 8

        space = us_1_track[current_space]

        self.assertEqual(
            space.name,
            "MORTAIN"
        )

        current_space += 1

        space = us_1_track[current_space]

        self.assertEqual(
            space.name,
            "FLERS"
        )

    def test_all_spaces_start_empty(self):
        for space in us_1_track:
            self.assertEqual(
                len(space.units),
                0
            )