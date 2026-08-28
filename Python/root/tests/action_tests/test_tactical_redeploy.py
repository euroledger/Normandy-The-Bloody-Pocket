import unittest

from core.actions.actions_helper import get_german_units_on_map
from core.german_units import create_flak88, create_kampfgruppe, create_nebelwerfer
from core.map.map_model import eliminated_units_box, in_transit_box, strategic_reserve_box
from core.map.map_spaces_brit_2 import mont_pincon
from core.map.map_spaces_can_1 import caen, cagny
from core.map.map_spaces_us_1 import mortain
from core.map.map_spaces_us_3 import brest, le_mans
from core.map.map_utilities import add_units_to_space, reset_map


class TestTacticalRedeploy(unittest.TestCase):

    def setUp(self):
        reset_map()
        self.original_units = [(mortain, list(mortain.units)), (mont_pincon, list(mont_pincon.units)), (caen, list(caen.units)), (cagny, list(cagny.units)), (brest, list(brest.units)), (le_mans, list(
            le_mans.units)), (in_transit_box, list(in_transit_box.units)), (strategic_reserve_box, list(strategic_reserve_box.units)), (eliminated_units_box, list(eliminated_units_box.units))]
        in_transit_box.units.clear()
        strategic_reserve_box.units.clear()
        eliminated_units_box.units.clear()

    def tearDown(self):
        for space, units in self.original_units:
            space.units.clear()
            space.units.extend(units)

    def test_german_unit_on_map_is_available(self):
        unit = create_kampfgruppe()
        add_units_to_space(mortain, unit)
        available = get_german_units_on_map()
        available_units = [unit for space, unit in available]
        self.assertIn(unit, available_units)

    def test_unit_in_transit_is_not_available(self):
        unit = create_kampfgruppe()
        in_transit_box.units.append(unit)
        available = get_german_units_on_map()
        available_units = [unit for space, unit in available]
        self.assertNotIn(unit, available_units)

    def test_unit_in_strategic_reserve_is_not_available(self):
        unit = create_kampfgruppe()
        strategic_reserve_box.units.append(unit)
        available = get_german_units_on_map()
        available_units = [unit for space, unit in available]
        self.assertNotIn(unit, available_units)

    def test_unit_in_eliminated_box_is_not_available(self):
        unit = create_kampfgruppe()
        eliminated_units_box.units.append(unit)
        available = get_german_units_on_map()
        available_units = [unit for space, unit in available]
        self.assertNotIn(unit, available_units)

    def test_german_unit_under_siege_is_not_available(self):
        unit = create_kampfgruppe()
        add_units_to_space(mortain, unit)
        mortain.under_siege = True
        available = get_german_units_on_map()
        available_units = [unit for space, unit in available]
        self.assertNotIn(unit, available_units)

    def test_multiple_german_units_on_map_are_available(self):
        unit_1 = create_kampfgruppe()
        unit_2 = create_flak88()
        unit_3 = create_nebelwerfer()
        add_units_to_space(mortain, unit_1)
        add_units_to_space(mont_pincon, unit_2)
        add_units_to_space(brest, unit_3)
        available = get_german_units_on_map()
        available_units = [unit for space, unit in available]
        self.assertIn(unit_1, available_units)
        self.assertIn(unit_2, available_units)
        self.assertIn(unit_3, available_units)


if __name__ == "__main__":
    unittest.main()
