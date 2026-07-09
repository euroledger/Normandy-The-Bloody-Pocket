import unittest

from core.allied_armies import BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_FIRST_ARMY
from core.global_game_state import GlobalGameState
from core.map.map_utilities import (
    add_units_to_space,
    can_counter_attack,
    do_opening_setup,
    calculate_german_attack_strength,
    get_eligible_german_units,
)
from core.map.map_spaces_us_1 import carentan, utah_omaha
from core.map.map_spaces_brit_2 import bayeux, gold_juno_sword_brit
from core.map.map_spaces_can_1 import lebisey_wood, gold_juno_sword_can
from core.military import get_front_line_space
from core.actions import get_counter_attack_options
from cards.card_2 import card as card_002

from core.weather import WEATHER_TABLE


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
        units = get_eligible_german_units(carentan)
        self.assertEqual(calculate_german_attack_strength(carentan, units), 1)

    def test_bayeux_attack_strength(self):
        units = get_eligible_german_units(bayeux)
        self.assertEqual(calculate_german_attack_strength(bayeux, units), 4)

    def test_lebisey_wood_attack_strength(self):
        units = get_eligible_german_units(lebisey_wood)
        self.assertEqual(calculate_german_attack_strength(lebisey_wood, units), 2)

    def test_model_adds_one_to_carentan_attack_strength(self):
        carentan.model_modifier = 1
        units = get_eligible_german_units(carentan)
        self.assertEqual(calculate_german_attack_strength(carentan, units), 2)

    def test_us_1_beach_front_line_cannot_be_counter_attacked_after_card_2(self):
        add_units_to_space(utah_omaha, US_FIRST_ARMY)

        GlobalGameState.cards_drawn = 3

        front_line_space = get_front_line_space(US_FIRST_ARMY)
        army_space = US_FIRST_ARMY.location

        self.assertEqual(front_line_space, army_space)
        self.assertEqual(front_line_space, utah_omaha)
        self.assertFalse(can_counter_attack(front_line_space))

    def test_allied_army_in_space_does_not_affect_german_attack_strength(self):
        add_units_to_space(carentan, US_FIRST_ARMY)
        units = get_eligible_german_units(carentan)
        self.assertEqual(calculate_german_attack_strength(carentan, units), 1)

    def test_counter_attack_with_carentan_as_attacking_space(self):
        GlobalGameState.cards_drawn = 1
        GlobalGameState.us_1_front_line = utah_omaha.track_number
        add_units_to_space(utah_omaha, US_FIRST_ARMY)

        GlobalGameState.current_card = card_002
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        options = get_counter_attack_options()
        option = next(option for option in options if option["army"] == US_FIRST_ARMY)

        self.assertEqual(option["target_space"], utah_omaha)
        self.assertEqual(option["attacking_space"], carentan)
        self.assertEqual(option["german_attack"], 1)
        self.assertEqual(option["allied_defense"], 5)

    def test_counter_attack_with_bayeux_as_attacking_space(self):
        GlobalGameState.cards_drawn = 1
        GlobalGameState.brit_2_front_line = gold_juno_sword_brit.track_number
        add_units_to_space(gold_juno_sword_brit, BRITISH_SECOND_ARMY)

        GlobalGameState.current_card = card_002
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        options = get_counter_attack_options()
        option = next(option for option in options if option["army"] == BRITISH_SECOND_ARMY)

        self.assertEqual(option["target_space"], gold_juno_sword_brit)
        self.assertEqual(option["attacking_space"], bayeux)
        self.assertEqual(option["german_attack"], 4)
        self.assertEqual(option["allied_defense"], 4)

    def test_counter_attack_with_lebisey_wood_as_attacking_space(self):
        GlobalGameState.cards_drawn = 1
        GlobalGameState.can_1_front_line = gold_juno_sword_can.track_number

        GlobalGameState.current_card = card_002
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        add_units_to_space(gold_juno_sword_can, CANADIAN_FIRST_ARMY)

        options = get_counter_attack_options()
        option = next(option for option in options if option["army"] == CANADIAN_FIRST_ARMY)

        self.assertEqual(option["target_space"], gold_juno_sword_can)
        self.assertEqual(option["attacking_space"], lebisey_wood)
        self.assertEqual(option["german_attack"], 2)
        self.assertEqual(option["allied_defense"], 4)