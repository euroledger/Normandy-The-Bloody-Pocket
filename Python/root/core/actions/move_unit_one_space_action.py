from core.actions.actions_helper import get_german_controlled_spaces, get_adjacent_german_controlled_spaces, use_action
from core.global_game_state import GlobalGameState
from core.german_units import GermanUnit


def do_move_unit_one_space(unit_choice=None, space_choice=None):
    print("MOVE UNIT ONE SPACE")
    print()

    german_controlled_spaces = get_german_controlled_spaces()
    movable_units = []

    for space in german_controlled_spaces:
        for unit in space.units:
            if isinstance(unit, GermanUnit):
                movable_units.append((space, unit))

    if not movable_units:
        print("NO GERMAN UNITS AVAILABLE TO MOVE")
        return

    if unit_choice is None:
        print("SELECT GERMAN UNIT")
        print()

        for index, (space, unit) in enumerate(movable_units, start=1):
            print(f"{index}. {unit.name} ({unit.combat_value}) - {space.name}")

        print()
        print("0. Return to main menu")

        unit_choice = input("Choice: ").strip()

        if unit_choice == "0":
            return

        if not unit_choice.isdigit():
            print("INVALID CHOICE")
            return

        selected_index = int(unit_choice) - 1

        if selected_index < 0 or selected_index >= len(movable_units):
            print("INVALID CHOICE")
            return

        current_space, selected_unit = movable_units[selected_index]

    else:
        selected_unit = unit_choice
        matching_units = [(space, unit) for space, unit in movable_units if unit is selected_unit]

        if not matching_units:
            print("INVALID UNIT")
            return

        current_space, selected_unit = matching_units[0]

    destination_spaces = get_adjacent_german_controlled_spaces(current_space)

    if not destination_spaces:
        print("NO LEGAL DESTINATIONS")
        return

    print()
    print(f"SELECT DESTINATION FOR {selected_unit.name}")
    print()

    if space_choice is None:
        print("SELECT GERMAN-CONTROLLED SPACE")
        print()

        for index, space in enumerate(destination_spaces, start=1):
            print(f"{index}. {space.name}")

        print()
        print("0. Return to main menu")

        space_choice = input("Choice: ").strip()

        if space_choice == "0":
            return

        if not space_choice.isdigit():
            print("INVALID CHOICE")
            return

        selected_index = int(space_choice) - 1

        if selected_index < 0 or selected_index >= len(destination_spaces):
            print("INVALID CHOICE")
            return

        selected_space = destination_spaces[selected_index]

    else:
        selected_space = space_choice

        if selected_space not in destination_spaces:
            print("INVALID DESTINATION")
            return
    if not use_action():
        print("NOT ENOUGH ACTIONS")
        return
    current_space.units.remove(selected_unit)
    selected_space.units.append(selected_unit)

    print()
    print(f"{selected_unit.name} MOVED FROM {current_space.name} TO {selected_space.name}")
    print(f"ACTIONS REMAINING: {GlobalGameState.actions_left_this_turn}")
