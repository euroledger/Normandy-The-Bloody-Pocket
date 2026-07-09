from random import randint

from core.card_utilities import calculate_defense_modifiers, get_all_defending_armies
from core.enums import ReinforcementType
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    in_transit_box,
    strategic_reserve_box,
    transport_track,
    hitler_approval_track,
    supply_track,
    TerrainType,
)
from core.map.map_utilities import (
    can_counter_attack,
    calculate_german_attack_strength,
    get_eligible_german_units,
    update_front_line_for_army,
)
from core.military import get_front_line_space, get_track_for, do_german_losses
from core.models import GermanUnit


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


def choose_attacking_units(units):
    selected = list(units)  # default: all selected

    while True:
        print("\nSELECT ATTACKING UNITS (number of unit to toggle, X=Participating)")
        print("Press ENTER to confirm\n")

        for i, unit in enumerate(units, start=1):
            marker = "[X]" if unit in selected else "[ ]"
            print(f"{i}. {marker} {unit} ({unit.combat_value})")

        choice = input("Choice: ").strip()

        if choice == "":
            break

        if not choice.isdigit():
            continue

        idx = int(choice) - 1
        if 0 <= idx < len(units):
            unit = units[idx]
            if unit in selected:
                selected.remove(unit)
            else:
                selected.append(unit)

    return list(selected)


def get_german_space_facing_front_line(army):
    track = get_track_for(army)
    front_line_space = get_front_line_space(army)

    return next(space for space in track if space.track_number == front_line_space.track_number - 1)


def get_counter_attack_options():
    options = []

    for army in get_all_defending_armies():

        if army.name in GlobalGameState.counter_attacked_armies:
            continue

        target_space = get_front_line_space(army)

        if not can_counter_attack(target_space):
            continue

        track = get_track_for(army)
        attacking_space = next((space for space in track if space.track_number == target_space.track_number - 1), None)

        if attacking_space is None:
            continue

        # attack = german_attack_strength(attacking_space)
        eligible = get_eligible_german_units(attacking_space)
        # selected = choose_attacking_units(eligible)

        attack = calculate_german_attack_strength(attacking_space, eligible)
        defense = calculate_defense_modifiers(
            card=GlobalGameState.current_card,
            army=army,
            weather=GlobalGameState.current_weather,
        )["defense_strength"]

        options.append(
            {
                "army": army,
                "target_space": target_space,
                "attacking_space": attacking_space,
                "german_attack": attack,
                "allied_defense": defense,
            }
        )

    return options


def print_counter_attack_options(options):
    RED = "\033[31m"  # bright red
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print()
    print(f"{BOLD}{RED}COUNTER-ATTACK OPTIONS{RESET}")
    print(f"{RED}0. Return to main menu{RESET}")

    for index, option in enumerate(options, start=1):
        print(
            f"{RED}{index}. {option['army'].name} at "
            f"{option['target_space'].name} "
            f"({option['german_attack']} attack from "
            f"{option['attacking_space'].name} vs "
            f"{option['allied_defense']} defense){RESET}"
        )


def choose_counter_attack_option(options):
    while True:
        choice = input("Choose counter-attack target: ")

        if choice == "0":
            return None

        if not choice.isdigit():
            print("INVALID CHOICE")
            continue

        choice_index = int(choice) - 1

        if 0 <= choice_index < len(options):
            return options[choice_index]

        print("INVALID CHOICE")


def resolve_counter_attack(attack, defense, selected_units, die_roll):
    print()
    print("RESOLVING COUNTER-ATTACK")
    print(f"Attack Strength: {attack}")
    print(f"Defense Strength: {defense}")
    print(f"Die Roll: {die_roll}")

    # --- Supply consumption (ANY Panzer unit) ---
    panzer_used = any(isinstance(unit, GermanUnit) and unit.is_panzer() for unit in selected_units)

    if panzer_used:
        supply_track.value -= 1
        print("SUPPLY -1 (Attacking Panzer Unit)")

    # --- Resolution ---
    if die_roll == 6:
        result = "WIN"
        print("Natural 6 → AUTOMATIC GERMAN WIN")

    elif die_roll == 1:
        result = "LOSS"
        print("Natural 1 → AUTOMATIC GERMAN LOSS")

    else:
        total = attack + die_roll
        print(f"Modified Total: {attack} + {die_roll} = {total}")

        if total > defense:
            result = "WIN"
            print("Result: GERMAN WIN")
        else:
            result = "LOSS"
            print("Result: GERMAN LOSS")

    print()

    return {
        "result": result,
        "attack_total": attack + die_roll,
        "defense": defense,
        "natural_roll": die_roll,
    }


def do_post_combat(result, selected_option, selected_units):

    army = selected_option["army"]
    target_space = selected_option["target_space"]
    attacking_space = selected_option["attacking_space"]

    print()
    print("POST-COMBAT")
    print("===========")

    if result["result"] == "WIN":
        print("GERMAN VICTORY")

        # --- Allied Retreat ---
        # track = get_track_for(army)
        # current_space = army.location

        # retreat_space = next(
        #     (s for s in track if s.track_number == current_space.track_number + 1),
        #     None
        # )
        track = get_track_for(army)
        current_space = army.location

        try:
            idx = track.index(current_space)
            retreat_space = track[idx - 1] if idx > 0 else None
        except ValueError:
            retreat_space = None

        if retreat_space:
            current_space.units.remove(army)
            retreat_space.units.append(army)
            army.location = retreat_space

            update_front_line_for_army(army, retreat_space.track_number)

            print(f"{army.name} RETREATS TO {retreat_space.name}")
        else:
            print("NO RETREAT POSSIBLE")

        # --- German Advance (ONLY selected units) ---
        if (
            target_space.terrain != TerrainType.BEACH
            and target_space.terrain != TerrainType.FORTRESS
            and target_space != TerrainType.START_BOX
        ):
            for unit in selected_units:
                if unit in attacking_space.units:
                    attacking_space.units.remove(unit)
                    target_space.units.append(unit)

            print(f"GERMANS ADVANCE INTO {target_space.name}")
        else:
            print("GERMANS DO NOT ADVANCE INTO BEACH SPACE OR FORTRESS")

        # --- Hitler Approval +1 (max 6) ---
        if hitler_approval_track.value < 6:
            hitler_approval_track.value += 1
            print(f"HITLER APPROVAL +1 → {hitler_approval_track.value}")
        else:
            print("HITLER APPROVAL ALREADY AT MAX (6)")

    else:
        print("GERMAN DEFEAT")

        # --- Apply 1 step loss if units attacking ---
        if selected_units:
            do_german_losses(attacking_space, selected_units)
        else:
            print("NO GERMAN UNITS ENGAGED - NO LOSSES APPLIED")


def do_counter_attack():
    options = get_counter_attack_options()

    if not options:
        print("NO VALID COUNTER-ATTACK TARGETS")
        return

    print_counter_attack_options(options)

    selected_option = choose_counter_attack_option(options)

    if selected_option is None:
        return

    GlobalGameState.counter_attacked_armies.add(selected_option["army"].name)

    # ✅ NOW choose units (only for chosen attack)
    eligible = get_eligible_german_units(selected_option["attacking_space"])
    selected_units = choose_attacking_units(eligible)

    attack = calculate_german_attack_strength(selected_option["attacking_space"], selected_units)
    defense = selected_option["allied_defense"]

    GlobalGameState.actions_left_this_turn -= 1

    print(f"COUNTER-ATTACK: {selected_option['army'].name} at {selected_option['target_space'].name}")
    print(f"Final attack strength: {attack} vs defense: {defense}")

    # resolution continues...
    result = resolve_counter_attack(
        attack=attack, defense=defense, selected_units=selected_units, die_roll=randint(1, 6)
    )
    do_post_combat(result, selected_option, selected_units)


def do_move_panzer_from_strategic_reserve():
    print("MOVE PANZER DIVISION FROM STRATEGIC RESERVE")
    GlobalGameState.actions_left_this_turn -= 1


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
