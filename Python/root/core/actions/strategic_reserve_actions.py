from core.enums import ReinforcementType, SideType
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    strategic_reserve_box,
)
from core.map.map_utilities import (
    get_all_map_spaces,
)
from core.models import GermanUnit


def get_german_controlled_spaces():
    spaces = [
        space
        for space in get_all_map_spaces()
        if hasattr(space, "controlling_player") and space.controlling_player == SideType.GERMAN
    ]
    unique_spaces = []
    for space in spaces:
        if space not in unique_spaces:
            unique_spaces.append(space)

    track_order = {
        "US FIRST ARMY": 1,
        "BRIT SECOND ARMY": 2,
        "CANADIAN FIRST ARMY": 3,
        "US THIRD ARMY": 4,
        "NO TRACK": 5,
    }
    unique_spaces.sort(
        key=lambda space: (
            track_order.get(space.track.value if space.track else "NO TRACK"),
            -space.track_number,
        )
    )
    return unique_spaces


def get_panzer_divisions_in_strategic_reserve():
    return [
        unit
        for unit in strategic_reserve_box.units
        if isinstance(unit, GermanUnit) and unit.type == ReinforcementType.PZ_DIV
    ]


LIGHT_BROWN = "\033[38;5;180m"
BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
GREY = "\033[90m"
RESET = "\033[0m"


def print_space_section(title, spaces, color, display_spaces):
    if not spaces:
        return

    print()
    print(f"{color}{title}{RESET}")

    for space in spaces:
        display_spaces.append(space)
        index = len(display_spaces)

        german_units = [unit for unit in space.units if isinstance(unit, GermanUnit)]

        if german_units:
            units_text = ", ".join(f"{unit.name} ({unit.combat_value})" for unit in german_units)
            print(f"{color}{index}. {space.name} (#{space.track_number}) - {units_text}{RESET}")
        else:
            print(f"{color}{index}. {space.name} (#{space.track_number}){RESET}")


def print_german_controlled_spaces(spaces):
    us_1_spaces = []
    brit_2_spaces = []
    can_1_spaces = []
    us_3_spaces = []
    falaise_gap_spaces = []

    for space in spaces:
        if space.name == "FALAISE GAP":
            falaise_gap_spaces.append(space)
        elif space.track.value == "US FIRST ARMY":
            us_1_spaces.append(space)
        elif space.track.value == "BRIT SECOND ARMY":
            brit_2_spaces.append(space)
        elif space.track.value == "CANADIAN FIRST ARMY":
            can_1_spaces.append(space)
        elif space.track.value == "US THIRD ARMY":
            us_3_spaces.append(space)

    display_spaces = []

    print()
    print("SELECT GERMAN-CONTROLLED SPACE")

    print_space_section("US 1ST ARMY", us_1_spaces, LIGHT_BROWN, display_spaces)
    print_space_section("BRIT 2ND ARMY", brit_2_spaces, BLUE, display_spaces)
    print_space_section("CAN 1ST ARMY", can_1_spaces, RED, display_spaces)
    print_space_section("US 3RD ARMY", us_3_spaces, GREEN, display_spaces)
    print_space_section("FALAISE GAP", falaise_gap_spaces[:1], GREY, display_spaces)

    print()
    print("0. Return to main menu")

    return display_spaces


def do_move_panzer_from_strategic_reserve():
    print("MOVE PANZER DIVISION FROM STRATEGIC RESERVE")
    print()

    panzer_divisions = get_panzer_divisions_in_strategic_reserve()

    if not panzer_divisions:
        print("No Panzer Divisions in Strategic Reserve")
        return

    print("SELECT PANZER DIVISION")
    print()

    for index, unit in enumerate(panzer_divisions, start=1):
        print(f"{index}. {unit.name} ({unit.combat_value})")

    print()
    print("0. Return to main menu")
    print()

    choice = input("Choice: ").strip()
    if choice == "0":
        return

    if not choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(choice) - 1
    if selected_index < 0 or selected_index >= len(panzer_divisions):
        print("INVALID CHOICE")
        return

    selected_panzer = panzer_divisions[selected_index]

    print()
    print(f"SELECTED: {selected_panzer.name}")

    german_spaces = get_german_controlled_spaces()
    if not german_spaces:
        print("No German-controlled spaces available")
        return
    display_spaces = print_german_controlled_spaces(german_spaces)
    choice = input("Choice: ").strip()

    if choice == "0":
        return

    if not choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(choice) - 1

    if selected_index < 0 or selected_index >= len(display_spaces):
        print("INVALID CHOICE")
        return

    selected_space = display_spaces[selected_index]

    strategic_reserve_box.units.remove(selected_panzer)
    selected_space.units.append(selected_panzer)

    GlobalGameState.actions_left_this_turn -= 1

    print()
    print(f"{selected_panzer.name} moved to {selected_space.name}")
