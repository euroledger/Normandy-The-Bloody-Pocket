import unittest

from core.actions.strategic_reserve_actions import (
    do_move_other_unit_from_strategic_reserve,
    get_german_controlled_spaces,
)
from core.enums import ReinforcementType
from core.german_units import create_flak88, create_kampfgruppe
from core.global_game_state import GlobalGameState
from core.map.map_model import strategic_reserve_box
from core.map.map_utilities import do_opening_setup
from tests.core_mechanics.testing_utilities import reset_game_state_for_tests


class TestMoveOtherUnitFromStrategicReserve(unittest.TestCase):
    def setUp(self):
        do_opening_setup()
        GlobalGameState.actions_left_this_turn = 1

        self.flak_1 = create_flak88()
        self.flak_2 = create_flak88()
        self.flak_3 = create_flak88()
        self.kampfgruppe = create_kampfgruppe()

        strategic_reserve_box.units.append(self.flak_1)
        strategic_reserve_box.units.append(self.flak_2)
        strategic_reserve_box.units.append(self.flak_3)
        strategic_reserve_box.units.append(self.kampfgruppe)

    def tearDown(self):
        reset_game_state_for_tests()

    def test_move_succeeds(self):
        destination = get_german_controlled_spaces()[0]

        self.assertEqual(
            sum(unit.type == ReinforcementType.FLAK_88 for unit in strategic_reserve_box.units),
            3,
        )
        self.assertNotIn(self.flak_1, destination.units)

        do_move_other_unit_from_strategic_reserve(
            unit_choice=1,
            space_choice=1,
        )

        # self.assertNotIn(self.flak_1, strategic_reserve_box.units)
        self.assertIn(self.flak_1, destination.units)
        self.assertEqual(
            sum(unit.type == ReinforcementType.FLAK_88 for unit in strategic_reserve_box.units),
            2,
        )
        self.assertEqual(GlobalGameState.actions_left_this_turn, 1)

    def test_invalid_unit_choice_does_nothing(self):
        destination = get_german_controlled_spaces()[0]

        self.assertIn(self.flak_1, strategic_reserve_box.units)
        self.assertNotIn(self.flak_1, destination.units)

        do_move_other_unit_from_strategic_reserve(
            unit_choice=99,
            space_choice=1,
        )

        self.assertIn(self.flak_1, strategic_reserve_box.units)
        self.assertNotIn(self.flak_1, destination.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 1)

    def test_invalid_destination_choice_does_nothing(self):
        destination = get_german_controlled_spaces()[0]

        self.assertIn(self.flak_1, strategic_reserve_box.units)
        self.assertNotIn(self.flak_1, destination.units)

        do_move_other_unit_from_strategic_reserve(
            unit_choice=1,
            space_choice=99,
        )

        self.assertIn(self.flak_1, strategic_reserve_box.units)
        self.assertNotIn(self.flak_1, destination.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 1)


if __name__ == "__main__":
    unittest.main()
