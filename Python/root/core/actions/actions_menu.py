from random import randint

from core.actions.counter_attack_action import do_counter_attack
from core.actions.strategic_reserve_actions import do_move_other_unit_from_strategic_reserve, do_move_panzer_from_strategic_reserve, do_move_panzer_to_strategic_reserve, get_panzer_divisions_in_strategic_reserve
from core.enums import ReinforcementType
from core.game_summary import print_game_summary
from core.german_units import TIGER_101
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    in_transit_box,
    strategic_reserve_box,
    transport_track,
)

YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"


def list_user_actions():
    print(YELLOW)
    print("AVAILABLE ACTIONS")
    print(f"ACTIONS REMAINING: {GlobalGameState.actions_left_this_turn}")
    print()

    if TIGER_101 in strategic_reserve_box.units:
        print(f"{GREEN}*** 101st TIGER BN AVAILABLE ***{YELLOW}")

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
    print("G. Game Summary")

    print(RESET)



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
        do_move_panzer_from_strategic_reserve(randint(1, 6))
    elif choice == "3":
        do_move_panzer_to_strategic_reserve(randint(1,6))
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
    elif choice == "G" or choice == "g":
        print_game_summary()
        print()
        input("Press ENTER to continue...")
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
