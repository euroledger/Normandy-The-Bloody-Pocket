from core.actions.actions_helper import get_display_spaces, get_german_controlled_spaces
from core.actions.stacking_limits import PANZER_STACKING_LIMIT
from core.enums import ReinforcementType
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
