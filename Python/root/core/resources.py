from core.actions.strategic_reserve_actions import do_move_other_unit_from_strategic_reserve, get_other_units_in_strategic_reserve
from core.enums import ModifierType, ReinforcementType, ResourceType
from core.global_game_state import GlobalGameState
from core.map.map_model import (
    hitler_approval_track,
    in_transit_box,
    strategic_reserve_box,
    supply_track,
    transport_track,
)
from core.models import Card
from core.tables.weather import WeatherType


def do_event(card: Card):
    print()
    print("EVENT")
    card.event()
    
    
def do_resource_phase_adjustments(card):
    print()
    print("RESOURCE ADJUSTMENTS")

    for effect in card.resources.effects:
        if effect.modifier_type not in (
            ModifierType.RESOURCE_LOSS,
            ModifierType.RESOURCE_GAIN,
        ):
            continue

        action = "GAIN" if effect.value > 0 else "LOSE"

        if effect.resource_type == ResourceType.HITLER_APPROVAL:
            old_value = hitler_approval_track.value
            hitler_approval_track.value = max(-2, min(6, hitler_approval_track.value + effect.value))
            print(f"Hitler Approval: {action} {abs(effect.value)} ({old_value} -> {hitler_approval_track.value})")

        elif effect.resource_type == ResourceType.SUPPLY:
            old_value = supply_track.value
            supply_track.value = max(0, min(6, supply_track.value + effect.value))
            print(f"Supply: {action} {abs(effect.value)} ({old_value} -> {supply_track.value})")

        elif effect.resource_type == ResourceType.TRANSPORT:
            old_value = transport_track.value
            transport_track.value = max(0, min(6, transport_track.value + effect.value))
            print(f"Transport: {action} {abs(effect.value)} ({old_value} -> {transport_track.value})")


def do_resource_phase_drms(weather_type, card):

    # 1. SET RESOURCE ROLL DRMs
    if weather_type == WeatherType.OVERCAST:
        GlobalGameState.supply_roll_drm = 1
        GlobalGameState.transport_roll_drm = 1
    else:
        GlobalGameState.supply_roll_drm = 0
        GlobalGameState.transport_roll_drm = 0

    # 2. SET EVENT CARD DRMs
    GlobalGameState.transport_check_drm = 0
    GlobalGameState.supply_check_drm = 0
    GlobalGameState.hitler_approval_check_drm = 0

    for effect in card.resources.effects:
        if effect.modifier_type != ModifierType.DRM:
            continue
        if effect.resource_type == ResourceType.TRANSPORT:
            GlobalGameState.transport_check_drm += effect.value
        elif effect.resource_type == ResourceType.SUPPLY:
            GlobalGameState.supply_check_drm += effect.value
        elif effect.resource_type == ResourceType.HITLER_APPROVAL:
            GlobalGameState.hitler_approval_check_drm += effect.value

    
def do_resource_phase_reinforcements(card):
    print()
    print("========================================")
    print("REINFORCEMENTS")
    print("========================================")
    print()
    reinforcements = card.reinforcements()
    if not reinforcements:
        print("NONE")
        return
    for unit, _ in reinforcements:
        if unit.type == ReinforcementType.PZ_DIV:
            in_transit_box.units.append(unit)
            print(f"{unit} -> IN TRANSIT")
        else:
            strategic_reserve_box.units.append(unit)
            print(f"{unit} -> STRATEGIC RESERVE")
            

        for effect in card.actions.effects:
            if effect.modifier_type == ModifierType.COMMANDER and effect.label and effect.target is None:
                print(f"{effect.label} -> STRATEGIC RESERVE")

    print()
    
    


# If the die roll is > base level for that resource, increase the resource level by one
# up to its maximum
def do_resource_roll(track, die_roll, drm=0):
    # die_roll = randint(1, 6)
    modified_roll = die_roll + drm

    print(f"{track.name} RESOURCE ROLL")
    print(f"ROLL: {die_roll}")

    if drm != 0:
        print(f"DRM: {drm:+}")

    print(f"MODIFIED ROLL: {modified_roll}")
    print(f"BASE LEVEL: {track.base_level}")

    if modified_roll > track.base_level:
        old_value = track.value

        track.value = min(track.value + 1, track.maximum)

        print(f"RESULT: {old_value} -> {track.value}")

    else:
        print("RESULT: NO CHANGE")
