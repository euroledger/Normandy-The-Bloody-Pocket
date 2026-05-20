from dataclasses import dataclass, field
from enum import Enum
from typing import List
from core.models import AlliedArmy, UnitBox
from core.enums import SideType

class TerrainType(Enum):
    BEACH = "Beach"
    BOCAGE = "Bocage"
    TOWN = "Town"
    HILL = "Hill"
    FORTRESS = "Fortress"
    FALAISE_GAP = "Falaise Gap"
    START_BOX = "Start Box"
    
@dataclass
class MapSpace:
    name: str
    track: AlliedArmy
    terrain: TerrainType
    controlling_player: SideType
    terrain_value: int = 0
    track_number: int = 0
    fortified: bool = False
    under_siege: bool = False
    units: list = field(default_factory=list)
  
@dataclass
class Track:
    name: str
    spaces: list[MapSpace]
    
from dataclasses import dataclass


@dataclass
class ResourceTrack:
    name: str
    value: int
    base_level: int
    minimum: int
    maximum: int
    
transport_track = ResourceTrack(
    name="Transport",
    value=5,
    base_level=3,
    minimum=0,
    maximum=6
)

supply_track = ResourceTrack(
    name="Supply",
    value=4,
    base_level=3,
    minimum=0,
    maximum=6
)

hitler_approval_track = ResourceTrack(
    name="Hitler Approval",
    value=6,
    base_level=3,
    minimum=-2,
    maximum=6
)

falaise_gap = MapSpace(
    name="FALAISE GAP",
    track=None,
    terrain=TerrainType.FALAISE_GAP,
    terrain_value=1,
    track_number=0,
    controlling_player=SideType.GERMAN
)

in_transit_box = UnitBox(
    name="IN TRANSIT"
)

strategic_reserve_box = UnitBox(
    name="STRATEGIC RESERVE"
)

eliminated_units_box = UnitBox(
    name="ELIMINATED UNITS"
)