import unittest

from core.map.map_utilities import do_opening_setup, german_defense_strength
from core.map.map_spaces_us_1 import carentan
from core.map.map_spaces_brit_2 import bayeux, tilly
from core.map.map_spaces_can_1 import lebisey_wood
from core.enums import ReinforcementType


class TestGermanUnits(unittest.TestCase):
    def setUp(self):
        carentan.units.clear()
        bayeux.units.clear()
        lebisey_wood.units.clear()

        carentan.model_modifier = 0
        bayeux.model_modifier = 0
        lebisey_wood.model_modifier = 0
        tilly.model_modifier = 0

        do_opening_setup()

    def test_carentan(self):
        self.assertEqual(len(carentan.units), 1)
        self.assertEqual(carentan.units[0].type, ReinforcementType.NEBELWERFER)
        self.assertEqual(carentan.units[0].combat_value, 1)
        self.assertEqual(german_defense_strength(carentan), 3)

    def test_bayeux(self):
        self.assertEqual(len(bayeux.units), 4)
        self.assertEqual(german_defense_strength(bayeux), 7)

    def test_lebisey_wood(self):
        self.assertEqual(len(lebisey_wood.units), 3)
        self.assertEqual(german_defense_strength(lebisey_wood), 6)

    def test_tilly(self):
        self.assertEqual(len(tilly.units), 0)
        self.assertEqual(german_defense_strength(tilly), 2)

    def test_model_adds_one_to_german_defense(self):
        carentan.model_modifier = 1
        self.assertEqual(german_defense_strength(carentan), 4)
        carentan.model_modifier = 0