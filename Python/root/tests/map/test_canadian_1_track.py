import unittest
from core.map.map_spaces_can_1 import can_1_track
from core.enums import SideType
from core.map.map_model import TerrainType

class TestCan1Track(unittest.TestCase):
    def test_track_has_8_spaces(self):
        self.assertEqual(
            len(can_1_track),
            8
        )

    def test_start_box(self):
        start_box = can_1_track[0]
        self.assertEqual(
            start_box.name,
            "1ST CAN START BOX"
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
        falaise_gap = can_1_track[-1]
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
            for space in can_1_track
        ]

        self.assertEqual(
            actual_track_numbers,
            expected_track_numbers
        )

    def test_caen_is_fortified(self):
        caen = can_1_track[3]
        self.assertTrue(
            caen.fortified
        )

    def test_german_controlled_spaces(self):
        german_spaces = [
            space
            for space in can_1_track
            if space.controlling_player == SideType.GERMAN
        ]
        self.assertEqual(
            len(german_spaces),
            6
        )

    def test_next_space_after_caen(self):
        current_space = 3
        space = can_1_track[current_space]
        self.assertEqual(
            space.name, "CAEN"
        )
        current_space += 1

        space = can_1_track[current_space]
        self.assertEqual(
            space.name, "CAGNY"
        )