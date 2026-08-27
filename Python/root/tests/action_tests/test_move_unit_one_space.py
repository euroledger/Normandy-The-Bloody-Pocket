import unittest

from core.actions.move_unit_one_space_action import do_move_unit_one_space
from core.german_units import SS_12
from core.global_game_state import GlobalGameState
from core.map.map_spaces_us_1 import cherbourg, valognes, st_lo, coutances
from core.map.map_spaces_us_3 import argentan, falaise_gap
from core.map.map_spaces_can_1 import falaise
from core.map.map_utilities import do_opening_setup
from tests.core_mechanics.testing_utilities import reset_game_state_for_tests


class TestMoveUnitOneSpace(unittest.TestCase):

    def setUp(self):
        do_opening_setup()
        GlobalGameState.actions_left_this_turn = 1
        cherbourg.units.append(SS_12)

    def tearDown(self):
        reset_game_state_for_tests()

    def test_move_unit_one_space_succeeds(self):
        self.assertIn(SS_12, cherbourg.units)
        self.assertNotIn(SS_12, valognes.units)

        do_move_unit_one_space(
            unit_choice=SS_12,
            space_choice=valognes,
        )

        self.assertNotIn(SS_12, cherbourg.units)
        self.assertIn(SS_12, valognes.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 0)

    def test_move_unit_one_space_succeeds_to_other_adjacent_space(self):
        self.assertIn(SS_12, cherbourg.units)
        self.assertNotIn(SS_12, st_lo.units)

        do_move_unit_one_space(
            unit_choice=SS_12,
            space_choice=st_lo,
        )

        self.assertNotIn(SS_12, cherbourg.units)
        self.assertIn(SS_12, st_lo.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 0)


    def test_move_unit_one_space_does_not_move_to_non_adjacent_space(self):
        self.assertIn(SS_12, cherbourg.units)
        self.assertNotIn(SS_12, coutances.units)

        do_move_unit_one_space(
            unit_choice=SS_12,
            space_choice=coutances,
        )

        self.assertIn(SS_12, cherbourg.units)
        self.assertNotIn(SS_12, coutances.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 1)


    def test_move_unit_through_falaise_gap_to_another_track(self):
        cherbourg.units.remove(SS_12)
        argentan.units.append(SS_12)

        self.assertIn(SS_12, argentan.units)
        self.assertNotIn(SS_12, falaise_gap.units)
        self.assertNotIn(SS_12, falaise.units)

        do_move_unit_one_space(
            unit_choice=SS_12,
            space_choice=falaise_gap,
        )

        self.assertNotIn(SS_12, argentan.units)
        self.assertIn(SS_12, falaise_gap.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 0)

        GlobalGameState.actions_left_this_turn = 1

        do_move_unit_one_space(
            unit_choice=SS_12,
            space_choice=falaise,
        )

        self.assertNotIn(SS_12, falaise_gap.units)
        self.assertIn(SS_12, falaise.units)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 0)
        
if __name__ == "__main__":
    unittest.main()
