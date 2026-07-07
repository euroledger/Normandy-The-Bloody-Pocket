import json
import os
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

from cards.decks import draw_deck
from cards.card_3 import card as card_003
from cards.card_4 import card as card_004
from cards.card_20 import card as card_020

from core.save_load_game import save_game, load_game
from core.global_game_state import GlobalGameState
from core.map.map_utilities import do_opening_setup
from core.map.map_model import (
    transport_track,
    supply_track,
    hitler_approval_track,
    in_transit_box,
    strategic_reserve_box,
    eliminated_units_box,
)
from core.map.map_spaces_brit_2 import bayeux
from core.german_units import (
    PZ_LEHR,
    PZ_21,
    SS_12,
    create_flak88,
    create_nebelwerfer,
)
from core.enums import SideType
from core.weather import get_weather_result


def reset_game_state_for_tests():
    do_opening_setup()

    draw_deck[:] = [
        card_003,
        card_004,
        card_020,
    ]

    GlobalGameState.cards_drawn = 0
    GlobalGameState.drawn_cards = []
    GlobalGameState.mid_deck_added = False
    GlobalGameState.late_deck_added = False
    GlobalGameState.current_card = None
    GlobalGameState.current_weather = None
    GlobalGameState.current_carpet_bombing = 0
    GlobalGameState.current_step = 1

    GlobalGameState.us_1_front_line = 11
    GlobalGameState.brit_2_front_line = 7
    GlobalGameState.can_1_front_line = 7
    GlobalGameState.us_3_front_line = 8
    GlobalGameState.us_viii_front_line = 7
    GlobalGameState.us_xv_front_line = 4

    transport_track.value = 5
    supply_track.value = 4
    hitler_approval_track.value = 6

    in_transit_box.units.clear()
    strategic_reserve_box.units.clear()
    eliminated_units_box.units.clear()


class TestSaveLoadGame(unittest.TestCase):
    def setUp(self):
        reset_game_state_for_tests()

    def tearDown(self):
        reset_game_state_for_tests()

    def test_save_game_creates_json_file(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                with patch("builtins.input", return_value="test_save"):
                    save_game()

                self.assertTrue(os.path.exists("data/test_save.json"))

            finally:
                os.chdir(old_cwd)

    def test_save_game_cancels_empty_filename(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                with patch("builtins.input", return_value=""):
                    save_game()

                self.assertFalse(os.path.exists("data"))

            finally:
                os.chdir(old_cwd)

    def test_save_game_writes_generic_global_game_state(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                GlobalGameState.cards_drawn = 2
                GlobalGameState.drawn_cards = [card_003, card_004]
                GlobalGameState.current_card = card_004
                GlobalGameState.current_weather = get_weather_result(3)
                GlobalGameState.current_carpet_bombing = 2
                GlobalGameState.mid_deck_added = True
                GlobalGameState.us_1_front_line = 99

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                with open("data/test_save.json", "r", encoding="utf-8") as save_file:
                    save_data = json.load(save_file)

                saved_state = save_data["global_game_state"]

                self.assertEqual(saved_state["cards_drawn"], 2)
                self.assertEqual(saved_state["drawn_cards"], [3, 4])
                self.assertEqual(saved_state["current_card"], 4)
                self.assertEqual(saved_state["current_carpet_bombing"], 2)
                self.assertTrue(saved_state["mid_deck_added"])
                self.assertEqual(saved_state["us_1_front_line"], 99)

            finally:
                os.chdir(old_cwd)

    def test_save_game_writes_resource_tracks(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                transport_track.value = 1
                supply_track.value = 2
                hitler_approval_track.value = -1

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                with open("data/test_save.json", "r", encoding="utf-8") as save_file:
                    save_data = json.load(save_file)

                self.assertEqual(
                    save_data["resource_tracks"],
                    {
                        "transport": 1,
                        "supply": 2,
                        "hitler_approval": -1,
                    },
                )

            finally:
                os.chdir(old_cwd)

    def test_save_game_writes_unit_boxes(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                in_transit_box.units[:] = [PZ_LEHR]
                strategic_reserve_box.units[:] = [SS_12]
                eliminated_units_box.units[:] = [PZ_21]

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                with open("data/test_save.json", "r", encoding="utf-8") as save_file:
                    save_data = json.load(save_file)

                self.assertEqual(save_data["unit_boxes"]["in_transit"], ["Panzer Lehr"])
                self.assertEqual(save_data["unit_boxes"]["strategic_reserve"], ["12th SS Panzer"])
                self.assertEqual(save_data["unit_boxes"]["eliminated_units"], ["21st Panzer"])

            finally:
                os.chdir(old_cwd)

    def test_save_game_writes_map_space_state(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                bayeux.units[:] = [
                    PZ_LEHR,
                    create_nebelwerfer(),
                    create_flak88(),
                ]
                bayeux.under_siege = True
                bayeux.fortified = True
                bayeux.fortified_village_modifier = 2
                bayeux.controlling_player = SideType.ALLIED

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                with open("data/test_save.json", "r", encoding="utf-8") as save_file:
                    save_data = json.load(save_file)

                saved_bayeux = save_data["map_spaces"][bayeux.name]

                self.assertEqual(
                    saved_bayeux["units"],
                    [
                        "Panzer Lehr",
                        "Nebelwerfer",
                        "Flak 88",
                    ],
                )
                self.assertTrue(saved_bayeux["under_siege"])
                self.assertTrue(saved_bayeux["fortified"])
                self.assertEqual(saved_bayeux["fortified_village_modifier"], 2)
                self.assertEqual(saved_bayeux["controlling_player"], "ALLIED")

            finally:
                os.chdir(old_cwd)

    def test_load_game_rejects_missing_file_without_crashing(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                GlobalGameState.cards_drawn = 7

                with patch("builtins.input", return_value="missing"):
                    load_game()

                self.assertEqual(GlobalGameState.cards_drawn, 7)

            finally:
                os.chdir(old_cwd)

    def test_load_game_restores_global_game_state(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                GlobalGameState.cards_drawn = 2
                GlobalGameState.drawn_cards = [card_003, card_004]
                GlobalGameState.current_card = card_004
                GlobalGameState.mid_deck_added = True
                GlobalGameState.current_carpet_bombing = 3
                GlobalGameState.us_1_front_line = 99

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                GlobalGameState.cards_drawn = 0
                GlobalGameState.drawn_cards = []
                GlobalGameState.current_card = None
                GlobalGameState.mid_deck_added = False
                GlobalGameState.current_carpet_bombing = 0
                GlobalGameState.us_1_front_line = 11

                with patch("builtins.input", return_value="test_save"):
                    load_game()

                self.assertEqual(GlobalGameState.cards_drawn, 2)
                self.assertEqual(
                    [card.card_id for card in GlobalGameState.drawn_cards],
                    [3, 4],
                )
                self.assertEqual(GlobalGameState.current_card.card_id, 4)
                self.assertTrue(GlobalGameState.mid_deck_added)
                self.assertEqual(GlobalGameState.current_carpet_bombing, 3)
                self.assertEqual(GlobalGameState.us_1_front_line, 99)

            finally:
                os.chdir(old_cwd)

    def test_load_game_restores_draw_deck(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                draw_deck[:] = [card_020, card_004]

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                draw_deck[:] = []

                with patch("builtins.input", return_value="test_save"):
                    load_game()

                self.assertEqual(
                    [card.card_id for card in draw_deck],
                    [20, 4],
                )

            finally:
                os.chdir(old_cwd)

    def test_load_game_restores_resource_tracks(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                transport_track.value = 1
                supply_track.value = 2
                hitler_approval_track.value = -1

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                transport_track.value = 5
                supply_track.value = 4
                hitler_approval_track.value = 6

                with patch("builtins.input", return_value="test_save"):
                    load_game()

                self.assertEqual(transport_track.value, 1)
                self.assertEqual(supply_track.value, 2)
                self.assertEqual(hitler_approval_track.value, -1)

            finally:
                os.chdir(old_cwd)

    def test_load_game_restores_unit_boxes(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                in_transit_box.units[:] = [PZ_LEHR]
                strategic_reserve_box.units[:] = [SS_12]
                eliminated_units_box.units[:] = [PZ_21]

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                in_transit_box.units.clear()
                strategic_reserve_box.units.clear()
                eliminated_units_box.units.clear()

                with patch("builtins.input", return_value="test_save"):
                    load_game()

                self.assertEqual([unit.name for unit in in_transit_box.units], ["Panzer Lehr"])
                self.assertEqual([unit.name for unit in strategic_reserve_box.units], ["12th SS Panzer"])
                self.assertEqual([unit.name for unit in eliminated_units_box.units], ["21st Panzer"])

            finally:
                os.chdir(old_cwd)

    def test_load_game_restores_map_space_state(self):
        with TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            os.chdir(tmp_dir)

            try:
                bayeux.units[:] = [
                    PZ_LEHR,
                    create_nebelwerfer(),
                    create_flak88(),
                ]
                bayeux.under_siege = True
                bayeux.fortified = True
                bayeux.fortified_village_modifier = 2
                bayeux.controlling_player = SideType.ALLIED

                with patch("builtins.input", return_value="test_save"):
                    save_game()

                bayeux.units.clear()
                bayeux.under_siege = False
                bayeux.fortified = False
                bayeux.fortified_village_modifier = 0
                bayeux.controlling_player = SideType.GERMAN

                with patch("builtins.input", return_value="test_save"):
                    load_game()

                self.assertEqual(
                    [unit.name for unit in bayeux.units],
                    [
                        "Panzer Lehr",
                        "Nebelwerfer",
                        "Flak 88",
                    ],
                )
                self.assertTrue(bayeux.under_siege)
                self.assertTrue(bayeux.fortified)
                self.assertEqual(bayeux.fortified_village_modifier, 2)
                self.assertEqual(bayeux.controlling_player, SideType.ALLIED)

            finally:
                os.chdir(old_cwd)