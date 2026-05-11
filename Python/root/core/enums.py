from enum import Enum


class ModifierType(Enum):
    ATTACK_STRENGTH = "Attack Strength"
    DEFENSE_STRENGTH = "Defense Strength"
    AIR_POWER = "Air Power"
    REINFORCEMENT = "Reinforcement"
    RESOURCE_GAIN = "Resource Gain"
    RESOURCE_LOSS = "Resource Loss"
    RETREAT = "Retreat"
    DRM = "DRM"
    COMMANDER = "Commander"


class Nation(Enum):
    US_1 = "US FIRST ARMY"
    US_3 = "US THIRD ARMY"
    BRIT_2 = "BRIT SECOND ARMY"
    CAN_1 = "CANADIAN FIRST ARMY"


class ReinforcementType(Enum):
    PZ_DIV = "PANZER"
    MARKER = "MARKER"



class ResourceType(Enum):
    TRANSPORT = "Transport"
    SUPPLY = "Supply"
    HITLER_APPROVAL = "Hitler Approval"