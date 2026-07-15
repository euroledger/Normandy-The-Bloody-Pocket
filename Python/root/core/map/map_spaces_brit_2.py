from core.map.map_model import MapSpace, TerrainType, falaise_gap
from core.enums import SideType, Nation

brit_2_start_box = MapSpace(
    name="2ND BRIT START BOX",
    track=Nation.BRIT_2,
    terrain=TerrainType.START_BOX,
    terrain_value=0,
    track_number=7,
    controlling_player=SideType.ALLIED,
)

gold_juno_sword_brit = MapSpace(
    name="GOLD-JUNO-SWORD BEACH (BRITISH TRACK)",
    track=Nation.BRIT_2,
    terrain=TerrainType.BEACH,
    terrain_value=2,
    track_number=6,
    controlling_player=SideType.ALLIED,
)

bayeux = MapSpace(
    name="BAYEUX",
    track=Nation.BRIT_2,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=5,
    controlling_player=SideType.GERMAN,
)

tilly = MapSpace(
    name="TILLY",
    track=Nation.BRIT_2,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=4,
    controlling_player=SideType.GERMAN,
)
villers_bocage = MapSpace(
    name="VILLERS-BOCAGE",
    track=Nation.BRIT_2,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=3,
    controlling_player=SideType.GERMAN,
)

mont_pincon = MapSpace(
    name="MONT PINCON",
    track=Nation.BRIT_2,
    terrain=TerrainType.HILL,
    terrain_value=2,
    track_number=2,
    controlling_player=SideType.GERMAN,
)

thury_harcourt = MapSpace(
    name="THURY HARCOURT",
    track=Nation.BRIT_2,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=1,
    controlling_player=SideType.GERMAN,
)

brit_2_track = [
    brit_2_start_box,
    gold_juno_sword_brit,
    bayeux,
    tilly,
    villers_bocage,
    mont_pincon,
    thury_harcourt,
    falaise_gap,
]
