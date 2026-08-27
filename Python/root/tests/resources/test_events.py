import unittest

from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY
from core.global_game_state import GlobalGameState
from core.map.map_utilities import reset_map
from core.resources import do_event
from cards.card_28 import card as card_028
from cards.card_5 import card as card_005
from cards.card_26 import card as card_026
from core.actions.actions_helper import get_unit_location
from core.german_units import MEYER, SS_12
from core.map.map_model import in_transit_box, strategic_reserve_box, eliminated_units_box
from core.map.map_spaces_us_1 import cherbourg
from core.map.map_spaces_can_1 import caen
from cards.card_27 import card as card_027


class TestEvents(unittest.TestCase):

    def setUp(self):
        US_FIRST_ARMY.flipped = False
        BRITISH_SECOND_ARMY.flipped = False
        CANADIAN_FIRST_ARMY.flipped = False
        reset_map()

    def tearDown(self):
        US_FIRST_ARMY.flipped = False
        BRITISH_SECOND_ARMY.flipped = False
        CANADIAN_FIRST_ARMY.flipped = False

    def test_card_28_flips_three_allied_armies(self):
        do_event(card_028)

        self.assertTrue(US_FIRST_ARMY.flipped)
        self.assertTrue(BRITISH_SECOND_ARMY.flipped)
        self.assertTrue(CANADIAN_FIRST_ARMY.flipped)
        
    def test_get_unit_location_on_map(self):
        cherbourg.units.append(SS_12)
        self.assertEqual(get_unit_location(SS_12), cherbourg)
        cherbourg.units.remove(SS_12)

    def test_get_unit_location_in_strategic_reserve(self):
        strategic_reserve_box.units.append(SS_12)
        self.assertEqual(get_unit_location(SS_12), strategic_reserve_box)
        strategic_reserve_box.units.remove(SS_12)

    def test_get_unit_location_in_eliminated_box(self):
        eliminated_units_box.units.append(SS_12)
        self.assertEqual(get_unit_location(SS_12), eliminated_units_box)
        eliminated_units_box.units.remove(SS_12)

    def test_get_unit_location_in_transit(self):
        in_transit_box.units.append(SS_12)
        self.assertEqual(get_unit_location(SS_12), in_transit_box)
        in_transit_box.units.remove(SS_12)

    def test_get_unit_location_returns_none_when_not_present(self):
        self.assertIsNone(get_unit_location(SS_12))
        
    def test_card_5_places_meyer_with_12ss_on_map(self):
        caen.units.append(SS_12)
        do_event(card_005)
        self.assertIn(SS_12, caen.units)
        self.assertIn(MEYER, caen.units)
        self.assertTrue(GlobalGameState.meyer_available)

    def test_card_5_meyer_waits_when_12ss_in_strategic_reserve(self):
        strategic_reserve_box.units.append(SS_12)
        do_event(card_005)
        self.assertIn(SS_12, strategic_reserve_box.units)
        self.assertNotIn(MEYER, strategic_reserve_box.units)
        self.assertFalse(any(MEYER in space.units for space in [caen]))
        self.assertTrue(GlobalGameState.meyer_available)

    def test_card_5_has_no_effect_if_12ss_eliminated(self):
        eliminated_units_box.units.append(SS_12)
        do_event(card_005)
        self.assertIn(SS_12, eliminated_units_box.units)
        self.assertNotIn(MEYER, eliminated_units_box.units)
        self.assertFalse(GlobalGameState.meyer_available)
        

    def test_card_26_sets_bocage_defense_modifier(self):
        GlobalGameState.bocage_defense_modifier = 0
        do_event(card_026)
        self.assertEqual(GlobalGameState.bocage_defense_modifier, -1)
        

    def test_card_27_sets_hitler_approval_base_level(self):
        GlobalGameState.hitler_approval_base_level = 3
        do_event(card_027)
        self.assertEqual(GlobalGameState.hitler_approval_base_level, 4)



