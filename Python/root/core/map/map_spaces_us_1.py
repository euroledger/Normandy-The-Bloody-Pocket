from core.map.map_model import MapSpace, TerrainType, falaise_gap
from core.enums import SideType, Nation

us_1_start_box = MapSpace(
    name="1ST US START BOX",
    track=Nation.US_1,
    terrain=TerrainType.START_BOX,
    terrain_value=0,
    track_number=11,
    controlling_player=SideType.ALLIED
)

utah_omaha = MapSpace(
    name="UTAH-OMAHA BEACH",
    track=Nation.US_1,
    terrain=TerrainType.BEACH,
    terrain_value=2,
    track_number=10,
    controlling_player=SideType.ALLIED
)

carentan = MapSpace(
    name="CARENTAN",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=9,
    controlling_player=SideType.GERMAN
)

valognes = MapSpace(
    name="VALOGNES",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=8,
    controlling_player=SideType.GERMAN
)

cherbourg = MapSpace(
    name="CHERBOURG",
    track=Nation.US_1,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=7,
    controlling_player=SideType.GERMAN
)

coutances = MapSpace(
    name="COUTANCES",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=6,
    controlling_player=SideType.GERMAN
)

st_lo = MapSpace(
    name="ST. LO",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=5,
    controlling_player=SideType.GERMAN
)

avranches = MapSpace(
    name="AVRANCHES",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=4,
    controlling_player=SideType.GERMAN
)

mortain = MapSpace(
    name="MORTAIN",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=3,
    controlling_player=SideType.GERMAN
)

flers = MapSpace(
    name="FLERS",
    track=Nation.US_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=2,
    controlling_player=SideType.GERMAN
)

chambois = MapSpace(
    name="CHAMBOIS",
    track=Nation.US_1,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=1,
    controlling_player=SideType.GERMAN
)


us_1_track = [
    us_1_start_box,
    utah_omaha,
    carentan,
    valognes,
    cherbourg,
    coutances,
    st_lo,
    avranches,
    mortain,
    flers,
    chambois,
    falaise_gap
]