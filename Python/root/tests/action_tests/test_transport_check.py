import unittest

from core.actions import do_panzer_transport_check
from core.global_game_state import GlobalGameState
from core.german_units import PZ_LEHR
from core.map.map_model import (
    transport_track,
    in_transit_box,
    strategic_reserve_box,
)


class TestPanzerTransportCheck(unittest.TestCase):
    def setUp(self):
        in_transit_box.units.clear()
        strategic_reserve_box.units.clear()

        transport_track.value = 5
        GlobalGameState.transport_check_drm = 0

    def tearDown(self):
        in_transit_box.units.clear()
        strategic_reserve_box.units.clear()

        transport_track.value = 5
        GlobalGameState.transport_check_drm = 0

    def test_panzer_moves_to_strategic_reserve_on_successful_check(self):
        in_transit_box.units.append(PZ_LEHR)

        result = do_panzer_transport_check(
            unit=PZ_LEHR,
            die_roll=5,
        )

        self.assertTrue(result)
        self.assertNotIn(PZ_LEHR, in_transit_box.units)
        self.assertIn(PZ_LEHR, strategic_reserve_box.units)

    def test_panzer_remains_in_transit_on_failed_check(self):
        in_transit_box.units.append(PZ_LEHR)

        result = do_panzer_transport_check(
            unit=PZ_LEHR,
            die_roll=6,
        )

        self.assertFalse(result)
        self.assertIn(PZ_LEHR, in_transit_box.units)
        self.assertNotIn(PZ_LEHR, strategic_reserve_box.units)

    def test_positive_transport_check_drm_can_cause_failure(self):
        in_transit_box.units.append(PZ_LEHR)
        GlobalGameState.transport_check_drm = 1

        result = do_panzer_transport_check(
            unit=PZ_LEHR,
            die_roll=5,
        )

        self.assertFalse(result)
        self.assertIn(PZ_LEHR, in_transit_box.units)
        self.assertNotIn(PZ_LEHR, strategic_reserve_box.units)

    def test_negative_transport_check_drm_can_cause_success(self):
        in_transit_box.units.append(PZ_LEHR)
        GlobalGameState.transport_check_drm = -1

        result = do_panzer_transport_check(
            unit=PZ_LEHR,
            die_roll=6,
        )

        self.assertTrue(result)
        self.assertNotIn(PZ_LEHR, in_transit_box.units)
        self.assertIn(PZ_LEHR, strategic_reserve_box.units)

    def test_success_uses_modified_roll_against_transport_track(self):
        in_transit_box.units.append(PZ_LEHR)

        transport_track.value = 3
        GlobalGameState.transport_check_drm = -2

        result = do_panzer_transport_check(
            unit=PZ_LEHR,
            die_roll=5,
        )

        self.assertTrue(result)
        self.assertNotIn(PZ_LEHR, in_transit_box.units)
        self.assertIn(PZ_LEHR, strategic_reserve_box.units)