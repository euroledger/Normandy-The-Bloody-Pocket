from core.card_utilities import get_armies_as_objects
from random import randint
from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY,
    US_THIRD_ARMY,
    US_VIII_CORPS,
    US_XV_CORPS,
)
from core.carpet_bombing import ATTACK_CANCELLED, get_carpet_bombing_result
from core.map.map_model import TerrainType, eliminated_units_box, hitler_approval_track
from core.card_utilities import calculate_attack_modifiers
from core.map.map_utilities import german_defense_strength
from random import choice
from core.global_game_state import GlobalGameState
from core.map.map_utilities import update_front_line_for_army
from core.models import GermanUnit, Strategy
from core.enums import Nation, SideType
from core.map.map_spaces_us_1 import us_1_track
from core.map.map_spaces_brit_2 import brit_2_track
from core.map.map_spaces_can_1 import can_1_track
from core.map.map_spaces_us_3 import us_viii_track, us_xv_track
from core.siege import calculate_siege_drm, get_siege_result


def get_track_for(army):
    if army.nation == Nation.US_1:
        track = us_1_track
    elif army.nation == Nation.BRIT_2:
        track = brit_2_track
    elif army.nation == Nation.CAN_1:
        track = can_1_track
    elif army.nation == Nation.US_3:
        track = us_viii_track
    elif army.nation == Nation.US_VIII:
        track = us_viii_track
    elif army.nation == Nation.US_XV:
        track = us_xv_track
    else:
        raise ValueError(f"Unknown army nation: {army.nation}")
    return track


def get_front_line_space(army):
    track = get_track_for(army)

    if army == US_FIRST_ARMY:
        front_line = GlobalGameState.us_1_front_line
    elif army == BRITISH_SECOND_ARMY:
        front_line = GlobalGameState.brit_2_front_line
    elif army == CANADIAN_FIRST_ARMY:
        front_line = GlobalGameState.can_1_front_line
    elif army == US_THIRD_ARMY:
        front_line = GlobalGameState.us_3_front_line
    elif army == US_VIII_CORPS:
        front_line = GlobalGameState.us_viii_front_line
    elif army == US_XV_CORPS:
        front_line = GlobalGameState.us_xv_front_line
    else:
        raise ValueError(f"Unknown army: {army}")

    return next(space for space in track if space.track_number == front_line)


def advance_army_one_space(army):
    track = get_track_for(army)
    current_space = army.location

    next_space = next((space for space in track if space.track_number == current_space.track_number - 1), None)

    if next_space is None:
        return

    current_space.units.remove(army)
    next_space.units.append(army)
    army.location = next_space

    if hasattr(next_space, "controlling_player"):
        next_space.controlling_player = SideType.ALLIED

    update_front_line_for_army(army, next_space.track_number)

    print(f"\nAFTER AUTO ADVANCE -> ALLIED ARMY LOCATION:{army.name} IS AT {army.location.name}")


def dday_landings_first_wave():
    print()
    print("D-DAY LANDINGS FIRST WAVE")
    print("=========================")
    print()

    for army, target_roll in [(US_FIRST_ARMY, 3), (BRITISH_SECOND_ARMY, 2), (CANADIAN_FIRST_ARMY, 2)]:
        roll = randint(1, 6)
        print(f"{army.display_name}")
        print(f"ROLL: {roll}")
        if roll >= target_roll:
            advance_army_one_space(army)
            print(f"SUCCESS -> {army.location.name}")
        else:
            print(f"FAILURE -> {army.location.name}")
        print()


def dday_landings_second_wave(card, weather):
    print()
    print("D-DAY LANDINGS SECOND WAVE")
    print("==========================")
    print()

    all_armies = [US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY]
    attacking_armies = []

    for army in all_armies:
        if army.location.terrain == TerrainType.START_BOX:
            advance_army_one_space(army)
            print(f"{army.display_name} -> {army.location.name}")
        else:
            attacking_armies.append(army)

    if attacking_armies:
        do_allied_attacks(attacking_armies, card, weather)


def do_german_losses(space, selected_units=None):
    panzer_present_before_losses = any(isinstance(unit, GermanUnit) and unit.is_panzer() for unit in space.units)

    if selected_units is None:
        german_units = space.units
    else:
        german_units = selected_units

    if not german_units:
        print("NO UNITS IN SPACE - NO LOSSES")
        return

    if panzer_present_before_losses:
        hitler_approval_track.value = max(0, hitler_approval_track.value - 1)
        print(f"HITLER APPROVAL -1 → {hitler_approval_track.value}")

    print()
    print("GERMAN LOSSES")
    print("=============")

    print(">>>> GlobalGameState.german_casualty_strategy=", GlobalGameState.german_casualty_strategy)
    if GlobalGameState.german_casualty_strategy == Strategy.HUMAN:
        for i, unit in enumerate(german_units, start=1):
            print(f"{i}. {unit} ({unit.combat_value})")

        selection = int(input("Select unit to take loss: "))
        casualty = german_units[selection - 1]
    elif GlobalGameState.german_casualty_strategy == Strategy.UNIT_TEST:
        # Always take first unit in list as loss for unit tests
        casualty = german_units[0]
    elif GlobalGameState.german_casualty_strategy == Strategy.RANDOM:
        casualty = choice(german_units)

    else:
        raise ValueError(
            f"Strategy.HUMAN={Strategy.HUMAN} Unknown strategy: {GlobalGameState.german_casualty_strategy}"
        )

    if casualty.combat_value > 1:
        casualty.combat_value -= 1
        print(f"REDUCED: {casualty} now {casualty.combat_value}")
    else:
        space.units.remove(casualty)
        eliminated_units_box.units.append(casualty)
        print(f"ELIMINATED: {casualty}")


def retreat_german_units(space, track):
    retreat_space = next((s for s in track if s.track_number == space.track_number - 1), None)

    if retreat_space is None:
        print("NO RETREAT POSSIBLE")
        return

    retreating_units = list(space.units)

    for unit in retreating_units:
        space.units.remove(unit)
        retreat_space.units.append(unit)

    print(f"GERMANS RETREAT FROM {space.name} TO {retreat_space.name}")


def do_allied_victory(army, target_space):
    print("ALLIED VICTORY")
    do_german_losses(target_space)
    track = get_track_for(army)
    if target_space.units:
        retreat_german_units(target_space, track)
    else:
        print("<<SPACE CLEARED>>")

    advance_army_one_space(army)


def get_carpet_bombing_modifier(card, weather, die_roll=None):
    if not card.air_power.has_carpet_bombing():
        return 0
    if weather.available_jabos == 0:
        return 0
    actual_die_roll = die_roll if die_roll is not None else randint(1, 6)
    result = get_carpet_bombing_result(die_roll=actual_die_roll, drm=weather.carpet_bombing_drm)

    if result.attack_modifier == ATTACK_CANCELLED:
        return 0

    return result.attack_modifier


def do_siege_roll(space, army, card, weather, carpet_bombing, defense_strength, die_roll=None):
    print()
    print("========================================")
    print(f"{army.name} - SIEGE ROLL")
    print("========================================")
    print()
    siege_roll = die_roll if die_roll is not None else randint(1, 6)
    modified_roll = siege_roll

    result = calculate_attack_modifiers(
        card=card, army=army, num_jabos=weather.available_jabos, carpet_bombing=carpet_bombing
    )
    attack_strength = result["attack_strength"]
    has_air_support = result["has_air_support"]

    drm_result = calculate_siege_drm(
        attack_strength=attack_strength, defense_strength=defense_strength, has_air_support=has_air_support
    )
    modified_roll += drm_result.drm

    # =====================================================
    # DISPLAY DRMS
    # =====================================================
    print(f"DEFENSE-ATTACK DIFFERENTIAL: {defense_strength - attack_strength}")
    for reason in drm_result.reasons:
        print(f"DRM: {reason}")

    modified_roll = max(1, min(6, modified_roll))
    siege_result = get_siege_result(modified_roll)

    print()
    print(f"BASE ROLL: {siege_roll}")
    print(f"MODIFIED ROLL: {modified_roll}")
    print()
    print(f"RESULT: {siege_result.result_type.value}")

    # =====================================================
    # APPLY COMBAT STEP LOSSES
    # =====================================================
    if siege_result.combat_steps_eliminated > 0:
        steps_elim = min(defense_strength - 4, siege_result.combat_steps_eliminated)
        print(f"COMBAT STEPS ELIMINATED: {steps_elim}")

        for _ in range(steps_elim):
            do_german_losses(space)

    # =====================================================
    # SPACE CAPTURED
    # =====================================================
    if siege_result.space_captured:
        space.under_siege = False
        do_allied_victory(army, space)


# def do_allied_attacks(armies, card, weather, die_roll=None):
def do_allied_attacks(armies, card, weather, carpet_bombing=0, die_roll=None):
    print()
    print("ALLIED ATTACKS")
    print("==============")
    print()

    for army in armies:
        if army.location.terrain == TerrainType.START_BOX:
            advance_army_one_space(army)
            print(f"{army.display_name} -> {army.location.name}")
            continue

        target_space = next(
            (space for space in get_track_for(army) if space.track_number == army.location.track_number - 1), None
        )

        if target_space is None:
            raise ValueError(f"No target space for: {army.name}")

        attack_result = calculate_attack_modifiers(card, army, weather.available_jabos)
        attack_strength = attack_result["attack_strength"]
        defense_strength = german_defense_strength(target_space)

        actual_die_roll = die_roll if die_roll is not None else randint(1, 6)
        attack_total = attack_strength + actual_die_roll

        print(f"{army.display_name}")
        print(f"TARGET: {target_space.name}")
        print(f"ATTACK STRENGTH: {attack_strength}")
        print(f"DEFENSE STRENGTH: {defense_strength}")
        print(f"DIE ROLL: {actual_die_roll}")
        print(f"ATTACK TOTAL: {attack_total}")
        print()

        # Once a fortress is under siege it remains under siege until:
        # 1. The fortress falls, or
        # 2. The besieging Allied army is forced to retreat.
        if target_space.under_siege or (
            defense_strength - attack_strength >= 6 and target_space.terrain == TerrainType.FORTRESS
        ):
            target_space.under_siege = True
            do_siege_roll(
                space=target_space,
                army=army,
                card=card,
                weather=weather,
                carpet_bombing=carpet_bombing,
                defense_strength=defense_strength,
                die_roll=actual_die_roll,
            )
            continue
        if actual_die_roll == 6:
            do_allied_victory(army, target_space)

        elif actual_die_roll == 1:
            print("ALLIED DEFEAT")

        elif attack_total > defense_strength:
            do_allied_victory(army, target_space)

        else:
            print("ALLIED DEFEAT")


def do_military_phase(card, weather):
    print()
    print("========================================")
    print("MILITARY PHASE")
    print("========================================")
    print()

    if card.card_id == 1:
        dday_landings_first_wave()
        return

    if card.card_id == 2:
        dday_landings_second_wave(card, weather)
        return

    armies = get_armies_as_objects(card)

    if not armies:
        print("NO ATTACKING ARMIES")
        return

    print("ATTACKING ARMIES")

    for army in armies:
        print(f" - {army}")

    carpet_bombing = get_carpet_bombing_modifier(card, weather)
    do_allied_attacks(armies, card, weather, carpet_bombing)
