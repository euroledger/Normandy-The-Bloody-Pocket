import unittest

from core.actions.resource_actions import (
    do_hitler_approval_augmentation_roll,
    do_supply_augmentation_roll,
    do_transport_augmentation_roll,
)
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    hitler_approval_track,
    supply_track,
    transport_track,
)
from core.map.map_utilities import do_opening_setup
from tests.core_mechanics.testing_utilities import reset_game_state_for_tests


class TestResourceAugmentationRoll(unittest.TestCase):
    def setUp(self):
        do_opening_setup()
        GlobalGameState.actions_left_this_turn = 1
        transport_track.value = GlobalGameState.transport_base_level
        supply_track.value = GlobalGameState.supply_base_level
        hitler_approval_track.value = GlobalGameState.hitler_approval_base_level

    def tearDown(self):
        reset_game_state_for_tests()

    def test_transport_augmentation_succeeds(self):
        do_transport_augmentation_roll(die_roll=4)

        self.assertEqual(transport_track.value, 4)

    def test_transport_augmentation_fails(self):
        do_transport_augmentation_roll(die_roll=3)

        self.assertEqual(transport_track.value, 3)

    def test_supply_augmentation_succeeds(self):
        do_supply_augmentation_roll(die_roll=4)

        self.assertEqual(supply_track.value, 4)

    def test_supply_augmentation_fails(self):
        do_supply_augmentation_roll(die_roll=3)

        self.assertEqual(supply_track.value, 3)

    def test_hitler_approval_augmentation_succeeds(self):
        do_hitler_approval_augmentation_roll(die_roll=4)

        self.assertEqual(hitler_approval_track.value, 4)

    def test_hitler_approval_augmentation_fails(self):
        do_hitler_approval_augmentation_roll(die_roll=3)

        self.assertEqual(hitler_approval_track.value, 3)


if __name__ == "__main__":
    unittest.main()
