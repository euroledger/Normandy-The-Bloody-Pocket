from core.enums import SideType
from core.map.map_utilities import get_all_map_spaces
from core.models import GermanUnit


LIGHT_BROWN = "\033[38;5;180m"
BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
GREY = "\033[90m"
RESET = "\033[0m"

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


def get_display_spaces(show_menu):
    german_spaces = get_german_controlled_spaces()

    if not german_spaces:
        print("No German-controlled spaces available")
        return None

    display_spaces = build_display_spaces(german_spaces)

    if show_menu:
        print_display_spaces(display_spaces)

    return display_spaces


def print_space_section(title, spaces, color, display_spaces):
    if not spaces:
        return
    print()
    print(f"{color}{title}{RESET}")
    for space in spaces:
        display_spaces.append(space)
        index = len(display_spaces)
        german_units = [unit for unit in space.units if isinstance(unit, GermanUnit)]
        marker = ""
        if space.fortified_village_modifier == 1:
            marker = " - FORTIFIED VILLAGES +1"
        elif space.fortified_village_modifier == 2:
            marker = " - FORTIFIED VILLAGES +2"
        if german_units:
            units_text = ", ".join(f"{unit.name} ({unit.combat_value})" for unit in german_units)
            print(f"{color}{index}. {space.name} (#{space.track_number}){marker} - {units_text}{RESET}")
        else:
            print(f"{color}{index}. {space.name} (#{space.track_number}){marker}{RESET}")


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
    print_space_section("1st CAN ARMY", can_1_spaces, RED, numbered_spaces)
    print_space_section("US 3RD ARMY", us_3_spaces, GREEN, numbered_spaces)
    print_space_section("FALAISE GAP", falaise_gap_spaces, GREY, numbered_spaces)

    print()
    print("0. Return to main menu")
