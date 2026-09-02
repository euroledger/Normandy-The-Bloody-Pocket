import unittest

from core.allied_advances_phase import enforce_german_stacking_limit
from core.enums import ReinforcementType
from core.german_units import PZ_LEHR, SS_12, SS_1, SS_9, SS_10, FS_3, FS_5, create_flak88, create_nebelwerfer
from core.map.map_model import eliminated_units_box
from core.map.map_spaces_us_1 import flers
from core.map.map_utilities import reset_map, add_units_to_space


class TestGermanRetreats(unittest.TestCase):

    def setUp(self):
        reset_map()

    def tearDown(self):
        reset_map()

    def test_panzer_excess_unit_is_eliminated(self):
        add_units_to_space(flers, [PZ_LEHR, SS_12, SS_1, SS_9, SS_10])

        enforce_german_stacking_limit(flers, choice=1)

        self.assertEqual(sum(1 for unit in flers.units if unit.is_panzer()), 4)
        self.assertIn(PZ_LEHR, eliminated_units_box.units)

    def test_flak_excess_unit_is_eliminated(self):
        flak_1 = create_flak88()
        flak_2 = create_flak88()
        flak_3 = create_flak88()
        flak_4 = create_flak88()

        add_units_to_space(flers, [flak_1, flak_2, flak_3, flak_4])

        enforce_german_stacking_limit(flers, choice=1)

        self.assertEqual(sum(1 for unit in flers.units if unit.type == ReinforcementType.FLAK_88), 3)
        self.assertIn(flak_1, eliminated_units_box.units)

    def test_nebelwerfer_excess_unit_is_eliminated(self):
        nebelwerfer_1 = create_nebelwerfer()
        nebelwerfer_2 = create_nebelwerfer()
        nebelwerfer_3 = create_nebelwerfer()
        nebelwerfer_4 = create_nebelwerfer()

        add_units_to_space(flers, [nebelwerfer_1, nebelwerfer_2, nebelwerfer_3, nebelwerfer_4])

        enforce_german_stacking_limit(flers)

        self.assertEqual(sum(1 for unit in flers.units if unit.type == ReinforcementType.NEBELWERFER), 3)
        self.assertIn(nebelwerfer_4, eliminated_units_box.units)

    def test_no_excess_units_are_eliminated(self):
        add_units_to_space(flers, [PZ_LEHR, SS_12, SS_1, SS_9])

        enforce_german_stacking_limit(flers, choice=1)

        self.assertEqual(sum(1 for unit in flers.units if unit.is_panzer()), 4)
        self.assertEqual(len(eliminated_units_box.units), 0)
