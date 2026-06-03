import unittest
from core.map.map_spaces_brit_2 import brit_2_track
from core.enums import SideType
from core.map.map_model import TerrainType


class TestBrit2Track(unittest.TestCase):
    def test_track_has_8_spaces(self):
        self.assertEqual(len(brit_2_track), 8)

    def test_start_box(self):
        start_box = brit_2_track[0]
        self.assertEqual(start_box.name, "2ND BRIT START BOX")
        self.assertEqual(start_box.terrain, TerrainType.START_BOX)
        self.assertEqual(start_box.controlling_player, SideType.ALLIED)

    def test_falaise_gap(self):
        falaise_gap = brit_2_track[-1]
        self.assertEqual(falaise_gap.name, "FALAISE GAP")
        self.assertEqual(falaise_gap.track_number, 0)

    def test_track_numbers_descend(self):
        expected_track_numbers = [7, 6, 5, 4, 3, 2, 1, 0]

        actual_track_numbers = [space.track_number for space in brit_2_track]

        self.assertEqual(actual_track_numbers, expected_track_numbers)

    def test_german_controlled_spaces(self):
        german_spaces = [space for space in brit_2_track if space.controlling_player == SideType.GERMAN]

        self.assertEqual(len(german_spaces), 6)

    def test_next_space_after_bayeux(self):
        current_space = 2
        space = brit_2_track[current_space]

        self.assertEqual(space.name, "BAYEUX")
        current_space += 1
        space = brit_2_track[current_space]
        self.assertEqual(space.name, "TILLY")

    def test_next_space_after_villers_bocage(self):
        current_space = 4
        space = brit_2_track[current_space]
        self.assertEqual(space.name, "VILLERS-BOCAGE")
        current_space += 1
        space = brit_2_track[current_space]
        self.assertEqual(space.name, "MONT PINCON")

