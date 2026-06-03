import unittest
from cards.card_17 import card as card_017
from core.enums import ReinforcementType
from core.resources import do_resource_phase_reinforcements
from core.map.map_model import in_transit_box, strategic_reserve_box


class TestReinforcements(unittest.TestCase):
    def setUp(self):
        in_transit_box.units.clear()
        strategic_reserve_box.units.clear()


def test_card_17_reinforcements(self):
    do_resource_phase_reinforcements(card_017)

    self.assertEqual(len(in_transit_box.units), 0)
    self.assertEqual(len(strategic_reserve_box.units), 3)
    self.assertEqual(strategic_reserve_box.units[0].type, ReinforcementType.NEBELWERFER)
    self.assertEqual(strategic_reserve_box.units[1].type, ReinforcementType.NEBELWERFER)
    self.assertEqual(strategic_reserve_box.units[2].type, ReinforcementType.NEBELWERFER)
