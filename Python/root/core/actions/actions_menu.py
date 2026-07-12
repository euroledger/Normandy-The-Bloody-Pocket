from random import randint

from core.actions.counter_attack_action import do_counter_attack
from core.actions.strategic_reserve_actions import do_move_panzer_from_strategic_reserve
from core.enums import ReinforcementType
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    in_transit_box,
    strategic_reserve_box,
    transport_track,
)

YELLOW = "\033[33m"
RESET = "\033[0m"


def list_user_actions():
    print(YELLOW)
    print("AVAILABLE ACTIONS")
    print(f"ACTIONS REMAINING: {GlobalGameState.actions_left_this_turn}")
    print()

    print("1. Counter-Attack (1)")
    print("2. Move Panzer Division From Strategic Reserve (1)")
    print("3. Move Panzer Division To Strategic Reserve (1)")
    print("4. Move Other Unit from Strategic Reserve (0)")
    print("5. Do Resource Augmentation Roll (1)")
    print("6. Place Fortified Villages Marker (3)")
    print("7. Move Unit One Space (1)")
    print("8. Refit Panzer Division (1)")
    print("9. Move Action Point to Strategic Reserve (1)")

    print(RESET)


# def get_german_controlled_spaces():
#     spaces = [
#         space
#         for space in get_all_map_spaces()
#         if hasattr(space, "controlling_player") and space.controlling_player == SideType.GERMAN
#     ]

#     unique_spaces = []

#     for space in spaces:
#         if space not in unique_spaces:
#             unique_spaces.append(space)

#     track_order = {
#         "US FIRST ARMY": 1,
#         "BRIT SECOND ARMY": 2,
#         "CANADIAN FIRST ARMY": 3,
#         "US THIRD ARMY": 4,
#         "NO TRACK": 5,
#     }

#     unique_spaces.sort(
#         key=lambda space: (track_order.get(space.track.value if space.track else "NO TRACK"), -space.track_number)
#     )

#     return unique_spaces


# def get_panzer_divisions_in_strategic_reserve():
#     return [
#         unit
#         for unit in strategic_reserve_box.units
#         if isinstance(unit, GermanUnit) and unit.type == ReinforcementType.PZ_DIV
#     ]


# LIGHT_BROWN = "\033[38;5;180m"
# BLUE = "\033[94m"
# RED = "\033[91m"
# GREEN = "\033[92m"
# GREY = "\033[90m"
# RESET = "\033[0m"


# def print_space_section(title, spaces, color, display_spaces):
#     if not spaces:
#         return

#     print()
#     print(f"{color}{title}{RESET}")

#     for space in spaces:
#         display_spaces.append(space)
#         index = len(display_spaces)

#         print(f"{color}{index}. {space.name} (#{space.track_number}){RESET}")


# def print_german_controlled_spaces(spaces):
#     us_1_spaces = []
#     brit_2_spaces = []
#     can_1_spaces = []
#     us_3_spaces = []
#     falaise_gap_spaces = []
#     display_spaces = []
#     for space in spaces:
#         if space.name == "FALAISE GAP":
#             falaise_gap_spaces.append(space)
#         elif space.track.value == "US FIRST ARMY":
#             us_1_spaces.append(space)
#         elif space.track.value == "BRIT SECOND ARMY":
#             brit_2_spaces.append(space)
#         elif space.track.value == "CANADIAN FIRST ARMY":
#             can_1_spaces.append(space)
#         elif space.track.value == "US THIRD ARMY":
#             us_3_spaces.append(space)
#     print()
#     print("SELECT GERMAN-CONTROLLED SPACE")

#     print_space_section("US 1ST ARMY", us_1_spaces, LIGHT_BROWN, display_spaces)
#     print_space_section("BRIT 2ND ARMY", brit_2_spaces, BLUE, display_spaces)
#     print_space_section("CAN 1ST ARMY", can_1_spaces, RED, display_spaces)
#     print_space_section("US 3RD ARMY", us_3_spaces, GREEN, display_spaces)
#     print_space_section("FALAISE GAP", falaise_gap_spaces[:1], GREY, display_spaces)

#     print()
#     print("0. Return to main menu")

#     return display_spaces


# def do_move_panzer_from_strategic_reserve():
#     print("MOVE PANZER DIVISION FROM STRATEGIC RESERVE")
#     print()

#     panzer_divisions = get_panzer_divisions_in_strategic_reserve()

#     if not panzer_divisions:
#         print("No Panzer Divisions in Strategic Reserve")
#         return

#     print("SELECT PANZER DIVISION")
#     print()

#     for index, unit in enumerate(panzer_divisions, start=1):
#         print(f"{index}. {unit.name} ({unit.combat_value})")

#     print()
#     print("0. Return to main menu")
#     print()

#     choice = input("Choice: ").strip()

#     if choice == "0":
#         return

#     if not choice.isdigit():
#         print("INVALID CHOICE")
#         return

#     selected_index = int(choice) - 1

#     if selected_index < 0 or selected_index >= len(panzer_divisions):
#         print("INVALID CHOICE")
#         return

#     selected_panzer = panzer_divisions[selected_index]

#     print()
#     print(f"SELECTED: {selected_panzer.name}")

#     GlobalGameState.actions_left_this_turn -= 1

#     german_spaces = get_german_controlled_spaces()

#     if not german_spaces:
#         print("No German-controlled spaces available")
#         return

#     print_german_controlled_spaces(german_spaces)
#     choice = input("Choice: ").strip()
#     if choice == "0":
#         return
#     if not choice.isdigit():
#         print("INVALID CHOICE")
#         return
#     selected_index = int(choice) - 1
#     if selected_index < 0 or selected_index >= len(german_spaces):
#         print("INVALID CHOICE")
#         return
#     selected_space = german_spaces[selected_index]

#     strategic_reserve_box.units.remove(selected_panzer)
#     selected_space.units.append(selected_panzer)
#     GlobalGameState.actions_left_this_turn -= 1
#     print()
#     print(f"{selected_panzer.name} moved to {selected_space.name}")


def do_move_panzer_to_strategic_reserve():
    print("MOVE PANZER DIVISION TO STRATEGIC RESERVE")


def do_move_other_unit_from_strategic_reserve():
    print("MOVE OTHER UNIT FROM STRATEGIC RESERVE")


def do_resource_augmentation_roll():
    print("RESOURCE AUGMENTATION ROLL")


def do_build_fortified_villages():
    print("BUILD FORTIFIED VILLAGES")


def do_move_unit_one_space():
    print("MOVE UNIT ONE SPACE")


def do_refit_panzer_division():
    print("REFIT PANZER DIVISION")


def do_move_action_point_to_strategic_reserve():
    print("MOVE ACTION POINT TO STRATEGIC RESERVE")


def choose_user_action():
    choice = input("Choose Action: ")

    if choice == "1":
        do_counter_attack()
    elif choice == "2":
        do_move_panzer_from_strategic_reserve()
    elif choice == "3":
        do_move_panzer_to_strategic_reserve()
    elif choice == "4":
        do_move_other_unit_from_strategic_reserve()
    elif choice == "5":
        do_resource_augmentation_roll()
    elif choice == "6":
        do_build_fortified_villages()
    elif choice == "7":
        do_move_unit_one_space()
    elif choice == "8":
        do_refit_panzer_division()
    elif choice == "9":
        do_move_action_point_to_strategic_reserve()
    else:
        print("INVALID ACTION")


def do_panzer_transport_check(unit, die_roll):
    modified_roll = die_roll + GlobalGameState.transport_check_drm

    print(f"{unit}")
    print(f"ROLL: {die_roll}")
    print(f"DRM: {GlobalGameState.transport_check_drm:+}")
    print(f"MODIFIED ROLL: {modified_roll}")
    print(f"CHECK: {modified_roll} <= Transport {transport_track.value}")

    if modified_roll <= transport_track.value:
        in_transit_box.units.remove(unit)
        strategic_reserve_box.units.append(unit)

        print(f"\t=>{unit} MOVED TO STRATEGIC RESERVE")
        return True

    print(f"\t=>{unit} REMAINS IN TRANSIT")
    return False


def do_action_phase(card, weather):
    GlobalGameState.actions_left_this_turn = card.actions.actions_available

    print()
    print("========================================")
    print("ACTION PHASE")
    print("========================================")
    print()

    # 1. Print number actions

    print(f"ACTIONS AVAILABLE: {GlobalGameState.actions_left_this_turn}")
    print()

    # 2. Do In Transit Pz Div Resource Roll (roll against Transport Level)

    panzer_divisions = [unit for unit in in_transit_box.units[:] if unit.type == ReinforcementType.PZ_DIV]

    for unit in panzer_divisions:
        die_roll = randint(1, 6)
        do_panzer_transport_check(unit, die_roll)

    # 3. Check Card Specific Events, eg Hitler Intervention

    # 4. List Menu of Actions

    # 5. Choose an action -> Implement Action

    while GlobalGameState.actions_left_this_turn > 0:
        list_user_actions()
        choose_user_action()

    print()
    print("NO ACTIONS LEFT")
