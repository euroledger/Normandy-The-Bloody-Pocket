from core.actions.stacking_limits import PANZER_STACKING_LIMIT
from core.enums import ReinforcementType, SideType
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    eliminated_units_box,
    hitler_approval_track,
    transport_track,
    in_transit_box,
    strategic_reserve_box,
)
from core.map.map_utilities import (
    get_all_map_spaces,
)
from core.models import GermanUnit, ReinforcementType



def get_panzer_divisions_on_map():
    panzer_divisions = []

    for space in get_all_map_spaces():
        if space in [in_transit_box, strategic_reserve_box, eliminated_units_box]:
            continue

        for unit in space.units:
            if isinstance(unit, GermanUnit) and unit.type == ReinforcementType.PZ_DIV:
                panzer_divisions.append((space, unit))

    return panzer_divisions


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
        if isinstance(unit, GermanUnit) and unit.type in [ReinforcementType.PZ_DIV]
    ]


def get_other_units_in_strategic_reserve():
    return [
        unit
        for unit in strategic_reserve_box.units
        if isinstance(unit, GermanUnit) and unit.type != ReinforcementType.PZ_DIV
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


def build_display_spaces(spaces):
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
    display_spaces.extend(us_1_spaces)
    display_spaces.extend(brit_2_spaces)
    display_spaces.extend(can_1_spaces)
    display_spaces.extend(us_3_spaces)
    display_spaces.extend(falaise_gap_spaces[:1])

    return display_spaces


def print_display_spaces(display_spaces):
    us_1_spaces = [space for space in display_spaces if space.track and space.track.value == "US FIRST ARMY"]
    brit_2_spaces = [space for space in display_spaces if space.track and space.track.value == "BRIT SECOND ARMY"]
    can_1_spaces = [space for space in display_spaces if space.track and space.track.value == "CANADIAN FIRST ARMY"]
    us_3_spaces = [space for space in display_spaces if space.track and space.track.value == "US THIRD ARMY"]
    falaise_gap_spaces = [space for space in display_spaces if space.name == "FALAISE GAP"]

    numbered_spaces = []

    print()
    print("SELECT GERMAN-CONTROLLED SPACE")

    print_space_section("US 1ST ARMY", us_1_spaces, LIGHT_BROWN, numbered_spaces)
    print_space_section("BRIT 2ND ARMY", brit_2_spaces, BLUE, numbered_spaces)
    print_space_section("CAN 1ST ARMY", can_1_spaces, RED, numbered_spaces)
    print_space_section("US 3RD ARMY", us_3_spaces, GREEN, numbered_spaces)
    print_space_section("FALAISE GAP", falaise_gap_spaces, GREY, numbered_spaces)

    print()
    print("0. Return to main menu")


def get_display_spaces(show_menu):
    german_spaces = get_german_controlled_spaces()

    if not german_spaces:
        print("No German-controlled spaces available")
        return None

    display_spaces = build_display_spaces(german_spaces)

    if show_menu:
        print_display_spaces(display_spaces)

    return display_spaces


def do_move_other_unit_from_strategic_reserve(unit_choice=None, space_choice=None):
    print("MOVE OTHER UNIT FROM STRATEGIC RESERVE")
    print()

    units = get_other_units_in_strategic_reserve()

    if not units:
        print("No Units in Strategic Reserve")
        return

    print("SELECT UNIT")
    print()

    for index, unit in enumerate(units, start=1):
        print(f"{index}. {unit.name} ({unit.combat_value})")

    print()
    print("0. Return to main menu")
    print()

    if unit_choice is None:
        unit_choice = input("Choice: ").strip()
    else:
        unit_choice = str(unit_choice).strip()

    if unit_choice == "0":
        return

    if not unit_choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(unit_choice) - 1

    if selected_index < 0 or selected_index >= len(units):
        print("INVALID CHOICE")
        return

    selected_unit = units[selected_index]

    print()
    print(f"SELECTED: {selected_unit.name}")

    german_spaces = get_german_controlled_spaces()

    if not german_spaces:
        print("No German-controlled spaces available")
        return

    # if space_choice is None:
    #     display_spaces = print_german_controlled_spaces(german_spaces)
    #     space_choice = input("Choice: ").strip()
    # else:
    # space_choice = str(space_choice).strip()

    display_spaces = get_display_spaces(space_choice is None)

    if display_spaces is None:
        return

    if space_choice is None:
        space_choice = input("Choice: ").strip()
    else:
        space_choice = str(space_choice).strip()

    if space_choice == "0":
        return

    if not space_choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(space_choice) - 1

    if selected_index < 0 or selected_index >= len(display_spaces):
        print("INVALID CHOICE")
        return

    selected_space = display_spaces[selected_index]

    print()
    print(f"{selected_unit.name} moved to {selected_space.name}")

    strategic_reserve_box.units.remove(selected_unit)
    selected_space.units.append(selected_unit)


def do_move_panzer_to_strategic_reserve(die_roll, div_choice=None):
    print("MOVE PANZER DIVISION TO STRATEGIC RESERVE")
    print()

    panzer_divisions = get_panzer_divisions_on_map()

    if not panzer_divisions:
        print("No Panzer Divisions on the map")
        return

    print("SELECT PANZER DIVISION")
    print()

    for index, (space, unit) in enumerate(panzer_divisions, start=1):
        print(f"{index}. {unit.name} ({unit.combat_value}) - {space.name}")

    print()
    print("0. Return to main menu")
    print()

    if div_choice is None:
        div_choice = input("Choice: ").strip()
    else:
        div_choice = str(div_choice).strip()

    if div_choice == "0":
        return

    if not div_choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(div_choice) - 1

    if selected_index < 0 or selected_index >= len(panzer_divisions):
        print("INVALID CHOICE")
        return

    selected_space, selected_panzer = panzer_divisions[selected_index]

    print()
    print(f"SELECTED: {selected_panzer.name}")

    print()
    print("TRANSPORT CHECK")
    print(f"ROLL: {die_roll}")
    print(f"TRANSPORT LEVEL: {transport_track.value}")

    if die_roll > transport_track.value:
        print("RESULT: FAILED")
        return

    print("RESULT: PASSED")
    print()
    print(f"{selected_panzer.name} moved to Strategic Reserve")

    selected_space.units.remove(selected_panzer)
    strategic_reserve_box.units.append(selected_panzer)

    GlobalGameState.actions_left_this_turn -= 1


# TODO move this into separate helper file to be used in move one unit action
# Need to add types of units to check (eg Panzer, FlaK, Fallschirmjager etc)
def check_stacking(space):
    panzer_units = [
        unit
        for unit in space.units
        if isinstance(unit, GermanUnit)
        and unit.type in [ReinforcementType.PZ_DIV, ReinforcementType.KAMPFGRUPPE]
    ]

    if len(panzer_units) >= PANZER_STACKING_LIMIT:
        print("STACKING LIMIT REACHED, INVALID MOVE")
        return False

    return True

def do_move_panzer_from_strategic_reserve(die_roll, div_choice=None, space_choice=None):
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

    if div_choice is None:
        div_choice = input("Choice: ").strip()
    else:
        div_choice = str(div_choice).strip()

    if div_choice == "0":
        return

    if not div_choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(div_choice) - 1

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

    display_spaces = get_display_spaces(space_choice is None)

    if display_spaces is None:
        return

    if space_choice is None:
        space_choice = input("Choice: ").strip()
    else:
        space_choice = str(space_choice).strip()

    if space_choice == "0":
        return

    if not space_choice.isdigit():
        print("INVALID CHOICE")
        return

    selected_index = int(space_choice) - 1

    if selected_index < 0 or selected_index >= len(display_spaces):
        print("INVALID CHOICE")
        return

    selected_space = display_spaces[selected_index]

    # Check Stacking -> Maximum 4 Panzer Units (Div or Kampfgruppe) per space
    if check_stacking(selected_space) == False:
        return

    print()
    print("HITLER APPROVAL CHECK")
    print(f"ROLL: {die_roll}")
    print(f"HITLER APPROVAL: {hitler_approval_track.value}")

    if die_roll > hitler_approval_track.value:
        print("RESULT: FAILED")
        return

    print("RESULT: PASSED")
    print()
    print(f"{selected_panzer.name} moved to {selected_space.name}")

    strategic_reserve_box.units.remove(selected_panzer)
    selected_space.units.append(selected_panzer)

    GlobalGameState.actions_left_this_turn -= 1
