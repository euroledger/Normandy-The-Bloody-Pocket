# tests/test_resource_check.py

import unittest

from core.map.map_model import (
    transport_track,
    supply_track,
    hitler_approval_track
)
from core.resources import do_resource_roll


class TestResources(unittest.TestCase):

    def setUp(self):
        transport_track.value = 5
        supply_track.value = 4
        hitler_approval_track.value = 6

    # =========================================================
    # TRANSPORT
    # =========================================================

    def test_transport_increases_when_roll_higher_than_base(self):
        do_resource_roll(
            track=transport_track,
            die_roll=4
        )

        self.assertEqual(
            transport_track.value,
            6
        )

    def test_transport_does_not_increase_when_roll_equals_base(self):
        do_resource_roll(
            track=transport_track,
            die_roll=3
        )

        self.assertEqual(
            transport_track.value,
            5
        )

    def test_transport_does_not_increase_when_roll_lower_than_base(self):
        do_resource_roll(
            track=transport_track,
            die_roll=2
        )

        self.assertEqual(
            transport_track.value,
            5
        )

    def test_transport_increases_with_drm(self):
        transport_track.value = 4

        do_resource_roll(
            track=transport_track,
            die_roll=3,
            drm=1
        )

        self.assertEqual(
            transport_track.value,
            5
        )

    def test_transport_cannot_exceed_maximum(self):
        do_resource_roll(
            track=transport_track,
            die_roll=6
        )

        self.assertEqual(
            transport_track.value,
            6
        )

    # =========================================================
    # SUPPLY
    # =========================================================

    def test_supply_increases_when_roll_higher_than_base(self):
        do_resource_roll(
            track=supply_track,
            die_roll=4
        )

        self.assertEqual(
            supply_track.value,
            5
        )

    def test_supply_does_not_increase_when_roll_equals_base(self):
        do_resource_roll(
            track=supply_track,
            die_roll=3
        )

        self.assertEqual(
            supply_track.value,
            4
        )

    def test_supply_does_not_increase_when_roll_lower_than_base(self):
        do_resource_roll(
            track=supply_track,
            die_roll=2
        )

        self.assertEqual(
            supply_track.value,
            4
        )

    def test_supply_increases_with_drm(self):
        do_resource_roll(
            track=supply_track,
            die_roll=3,
            drm=1
        )

        self.assertEqual(
            supply_track.value,
            5
        )

    def test_supply_cannot_exceed_maximum(self):
        supply_track.value = 6

        do_resource_roll(
            track=supply_track,
            die_roll=6
        )

        self.assertEqual(
            supply_track.value,
            6
        )

    # =========================================================
    # HITLER APPROVAL
    # =========================================================

    def test_hitler_approval_does_not_increase_when_at_maximum(self):
        do_resource_roll(
            track=hitler_approval_track,
            die_roll=6
        )

        self.assertEqual(
            hitler_approval_track.value,
            6
        )

    def test_hitler_approval_does_not_increase_when_roll_equals_base(self):
        do_resource_roll(
            track=hitler_approval_track,
            die_roll=3
        )

        self.assertEqual(
            hitler_approval_track.value,
            6
        )

    def test_hitler_approval_does_not_increase_when_roll_lower_than_base(self):
        do_resource_roll(
            track=hitler_approval_track,
            die_roll=2
        )

        self.assertEqual(
            hitler_approval_track.value,
            6
        )