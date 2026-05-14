from enum import Enum


class ModifierType(Enum):
    ATTACK_STRENGTH = "Attack Strength"
    DEFENSE_STRENGTH = "Defense Strength"
    AIR_POWER = "Air Power"
    REINFORCEMENT = "Reinforcement"
    RESOURCE_GAIN = "Resource Gain"
    RESOURCE_LOSS = "Resource Loss"
    DRM = "DRM"
    COMMANDER = "Commander"
    RETREAT = "Retreat"


class Nation(Enum):
    US_1 = "US FIRST ARMY"
    US_3 = "US THIRD ARMY"
    BRIT_2 = "BRIT SECOND ARMY"
    CAN_1 = "CANADIAN FIRST ARMY"


class ReinforcementType(Enum):
    PZ_DIV = "PANZER"
    MARKER = "MARKER"
    NEBELWERFER = "NEBELWERFER"
    FLAK_88 = "FLAK 88"
    KAMPFGRUPPE = "KAMPFGRUPPE"



class ResourceType(Enum):
    TRANSPORT = "Transport"
    SUPPLY = "Supply"
    HITLER_APPROVAL = "Hitler Approval"
    
# =========================================================
# TERRAIN TYPES
# =========================================================

class TerrainType(Enum):
    BOCAGE = ("Bocage", 2)
    TOWN = ("Town", 1)
    HILL = ("Hill", 2)
    BEACH = ("Beach", 2)
    FORTRESS = ("Fortress", 4)
    FORTIFIED_VILLAGE = ("Fortified Village", 3)
    FALAISE_GAP = ("Falaise Gap", 1)

    def __init__(self, display_name, defense_value):
        self.display_name = display_name
        self.defense_value = defense_value
    
