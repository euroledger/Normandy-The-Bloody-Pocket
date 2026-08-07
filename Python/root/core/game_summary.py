# core/game_summary.py

from core.global_game_state import GlobalGameState
from core.map.map_spaces_us_1 import us_1_track
from core.map.map_spaces_brit_2 import brit_2_track
from core.map.map_spaces_can_1 import can_1_track
from core.map.map_spaces_us_3 import us_viii_track, us_xv_track
from core.map.map_model import in_transit_box, strategic_reserve_box, eliminated_units_box
from core.map.map_model import transport_track, supply_track, hitler_approval_track
from collections import Counter

def format_eliminated_units(units):
    counts = Counter(unit.name for unit in units)

    result = []

    for name, count in counts.items():
        if name in ["Nebelwerfer", "Flak 88", "Kampfgruppe"]:
            result.append(name if count == 1 else f"{name} (x{count})")
        else:
            result.append(name)

    return ", ".join(result)

def print_game_summary():
    print("\n================================================")
    print("GAME SUMMARY")
    print("================================================")
    print()
    print(f"TURNS COMPLETED: {GlobalGameState.cards_drawn}")
    print("\nALLIED ARMIES")

    all_tracks = [us_1_track, brit_2_track, can_1_track, us_viii_track, us_xv_track]
    printed_spaces = set()
    for track in all_tracks:
        for space in track:
            if space.name in printed_spaces:
                continue

            printed_spaces.add(space.name)
            allied_units = [unit for unit in space.units if hasattr(unit, "nation")]
            if allied_units:
                # print(f"{space.name:<25} {', '.join(str(unit) for unit in allied_units)}")
                print(
                    f"{space.name:<25} {', '.join(f'{unit.display_name} ({unit.strength})' for unit in allied_units)}"
                )

    print("\nGERMAN UNITS")

    printed_spaces = set()

    for track in all_tracks:
        for space in track:
            if space.name in printed_spaces:
                continue

            printed_spaces.add(space.name)
            german_units = [unit for unit in space.units if not hasattr(unit, "nation")]
            if german_units:
                unit_text = ", ".join(f"{unit} ({unit.combat_value})" for unit in german_units)
                print(f"{space.name:<25} {unit_text}")

    print("\nIN TRANSIT")

    if in_transit_box.units:
        print(", ".join(str(unit) for unit in in_transit_box.units))
    else:
        print("EMPTY")

    print("\nSTRATEGIC RESERVE")

    if strategic_reserve_box.units:
        print(", ".join(str(unit) for unit in strategic_reserve_box.units))
    else:
        print("EMPTY")

    print("\nELIMINATED UNITS")

    # if eliminated_units_box.units:
    #     print(", ".join(str(unit) for unit in eliminated_units_box.units))
    # else:
    #     print("EMPTY")
    if eliminated_units_box.units:
        print(format_eliminated_units(eliminated_units_box.units))
    else:
        print("EMPTY")

    print("\nRESOURCE TRACKS")

    print(f"Transport:        {transport_track.value}")
    print(f"Supply:           {supply_track.value}")
    print(f"Hitler Approval:  {hitler_approval_track.value}")

    print("================================================")
