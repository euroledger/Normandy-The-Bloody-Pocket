from core.map.map_model import MapSpace, TerrainType, falaise_gap
from core.enums import SideType, Nation

st_malo = MapSpace(
    name="ST. MALO",
    track=Nation.US_3,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=7,
    controlling_player=SideType.GERMAN
)

brest = MapSpace(
    name="BREST",
    track=Nation.US_3,
    terrain=TerrainType.FORTRESS,
    terrain_value=4,
    track_number=6,
    controlling_player=SideType.GERMAN,
    fortified=True
)

lorient = MapSpace(
    name="LORIENT",
    track=Nation.US_3,
    terrain=TerrainType.FORTRESS,
    terrain_value=4,
    track_number=5,
    controlling_player=SideType.GERMAN,
    fortified=True
)

rennes = MapSpace(
    name="RENNES",
    track=Nation.US_3,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=4,
    controlling_player=SideType.GERMAN
)

le_mans = MapSpace(
    name="LE MANS",
    track=Nation.US_3,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=3,
    controlling_player=SideType.GERMAN
)

alencon = MapSpace(
    name="ALENCON",
    track=Nation.US_3,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=2,
    controlling_player=SideType.GERMAN
)

argentan = MapSpace(
    name="ARGENTAN",
    track=Nation.US_3,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=1,
    controlling_player=SideType.GERMAN
)

us_viii_track = [
    st_malo,
    brest,
    lorient,
    rennes
]

us_xv_track = [
    rennes,
    le_mans,
    alencon,
    argentan,
    falaise_gap
]