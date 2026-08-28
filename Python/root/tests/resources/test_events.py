import unittest

from core.allied_armies import US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_THIRD_ARMY, US_XV_CORPS
from core.global_game_state import GlobalGameState
from core.map.map_utilities import add_units_to_space, reset_map
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
from cards.card_42 import card as card_042
from core.map.map_spaces_us_3 import us_viii_track, us_xv_track


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

    # =========================================================
    # CARD #42 - BRADLEY HALT ORDER
    # =========================================================

    def test_card_42_retreats_third_army_from_le_mans(self):
        le_mans = next(space for space in us_viii_track if space.name == "LE MANS")
        retreat_space = next(space for space in us_viii_track if space.track_number == le_mans.track_number + 1)

        add_units_to_space(le_mans, US_THIRD_ARMY)
        do_event(card_042)

        self.assertEqual(US_THIRD_ARMY.location, retreat_space)
        self.assertIn(US_THIRD_ARMY, retreat_space.units)
        self.assertNotIn(US_THIRD_ARMY, le_mans.units)

    def test_card_42_retreats_xv_corps_from_le_mans(self):
        le_mans = next(space for space in us_xv_track if space.name == "LE MANS")
        retreat_space = next(space for space in us_xv_track if space.track_number == le_mans.track_number + 1)

        add_units_to_space(le_mans, US_XV_CORPS)
        do_event(card_042)

        self.assertEqual(US_XV_CORPS.location, retreat_space)
        self.assertIn(US_XV_CORPS, retreat_space.units)
        self.assertNotIn(US_XV_CORPS, le_mans.units)

    def test_card_42_has_no_effect_before_le_mans(self):
        le_mans_track_number = next(space.track_number for space in us_viii_track if space.name == "LE MANS")
        before_le_mans = next(space for space in us_viii_track if space.track_number > le_mans_track_number)

        add_units_to_space(before_le_mans, US_THIRD_ARMY)
        do_event(card_042)

        self.assertEqual(US_THIRD_ARMY.location, before_le_mans)
        self.assertIn(US_THIRD_ARMY, before_le_mans.units)

    def test_card_42_retreats_third_army_beyond_le_mans(self):
        le_mans_track_number = next(space.track_number for space in us_viii_track if space.name == "LE MANS")
        beyond_le_mans = next(space for space in us_viii_track if space.track_number < le_mans_track_number)
        retreat_space = next(space for space in us_viii_track if space.track_number == beyond_le_mans.track_number + 1)

        add_units_to_space(beyond_le_mans, US_THIRD_ARMY)
        do_event(card_042)

        self.assertEqual(US_THIRD_ARMY.location, retreat_space)
        self.assertIn(US_THIRD_ARMY, retreat_space.units)
        self.assertNotIn(US_THIRD_ARMY, beyond_le_mans.units)

    def test_card_42_retreats_xv_corps_beyond_le_mans(self):
        le_mans_track_number = next(space.track_number for space in us_xv_track if space.name == "LE MANS")
        beyond_le_mans = next(space for space in us_xv_track if space.track_number < le_mans_track_number)
        retreat_space = next(space for space in us_xv_track if space.track_number == beyond_le_mans.track_number + 1)

        add_units_to_space(beyond_le_mans, US_XV_CORPS)
        do_event(card_042)

        self.assertEqual(US_XV_CORPS.location, retreat_space)
        self.assertIn(US_XV_CORPS, retreat_space.units)
        self.assertNotIn(US_XV_CORPS, beyond_le_mans.units)

    def test_card_42_xv_corps_takes_priority_over_third_army(self):
        xv_le_mans = next(space for space in us_xv_track if space.name == "LE MANS")
        xv_retreat_space = next(space for space in us_xv_track if space.track_number == xv_le_mans.track_number + 1)

        third_le_mans = next(space for space in us_viii_track if space.name == "LE MANS")

        add_units_to_space(xv_le_mans, US_XV_CORPS)
        add_units_to_space(third_le_mans, US_THIRD_ARMY)

        do_event(card_042)

        self.assertEqual(US_XV_CORPS.location, xv_retreat_space)
        self.assertIn(US_XV_CORPS, xv_retreat_space.units)
        self.assertEqual(US_THIRD_ARMY.location, third_le_mans)
        self.assertIn(US_THIRD_ARMY, third_le_mans.units)
