import unittest
from cards.card_13 import card as card_013
from core.card_utilities import calculate_defense_modifiers, get_all_defending_armies
from core.map.map_spaces_us_1 import cherbourg
from core.map.map_spaces_brit_2 import tilly
from core.map.map_spaces_can_1 import caen, lebisey_wood
from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY
from core.map.map_utilities import reset_allied_armies
from core.weather import WEATHER_TABLE


class TestDefenseStrengthsCard13(unittest.TestCase):
    def setUp(self):
        self.weather = WEATHER_TABLE[1]
        reset_allied_armies()

    def test_us_first_army_in_cherbourg(self):
        US_FIRST_ARMY.location = cherbourg
        result = calculate_defense_modifiers(card=card_013, army=US_FIRST_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 4)

    def test_british_second_army_in_tilly(self):
        BRITISH_SECOND_ARMY.location = tilly
        result = calculate_defense_modifiers(card=card_013, army=BRITISH_SECOND_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 4)

    def test_upgraded_british_second_army_in_tilly(self):
        BRITISH_SECOND_ARMY.location = tilly
        BRITISH_SECOND_ARMY.flip()
        result = calculate_defense_modifiers(card=card_013, army=BRITISH_SECOND_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 6)
        BRITISH_SECOND_ARMY.flip()

    def test_canadian_first_army_in_caen(self):
        CANADIAN_FIRST_ARMY.location = lebisey_wood
        result = calculate_defense_modifiers(card=card_013, army=CANADIAN_FIRST_ARMY, weather=self.weather)
        self.assertEqual(result["defense_strength"], 4)

    # Armies in Fortresses (eg Caen) cannot be attacked
    def test_canadian_first_army_in_caen_not_defending(self):
        CANADIAN_FIRST_ARMY.location = caen
        armies = get_all_defending_armies()
        self.assertNotIn(CANADIAN_FIRST_ARMY, armies)
