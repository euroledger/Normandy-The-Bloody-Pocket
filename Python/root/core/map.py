from dataclasses import dataclass

from core.models import AlliedArmy
from core.enums import TerrainType


# =========================================================
# BASE LOCATION
# =========================================================

@dataclass
class Location:
    name: str


# =========================================================
# START BOX
# =========================================================

@dataclass
class StartBox(Location):
    army: AlliedArmy


# =========================================================
# MAP SPACE
# =========================================================

@dataclass
class MapSpace(Location):
    army: AlliedArmy
    terrain: TerrainType
    position: int