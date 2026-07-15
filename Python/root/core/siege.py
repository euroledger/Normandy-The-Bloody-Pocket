from dataclasses import dataclass
from enum import Enum

# =========================================================
# SIEGE RESULTS
# =========================================================
class SiegeResultType(Enum):
    NO_EFFECT = "No Effect"
    ELIMINATE_1_STEP = "Eliminate 1 combat step"
    ELIMINATE_2_STEPS = "Eliminate 2 combat steps"
    ELIMINATE_3_STEPS = "Eliminate 3 combat steps"
    SPACE_CAPTURED = "Space captured"

# =========================================================
# SIEGE RESULT
# =========================================================
@dataclass
class SiegeResult:
    result_type: SiegeResultType
    combat_steps_eliminated: int
    space_captured: bool

# =========================================================
# SIEGE DRM RESULT
# =========================================================
@dataclass
class SiegeDrmResult:
    drm: int
    reasons: list[str]

# =========================================================
# SIEGE TABLE
# =========================================================
def get_siege_result(die_roll: int) -> SiegeResult:
    return SIEGE_TABLE_MARK_3[die_roll]

# =========================================================
# SIEGE DRM
# =========================================================
def calculate_siege_drm(attack_strength: int, defense_strength: int, has_air_support: bool) -> SiegeDrmResult:
    drm = 0
    reasons = []
    # =====================================================
    # DEFENSE DIFFERENTIAL
    # =====================================================
    defense_attack_differential = defense_strength - attack_strength
    if defense_attack_differential >= 10:
        drm -= 2
        reasons.append("-2 DEFENSE DIFFERENTIAL >= 10")

    elif defense_attack_differential >= 6:
        drm -= 1
        reasons.append("-1 DEFENSE DIFFERENTIAL >= 6")

    # =====================================================
    # NO AIR SUPPORT
    # =====================================================
    if has_air_support is False:
        drm -= 1
        reasons.append("-1 NO AIR SUPPORT")

    # =====================================================
    # NO COMBAT STEPS IN FORTRESS
    # =====================================================
    if defense_strength == 4:
        drm += 1
        reasons.append("+1 NO COMBAT STEPS IN FORTRESS")
    return SiegeDrmResult(drm=drm, reasons=reasons)


# SIEGE_TABLE = {
#     1: SiegeResult(result_type=SiegeResultType.NO_EFFECT, combat_steps_eliminated=0, space_captured=False),
#     2: SiegeResult(result_type=SiegeResultType.NO_EFFECT, combat_steps_eliminated=0, space_captured=False),
#     3: SiegeResult(result_type=SiegeResultType.ELIMINATE_1_STEP, combat_steps_eliminated=1, space_captured=False),
#     4: SiegeResult(result_type=SiegeResultType.ELIMINATE_2_STEPS, combat_steps_eliminated=2, space_captured=False),
#     5: SiegeResult(result_type=SiegeResultType.ELIMINATE_3_STEPS, combat_steps_eliminated=3, space_captured=False),
#     6: SiegeResult(result_type=SiegeResultType.SPACE_CAPTURED, combat_steps_eliminated=0, space_captured=True),
# }


# SIEGE_TABLE_MARK_2 = {
#     1: SiegeResult(result_type=SiegeResultType.NO_EFFECT, combat_steps_eliminated=0, space_captured=False),
#     2: SiegeResult(result_type=SiegeResultType.ELIMINATE_1_STEP, combat_steps_eliminated=1, space_captured=False),
#     3: SiegeResult(result_type=SiegeResultType.ELIMINATE_2_STEPS, combat_steps_eliminated=2, space_captured=False),
#     4: SiegeResult(result_type=SiegeResultType.ELIMINATE_3_STEPS, combat_steps_eliminated=3, space_captured=False),
#     5: SiegeResult(result_type=SiegeResultType.SPACE_CAPTURED, combat_steps_eliminated=3, space_captured=True),
#     6: SiegeResult(result_type=SiegeResultType.SPACE_CAPTURED, combat_steps_eliminated=0, space_captured=True),
# }

SIEGE_TABLE_MARK_3= {
    1: SiegeResult(result_type=SiegeResultType.NO_EFFECT, combat_steps_eliminated=0, space_captured=False),
    2: SiegeResult(result_type=SiegeResultType.ELIMINATE_1_STEP, combat_steps_eliminated=1, space_captured=False),
    3: SiegeResult(result_type=SiegeResultType.ELIMINATE_2_STEPS, combat_steps_eliminated=2, space_captured=False),
    4: SiegeResult(result_type=SiegeResultType.ELIMINATE_3_STEPS, combat_steps_eliminated=3, space_captured=False),
    5: SiegeResult(result_type=SiegeResultType.ELIMINATE_3_STEPS, combat_steps_eliminated=3, space_captured=False),
    6: SiegeResult(result_type=SiegeResultType.SPACE_CAPTURED, combat_steps_eliminated=0, space_captured=True),
}

