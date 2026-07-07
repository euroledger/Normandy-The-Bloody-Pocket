from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY,
    US_THIRD_ARMY,
    US_VIII_CORPS,
    US_XV_CORPS,
)
from core.map.map_spaces_us_1 import us_1_start_box, carentan, us_1_track
from core.map.map_spaces_brit_2 import brit_2_start_box, bayeux, brit_2_track
from core.map.map_spaces_can_1 import can_1_start_box, lebisey_wood, can_1_track
from core.map.map_spaces_us_3 import us_3_start_box, us_viii_track, us_xv_track
from core.enums import ReinforcementType, SideType
from core.map.map_model import (
    in_transit_box,
    strategic_reserve_box,
    eliminated_units_box,
)
from core.global_game_state import GlobalGameState
from core.map.map_model import TerrainType
from core.models import AlliedArmy
from core.german_units import (
    create_flak88,
    create_nebelwerfer,
    PZ_LEHR,
    SS_12,
    SS_1,
    SS_9,
    SS_10,
    SS_2,
    PZ_21,
    PZ_116,
    SS_21_PZGRD,
    PZ_2,
    PZ_9,
)


def add_units_to_space(space, units):
    if not isinstance(units, list):
        units = [units]
    for unit in units:
        space.units.append(unit)
        if isinstance(unit, AlliedArmy):
            unit.location = space


def remove_units_from_space(space, units):
    if not isinstance(units, list):
        units = [units]
    for unit in units:
        if unit in space.units:
            space.units.remove(unit)
            if isinstance(unit, AlliedArmy):
                unit.location = None


def german_defense_strength(space):
    terrain_value = space.terrain_value

    if space.terrain == TerrainType.BOCAGE:
        terrain_value += GlobalGameState.bocage_defense_modifier

    fortified_value = space.fortified_village_modifier
    model_value = space.model_modifier
    unit_strength = sum(unit.combat_value for unit in space.units)

    print()
    print(f"GERMAN DEFENSE: {space.name}")
    print(f"TERRAIN: {terrain_value}")
    print(f"FORTIFIED VILLAGES: {fortified_value}")
    print(f"MODEL: {model_value}")

    for unit in space.units:
        print(f"{unit}: {unit.combat_value}")

    print(f"TOTAL DEFENSE: {terrain_value + fortified_value + model_value + unit_strength}")
    print()

    return terrain_value + fortified_value + model_value + unit_strength


def can_counter_attack(space):
    if space.terrain == TerrainType.BEACH and GlobalGameState.cards_drawn >= 3:
        return False

    return True


def german_attack_strength(space):
    model_value = space.model_modifier

    unit_strength = sum(unit.combat_value for unit in space.units if unit.type != ReinforcementType.FLAK_88)

    print()
    print(f"GERMAN ATTACK: {space.name}")
    print(f"MODEL: {model_value}")

    for unit in space.units:
        if unit.type != ReinforcementType.FLAK_88:
            print(f"{unit}: {unit.combat_value}")

    print(f"TOTAL ATTACK: {model_value + unit_strength}")
    print()

    return model_value + unit_strength


# Some tests reduce combat values - reset them here
def reset_german_panzer_divisions():
    for unit in [PZ_LEHR, SS_12, SS_1, SS_9, SS_10, SS_2, PZ_21, PZ_116, SS_21_PZGRD, PZ_2, PZ_9]:
        unit.combat_value = 2


def reset_map():
    allied_starting_spaces = {
        "1ST US START BOX",
        "UTAH-OMAHA BEACH",
        "2ND BRIT START BOX",
        "GOLD-JUNO-SWORD BEACH (BRITISH TRACK)",
        "1ST CAN START BOX",
        "GOLD-JUNO-SWORD BEACH (CANADIAN TRACK)",
        "3RD US START BOX",
    }

    for track in [us_1_track, can_1_track, brit_2_track, us_viii_track, us_xv_track]:
        for space in track:
            space.units.clear()
            space.fortified_village_modifier = 0
            space.under_siege = False

            if space.name in allied_starting_spaces:
                space.controlling_player = SideType.ALLIED
            else:
                space.controlling_player = SideType.GERMAN


def reset_allied_armies():
    armies = [
        US_FIRST_ARMY,
        BRITISH_SECOND_ARMY,
        CANADIAN_FIRST_ARMY,
        US_VIII_CORPS,
        US_THIRD_ARMY,
    ]

    for army in armies:
        army.location = None
        army.flipped = False
        army.merged = False


def get_all_map_spaces():
    return (
        us_1_track
        + brit_2_track
        + can_1_track
        + us_viii_track
        + us_xv_track
        + [
            in_transit_box,
            strategic_reserve_box,
            eliminated_units_box,
        ]
    )


def clear_all_units_from_map():
    for space in get_all_map_spaces():
        space.units.clear()


def do_opening_setup():
    reset_map()
    reset_german_panzer_divisions()
    reset_allied_armies()
    GlobalGameState.bocage_defense_modifier = 0

    # =========================================================
    # OPENING SETUP - ALLIES
    # =========================================================

    add_units_to_space(us_1_start_box, US_FIRST_ARMY)
    add_units_to_space(brit_2_start_box, BRITISH_SECOND_ARMY)
    add_units_to_space(can_1_start_box, CANADIAN_FIRST_ARMY)
    add_units_to_space(us_3_start_box, [US_THIRD_ARMY, US_VIII_CORPS, US_XV_CORPS])

    # =========================================================
    # OPENING SETUP - GERMANS
    # =========================================================

    add_units_to_space(bayeux, [PZ_21, create_nebelwerfer(), create_nebelwerfer(), create_flak88()])
    add_units_to_space(lebisey_wood, [create_nebelwerfer(), create_nebelwerfer(), create_flak88()])
    add_units_to_space(carentan, [create_nebelwerfer()])
