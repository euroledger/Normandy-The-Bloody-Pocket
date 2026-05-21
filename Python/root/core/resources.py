from random import randint

from core.enums import ModifierType, ResourceType
from core.global_game_state import GlobalGameState
from core.weather import WeatherType

def do_resource_phase(weather_type, card):
    
    # 1. SET RESOURCE ROLL DRMs
    print(f"RESOURCE PHASE weather={weather_type}\n")
    
    if (weather_type == WeatherType.OVERCAST):
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
        if (effect.modifier_type != ModifierType.DRM):
            continue
        if (effect.resource_type == ResourceType.TRANSPORT):
            GlobalGameState.transport_check_drm += effect.value
        elif (effect.resource_type == ResourceType.SUPPLY):
            GlobalGameState.supply_check_drm += effect.value
        elif (effect.resource_type == ResourceType.HITLER_APPROVAL):
            GlobalGameState.hitler_approval_check_drm += effect.value
        
    
    
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

        track.value = min(
            track.value + 1,
            track.maximum
        )

        print(f"RESULT: {old_value} -> {track.value}")

    else:
        print("RESULT: NO CHANGE")
    