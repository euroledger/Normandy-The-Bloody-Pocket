from dataclasses import dataclass
from enum import Enum


# =========================================================
# CARPET BOMBING CONSTANTS
# =========================================================

ATTACK_CANCELLED = -999


# =========================================================
# CARPET BOMBING RESULT TYPES
# =========================================================

class CarpetBombingResultType(Enum):
    PLUS_TWO = "+2 Carpet Bombing"
    PLUS_ONE = "+1 Carpet Bombing"
    CANCELLED = "Attack Cancelled"


# =========================================================
# CARPET BOMBING RESULT
# =========================================================

@dataclass
class CarpetBombingResult:

    result_type: CarpetBombingResultType
    attack_modifier: int


# =========================================================
# CARPET BOMBING TABLE
# =========================================================

CARPET_BOMBING_TABLE = {

    1: CarpetBombingResult(
        result_type=CarpetBombingResultType.PLUS_TWO,
        attack_modifier=2
    ),

    2: CarpetBombingResult(
        result_type=CarpetBombingResultType.PLUS_TWO,
        attack_modifier=2
    ),

    3: CarpetBombingResult(
        result_type=CarpetBombingResultType.PLUS_TWO,
        attack_modifier=2
    ),

    4: CarpetBombingResult(
        result_type=CarpetBombingResultType.PLUS_TWO,
        attack_modifier=2
    ),

    5: CarpetBombingResult(
        result_type=CarpetBombingResultType.PLUS_ONE,
        attack_modifier=1
    ),

    6: CarpetBombingResult(
        result_type=CarpetBombingResultType.CANCELLED,
        attack_modifier=ATTACK_CANCELLED
    )
}


# =========================================================
# LOOKUP
# =========================================================

def get_carpet_bombing_result(
    die_roll: int,
    drm: int = 0
) -> CarpetBombingResult:
    modified_roll = die_roll + drm
    modified_roll = max(1, min(6, modified_roll))
    return CARPET_BOMBING_TABLE[modified_roll]