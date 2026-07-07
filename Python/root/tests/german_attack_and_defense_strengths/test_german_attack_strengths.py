import unittest

from core.allied_armies import US_FIRST_ARMY
from core.global_game_state import GlobalGameState
from core.map.map_utilities import add_units_to_space, can_counter_attack, do_opening_setup, german_attack_strength
from core.map.map_spaces_us_1 import carentan, utah_omaha
from core.map.map_spaces_brit_2 import bayeux
from core.map.map_spaces_can_1 import lebisey_wood
from core.military import get_front_line_space


class TestGermanAttackStrengths(unittest.TestCase):

    def setUp(self):
        carentan.units.clear()
        bayeux.units.clear()
        lebisey_wood.units.clear()

        carentan.model_modifier = 0
        bayeux.model_modifier = 0
        lebisey_wood.model_modifier = 0

        do_opening_setup()

    def tearDown(self):
        GlobalGameState.cards_drawn = 0
        GlobalGameState.us_1_front_line = 11
        do_opening_setup()

    def test_carentan_attack_strength(self):
        self.assertEqual(german_attack_strength(carentan), 1)

    def test_bayeux_attack_strength(self):
        self.assertEqual(german_attack_strength(bayeux), 4)

    def test_lebisey_wood_attack_strength(self):
        self.assertEqual(german_attack_strength(lebisey_wood), 2)

    def test_model_adds_one_to_carentan_attack_strength(self):
        carentan.model_modifier = 1
        self.assertEqual(german_attack_strength(carentan), 2)

    def test_us_1_beach_front_line_cannot_be_counter_attacked_after_card_2(self):
        add_units_to_space(utah_omaha, US_FIRST_ARMY)

        GlobalGameState.cards_drawn = 3
        GlobalGameState.us_1_front_line = 10

        front_line_space = get_front_line_space(US_FIRST_ARMY)
        army_space = US_FIRST_ARMY.location
        self.assertEqual(front_line_space, army_space)

        self.assertEqual(front_line_space, utah_omaha)
        self.assertFalse(can_counter_attack(front_line_space))

