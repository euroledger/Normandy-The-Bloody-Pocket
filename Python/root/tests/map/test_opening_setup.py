# tests/test_opening_setup.py

import unittest

from core.allied_armies import *
from core.german_units import PZ_21
from core.global_game_state import *
from core.map.map_spaces_us_1 import us_1_start_box, carentan
from core.map.map_spaces_brit_2 import brit_2_start_box, bayeux
from core.map.map_spaces_can_1 import can_1_start_box, lebisey_wood
from core.map.map_spaces_us_3 import us_3_start_box
from core.map.map_utilities import do_opening_setup


class TestOpeningSetup(unittest.TestCase):

    # =========================================================
    # ALLIED SETUP
    # =========================================================
            
    @classmethod
    def setUpClass(cls):
        do_opening_setup()

    
    def test_us_first_army_setup(self):
        self.assertIn(
            US_FIRST_ARMY,
            us_1_start_box.units
        )

    def test_british_second_army_setup(self):
        self.assertIn(
            BRITISH_SECOND_ARMY,
            brit_2_start_box.units
        )

    def test_canadian_first_army_setup(self):
        self.assertIn(
            CANADIAN_FIRST_ARMY,
            can_1_start_box.units
        )

    def test_us_third_army_corps_setup(self):
        self.assertIn(
            US_VIII_CORPS,
            us_3_start_box.units
        )

        self.assertIn(
            US_XV_CORPS,
            us_3_start_box.units
        )

    # =========================================================
    # GERMAN SETUP
    # =========================================================

    def test_bayeux_setup(self):
        self.assertIn(
            PZ_21,
            bayeux.units
        )

        self.assertEqual(
            len(bayeux.units),
            4
        )

    def test_lebisey_wood_setup(self):
        self.assertEqual(
            len(lebisey_wood.units),
            3
        )

    def test_carentan_setup(self):
        self.assertEqual(
            len(carentan.units),
            1
        )

    # =========================================================
    # FRONT LINES
    # =========================================================

    def test_allied_front_lines(self):
        self.assertEqual(
            GlobalGameState.us_1_front_line,
            11
        )

        self.assertEqual(
            GlobalGameState.brit_2_front_line,
            7
        )

        self.assertEqual(
            GlobalGameState.can_1_front_line,
            7
        )
