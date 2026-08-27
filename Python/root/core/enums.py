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


class SideType(Enum):
    ALLIED = ("ALLIED",)
    GERMAN = "GERMAN"


class Nation(Enum):
    US_1 = "US FIRST ARMY"
    US_3 = "US THIRD ARMY"
    US_VIII = "US EIGHTH CORPS"
    US_XV = "US_XV_CORPS"
    BRIT_2 = "BRIT SECOND ARMY"
    CAN_1 = "CANADIAN FIRST ARMY"
    GER = "GERMAN SEVENTH ARMY"


class ReinforcementType(Enum):
    PZ_DIV = "PANZER"
    MARKER = "MARKER"
    TIGER_BN = "TIGER"
    NEBELWERFER = "NEBELWERFER"
    FALLSCHIRMJAGER = "FALLSCHIRMJAGER"
    FLAK_88 = "FLAK 88"
    KAMPFGRUPPE = "KAMPFGRUPPE"
    COMMANDER = "COMMANDER"


class ResourceType(Enum):
    TRANSPORT = "Transport"
    SUPPLY = "Supply"
    HITLER_APPROVAL = "Hitler Approval"
