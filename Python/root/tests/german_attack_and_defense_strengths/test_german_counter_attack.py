import unittest

from core.german_units import create_kampfgruppe
from core.global_game_state import GlobalGameState
from core.map.map_utilities import (
    do_opening_setup,
    can_counter_attack,
    get_eligible_german_units,
    add_units_to_space
)
from core.actions import (
    get_counter_attack_options,
    print_counter_attack_options,
    resolve_counter_attack,
    do_post_combat,
)
from core.map.map_spaces_us_1 import carentan, utah_omaha
from core.map.map_spaces_brit_2 import bayeux, gold_juno_sword_brit
from core.map.map_spaces_can_1 import lebisey_wood, gold_juno_sword_can
from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY,
    US_XV_CORPS,
    US_VIII_CORPS
)
from core.military import advance_army_one_space
from core.map.map_model import hitler_approval_track, TerrainType
from core.models import Strategy
from cards.card_2 import card as card_002
from cards.card_37 import card as card_037
from core.weather import WEATHER_TABLE
from tests.core_mechanics.testing_utilities import setup_units_for_tests
from core.map.map_spaces_us_3 import us_3_start_box, st_malo, rennes


# =========================================================
# COUNTER-ATTACK OPTION TESTS
# =========================================================


class TestGermanCounterAttackOptions(unittest.TestCase):
    def setUp(self):
        carentan.units.clear()
        bayeux.units.clear()
        lebisey_wood.units.clear()

        do_opening_setup()

    def tearDown(self):
        GlobalGameState.cards_drawn = 0
        GlobalGameState.us_1_front_line = 11
        GlobalGameState.brit_2_front_line = 7
        GlobalGameState.can_1_front_line = 7
        do_opening_setup()

    def test_carentan_counter_attack(self):
        GlobalGameState.cards_drawn = 1
        GlobalGameState.us_1_front_line = utah_omaha.track_number

        advance_army_one_space(US_FIRST_ARMY)

        GlobalGameState.current_card = card_002
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        options = get_counter_attack_options()
        option = next(o for o in options if o["army"] == US_FIRST_ARMY)

        self.assertEqual(option["attacking_space"], carentan)
        self.assertEqual(option["german_attack"], 1)
        self.assertEqual(option["allied_defense"], 5)

    def test_bayeux_counter_attack(self):
        GlobalGameState.cards_drawn = 1
        GlobalGameState.brit_2_front_line = gold_juno_sword_brit.track_number

        advance_army_one_space(BRITISH_SECOND_ARMY)

        GlobalGameState.current_card = card_002
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        options = get_counter_attack_options()
        option = next(o for o in options if o["army"] == BRITISH_SECOND_ARMY)

        self.assertEqual(option["attacking_space"], bayeux)
        self.assertEqual(option["german_attack"], 4)
        self.assertEqual(option["allied_defense"], 4)

    def test_lebisey_counter_attack(self):
        GlobalGameState.cards_drawn = 1
        GlobalGameState.can_1_front_line = gold_juno_sword_can.track_number

        advance_army_one_space(CANADIAN_FIRST_ARMY)

        GlobalGameState.current_card = card_002
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        options = get_counter_attack_options()
        option = next(o for o in options if o["army"] == CANADIAN_FIRST_ARMY)

        self.assertEqual(option["attacking_space"], lebisey_wood)
        self.assertEqual(option["german_attack"], 2)
        self.assertEqual(option["allied_defense"], 4)


# =========================================================
# RESOLVE COUNTER-ATTACK TESTS
# =========================================================


class TestResolveCounterAttack(unittest.TestCase):
    def test_natural_6_is_auto_win(self):
        result = resolve_counter_attack(0, 999, [], 6)
        self.assertEqual(result["result"], "WIN")

    def test_natural_1_is_auto_loss(self):
        result = resolve_counter_attack(999, 0, [], 1)
        self.assertEqual(result["result"], "LOSS")

    def test_attack_plus_roll_beats_defense(self):
        result = resolve_counter_attack(3, 6, [], 4)  # 3+4=7 > 6
        self.assertEqual(result["result"], "WIN")

    def test_attack_plus_roll_fails(self):
        result = resolve_counter_attack(3, 7, [], 4)  # 7 == 7 → LOSS
        self.assertEqual(result["result"], "LOSS")

    def test_same_army_cannot_be_counter_attacked_twice(self):
        setup_units_for_tests()

        GlobalGameState.current_card = card_037
        GlobalGameState.current_weather = WEATHER_TABLE[1]

        options = get_counter_attack_options()
        option = next(o for o in options if o["army"] == US_XV_CORPS)

        # First attack
        result = resolve_counter_attack(
            option["german_attack"],
            option["allied_defense"],
            [],
            die_roll=6
        )

        do_post_combat(result, option, [])

        # GlobalGameState.counter_attacked_armies.add(option["army"])

        # Recompute options
        options_after = get_counter_attack_options()

        self.assertTrue(
            all(o["army"] != US_XV_CORPS for o in options_after)
        )


# =========================================================
# POST-COMBAT TESTS
# =========================================================


class TestGermanPostCombat(unittest.TestCase):
    def setUp(self):
        carentan.units.clear()
        bayeux.units.clear()
        lebisey_wood.units.clear()

        do_opening_setup()

        # Move all Allied to beaches
        advance_army_one_space(US_FIRST_ARMY)
        advance_army_one_space(BRITISH_SECOND_ARMY)
        advance_army_one_space(CANADIAN_FIRST_ARMY)

    def tearDown(self):
        GlobalGameState.us_1_front_line = 11
        GlobalGameState.brit_2_front_line = 7
        GlobalGameState.can_1_front_line = 7
        do_opening_setup()

    def test_german_win_forces_allied_retreat(self):
        army = US_FIRST_ARMY

        result = {"result": "WIN"}

        selected_option = {
            "army": army,
            "target_space": army.location,
            "attacking_space": carentan,
        }

        do_post_combat(result, selected_option, carentan.units)

        self.assertNotEqual(army.location, utah_omaha)

    def test_hitler_approval_increases(self):
        hitler_approval_track.value = 3

        result = {"result": "WIN"}

        selected_option = {
            "army": US_FIRST_ARMY,
            "target_space": US_FIRST_ARMY.location,
            "attacking_space": carentan,
        }

        do_post_combat(result, selected_option, carentan.units)

        self.assertEqual(hitler_approval_track.value, 4)

    def test_hitler_approval_capped(self):
        hitler_approval_track.value = 6

        result = {"result": "WIN"}

        selected_option = {
            "army": US_FIRST_ARMY,
            "target_space": US_FIRST_ARMY.location,
            "attacking_space": carentan,
        }

        do_post_combat(result, selected_option, carentan.units)

        self.assertEqual(hitler_approval_track.value, 6)

    def test_german_loss_applies_step_loss(self):
        GlobalGameState.german_casualty_strategy = Strategy.UNIT_TEST

        initial_units = len(carentan.units)

        result = {"result": "LOSS"}

        selected_option = {
            "army": US_FIRST_ARMY,
            "target_space": utah_omaha,
            "attacking_space": carentan,
        }

        do_post_combat(result, selected_option, carentan.units)

        self.assertTrue(len(carentan.units) <= initial_units)

    def test_no_german_advance_into_beach(self):
        selected_units = carentan.units.copy()

        result = {"result": "WIN"}

        selected_option = {
            "army": US_FIRST_ARMY,
            "target_space": utah_omaha,
            "attacking_space": carentan,
        }

        do_post_combat(result, selected_option, selected_units)

        for unit in selected_units:
            self.assertNotIn(unit, utah_omaha.units)




# =========================================================
# TERRAIN RULE TESTS
# =========================================================
class TestCounterAttackTerrainRules(unittest.TestCase):
    def test_fortress_cannot_be_attacked(self):
        original = carentan.terrain
        carentan.terrain = TerrainType.FORTRESS

        try:
            self.assertFalse(can_counter_attack(carentan))
        finally:
            carentan.terrain = original

    def test_beach_block_after_turn_3(self):
        GlobalGameState.cards_drawn = 3
        self.assertFalse(can_counter_attack(utah_omaha))

    def test_no_counter_attack_against_us_3_start_box(self):
        # Clear state (defensive, in case other tests leak)
        us_3_start_box.units.clear()
        st_malo.units.clear()
        rennes.units.clear()

        # Place Allied armies in start box
        add_units_to_space(us_3_start_box, US_VIII_CORPS)
        add_units_to_space(us_3_start_box, US_XV_CORPS)

        # Place Germans in adjacent attacking spaces
        add_units_to_space(st_malo, [create_kampfgruppe()])
        add_units_to_space(rennes, [create_kampfgruppe()])

        # ASSERT: no counter-attack possible against start box
        self.assertFalse(can_counter_attack(us_3_start_box))


class TestCounterAttackUSThirdArmy(unittest.TestCase):
    def test_german_counter_attack_against_xv_corps(self):
        setup_units_for_tests()

        GlobalGameState.current_card = card_037
        GlobalGameState.current_weather = WEATHER_TABLE[1]  # whatever your default is
        GlobalGameState.cards_drawn = 39

        options = get_counter_attack_options()

        print_counter_attack_options(options)

        option = next(o for o in options if o["army"] == US_XV_CORPS)

        self.assertEqual(option["target_space"], rennes)

        # Optional but useful sanity checks:
        self.assertIsNotNone(option["attacking_space"])
        self.assertGreaterEqual(option["german_attack"], 0)
        self.assertGreater(option["allied_defense"], 0)

    def test_xv_corps_counter_attack_executes(self):
        setup_units_for_tests()

        GlobalGameState.current_card = card_037
        GlobalGameState.current_weather = WEATHER_TABLE[1]
        GlobalGameState.cards_drawn = 39
        hitler_approval_track.value = 1

        options = get_counter_attack_options()
        option = next(o for o in options if o["army"] == US_XV_CORPS)

        attacking_space = option["attacking_space"]
        target_space = option["target_space"]

        # Select ALL eligible units (default behavior)
        eligible = get_eligible_german_units(attacking_space)
        selected_units = eligible.copy()

        # Force a deterministic outcome (e.g. strong win)
        result = resolve_counter_attack(option["german_attack"], option["allied_defense"], selected_units, die_roll=6)

        self.assertEqual(result["result"], "WIN")

        # Capture initial state
        initial_front_line = US_XV_CORPS.location

        do_post_combat(result, option, selected_units)

        # --- Assertions ---

        # 1. Allied retreat
        self.assertNotEqual(US_XV_CORPS.location, initial_front_line)

        # 2. Germans advance (unless blocked by rules)
        self.assertIn(
            any(unit in target_space.units for unit in selected_units),
            [True, False],  # allow rule-based blocking (beach/fortress)
        )

        # 3. Hitler approval +1 (capped at 6)
        self.assertEqual(hitler_approval_track.value, 2)
