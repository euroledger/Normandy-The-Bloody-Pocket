from core.map.map_model import MapSpace, TerrainType, falaise_gap
from core.enums import SideType, Nation

can_1_start_box = MapSpace(
    name="1ST CAN START BOX",
    track=Nation.CAN_1,
    terrain=TerrainType.START_BOX,
    terrain_value=0,
    track_number=7,
    controlling_player=SideType.ALLIED,
)

gold_juno_sword_can = MapSpace(
    name="GOLD-JUNO-SWORD BEACH (CANADIAN TRACK)",
    track=Nation.CAN_1,
    terrain=TerrainType.BEACH,
    terrain_value=2,
    track_number=6,
    controlling_player=SideType.ALLIED,
)

lebisey_wood = MapSpace(
    name="LEBISEY WOOD",
    track=Nation.CAN_1,
    terrain=TerrainType.BOCAGE,
    terrain_value=2,
    track_number=5,
    controlling_player=SideType.GERMAN,
)

caen = MapSpace(
    name="CAEN",
    track=Nation.CAN_1,
    terrain=TerrainType.FORTRESS,
    terrain_value=4,
    track_number=4,
    controlling_player=SideType.GERMAN,
    fortified=True,
)

cagny = MapSpace(
    name="CAGNY",
    track=Nation.CAN_1,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=3,
    controlling_player=SideType.GERMAN,
)

bourguebus_ridge = MapSpace(
    name="BOURGUEBUS RIDGE",
    track=Nation.CAN_1,
    terrain=TerrainType.HILL,
    terrain_value=2,
    track_number=2,
    controlling_player=SideType.GERMAN,
)

falaise = MapSpace(
    name="FALAISE",
    track=Nation.CAN_1,
    terrain=TerrainType.TOWN,
    terrain_value=1,
    track_number=1,
    controlling_player=SideType.GERMAN,
)


can_1_track = [can_1_start_box, gold_juno_sword_can, lebisey_wood, caen, cagny, bourguebus_ridge, falaise, falaise_gap]
