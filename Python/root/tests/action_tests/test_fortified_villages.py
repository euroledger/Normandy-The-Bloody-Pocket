import unittest

from core.actions.fortified_villages_action import do_build_fortified_villages
from core.global_game_state import GlobalGameState
from core.map.map_spaces_us_1 import mortain
from core.map.map_spaces_us_3 import le_mans
from core.map.map_utilities import do_opening_setup
from tests.core_mechanics.testing_utilities import reset_game_state_for_tests


class TestBuildFortifiedVillages(unittest.TestCase):
    def setUp(self):
        do_opening_setup()
        GlobalGameState.actions_left_this_turn = 3
        GlobalGameState.reserve_actions = 0

    def tearDown(self):
        reset_game_state_for_tests()

    def test_place_fortified_village(self):
        le_mans.fortified_village_modifier = 0

        do_build_fortified_villages(le_mans)
        
        self.assertEqual(le_mans.fortified_village_modifier, 1)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 0)
        self.assertEqual(GlobalGameState.reserve_actions, 0)

    def test_upgrade_fortified_village(self):
        mortain.fortified_village_modifier = 1

        do_build_fortified_villages(mortain)

        self.assertEqual(mortain.fortified_village_modifier, 2)
        self.assertEqual(GlobalGameState.actions_left_this_turn, 0)
        self.assertEqual(GlobalGameState.reserve_actions, 0)


if __name__ == "__main__":
    unittest.main()
