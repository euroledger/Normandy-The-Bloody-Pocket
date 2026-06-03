import unittest
from cards.card_1 import card as card_001
from core.resources import do_resource_phase_reinforcements
from core.german_units import PZ_LEHR, SS_12
from core.map.map_model import in_transit_box, strategic_reserve_box


class TestReinforcements(unittest.TestCase):
    def setUp(self):
        in_transit_box.units.clear()
        strategic_reserve_box.units.clear()

    def test_card_1_reinforcements(self):
        do_resource_phase_reinforcements(card_001)
        self.assertEqual(len(in_transit_box.units), 2)
        self.assertIn(PZ_LEHR, in_transit_box.units)
        self.assertIn(SS_12, in_transit_box.units)
        self.assertEqual(len(strategic_reserve_box.units), 0)
