import unittest

from cards.card_12 import card as card_012
from cards.card_36 import card as card_036
from cards.card_27 import card as card_027
from core.map.map_model import (
    hitler_approval_track,
    supply_track,
    transport_track,
)
from core.resources import do_resource_phase_adjustments


class TestResourcePhaseAdjustments(unittest.TestCase):
    def setUp(self):
        transport_track.value = 5
        supply_track.value = 4
        hitler_approval_track.value = 6

    def test_card_12_resource_adjustments(self):
        do_resource_phase_adjustments(card_012)

        self.assertEqual(transport_track.value, 5)
        self.assertEqual(supply_track.value, 3)
        self.assertEqual(hitler_approval_track.value, 4)

    def test_card_36_resource_adjustments(self):
        do_resource_phase_adjustments(card_036)

        self.assertEqual(transport_track.value, 5)
        self.assertEqual(supply_track.value, 6)
        self.assertEqual(hitler_approval_track.value, 6)


    def test_hitler_approval_does_not_exceed_maximum(self):
        transport_track.value = 5
        supply_track.value = 4
        hitler_approval_track.value = 6

        do_resource_phase_adjustments(card_036)

        self.assertEqual(transport_track.value, 5)
        self.assertEqual(supply_track.value, 6)
        self.assertEqual(hitler_approval_track.value, 6)


    def test_supply_does_not_exceed_maximum(self):
        transport_track.value = 5
        supply_track.value = 5
        hitler_approval_track.value = 5

        do_resource_phase_adjustments(card_036)

        self.assertEqual(transport_track.value, 5)
        self.assertEqual(supply_track.value, 6)
        self.assertEqual(hitler_approval_track.value, 6)


    def test_supply_does_not_go_below_zero(self):
        transport_track.value = 5
        supply_track.value = 0
        hitler_approval_track.value = 6

        do_resource_phase_adjustments(card_012)

        self.assertEqual(transport_track.value, 5)
        self.assertEqual(supply_track.value, 0)
        self.assertEqual(hitler_approval_track.value, 4)


    def test_hitler_approval_does_not_go_below_minimum(self):
        transport_track.value = 5
        supply_track.value = 4
        hitler_approval_track.value = -2

        do_resource_phase_adjustments(card_012)

        self.assertEqual(transport_track.value, 5)
        self.assertEqual(supply_track.value, 3)
        self.assertEqual(hitler_approval_track.value, -2)
        

    def test_card_27_reduces_hitler_approval_by_3(self):
        hitler_approval_track.value = 4
        do_resource_phase_adjustments(card_027)
        self.assertEqual(hitler_approval_track.value, 1)
