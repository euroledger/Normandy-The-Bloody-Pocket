from dataclasses import dataclass
from enum import Enum


# =========================================================
# WEATHER TYPES
# =========================================================

class WeatherType(Enum):
    OVERCAST = "Overcast"
    PARTLY_CLEAR = "Partly Clear"
    CLEAR = "Clear"

ALL_JABOS_AVAILABLE = 999
CARPET_BOMBING_UNAVAILABLE = -999

# =========================================================
# WEATHER RESULT
# =========================================================

@dataclass
class WeatherResult:

    weather_type: WeatherType
    available_jabos: int 
    resource_drm: int
    carpet_bombing_drm: int


# =========================================================
# WEATHER TABLE
# =========================================================

def get_weather_result(die_roll: int) -> WeatherResult:
    return WEATHER_TABLE[die_roll]


WEATHER_TABLE = {
    1: WeatherResult(
        weather_type=WeatherType.OVERCAST,
        available_jabos=0,
        resource_drm=1,
        carpet_bombing_drm=CARPET_BOMBING_UNAVAILABLE
    ),

    2: WeatherResult(
        weather_type=WeatherType.PARTLY_CLEAR,
        available_jabos=1,
        resource_drm=0,
        carpet_bombing_drm=1
    ),

    3: WeatherResult(
        weather_type=WeatherType.PARTLY_CLEAR,
        available_jabos=1,
        resource_drm=0,
        carpet_bombing_drm=1
    ),

    4: WeatherResult(
        weather_type=WeatherType.CLEAR,
        available_jabos=ALL_JABOS_AVAILABLE,
        resource_drm=0,
        carpet_bombing_drm=0
    ),

    5: WeatherResult(
        weather_type=WeatherType.CLEAR,
        available_jabos=ALL_JABOS_AVAILABLE,
        resource_drm=0,
        carpet_bombing_drm=0
    ),

    6: WeatherResult(
        weather_type=WeatherType.CLEAR,
        available_jabos=ALL_JABOS_AVAILABLE,
        resource_drm=0,
        carpet_bombing_drm=0
    )
}