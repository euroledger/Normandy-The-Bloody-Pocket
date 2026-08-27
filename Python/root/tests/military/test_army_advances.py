import unittest
from core.global_game_state import GlobalGameState
from core.map.map_utilities import do_opening_setup
from core.allied_advances_phase import advance_army_one_space, do_allied_advances_phase
from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_VIII_CORPS, US_XV_CORPS
from core.map.map_spaces_us_1 import utah_omaha, carentan
from core.map.map_spaces_brit_2 import gold_juno_sword_brit, bayeux
from core.map.map_spaces_can_1 import gold_juno_sword_can, lebisey_wood
from core.map.map_spaces_us_3 import us_3_start_box, rennes
from core.tables.weather import get_weather_result
from cards.card_29 import card as card_029



class TestArmyMovement(unittest.TestCase):
    def setUp(self):
        do_opening_setup()

    def test_us_1_army_advances_to_beach(self):
        advance_army_one_space(US_FIRST_ARMY)

        self.assertEqual(US_FIRST_ARMY.location, utah_omaha)

    def test_us_1_army_advances_to_carentan(self):
        advance_army_one_space(US_FIRST_ARMY)
        advance_army_one_space(US_FIRST_ARMY)

        self.assertEqual(US_FIRST_ARMY.location, carentan)

    def test_brit_2_army_advances_to_beach(self):
        advance_army_one_space(BRITISH_SECOND_ARMY)

        self.assertEqual(BRITISH_SECOND_ARMY.location, gold_juno_sword_brit)

    def test_brit_2_army_advances_to_bayeux(self):
        advance_army_one_space(BRITISH_SECOND_ARMY)
        advance_army_one_space(BRITISH_SECOND_ARMY)

        self.assertEqual(BRITISH_SECOND_ARMY.location, bayeux)

    def test_can_1_army_advances_to_beach(self):
        advance_army_one_space(CANADIAN_FIRST_ARMY)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, gold_juno_sword_can)

    def test_can_1_army_advances_to_lebisey_wood(self):
        advance_army_one_space(CANADIAN_FIRST_ARMY)
        advance_army_one_space(CANADIAN_FIRST_ARMY)

        self.assertEqual(CANADIAN_FIRST_ARMY.location, lebisey_wood)
                

    def test_us_third_army_does_not_advance_before_activation(self):
        GlobalGameState.us_third_army_activated = False
        weather = get_weather_result(4)
        do_allied_advances_phase(card_029, weather)
        self.assertFalse(GlobalGameState.us_third_army_activated)
        self.assertIsNone(US_VIII_CORPS.location)
        self.assertIsNone(US_XV_CORPS.location)
