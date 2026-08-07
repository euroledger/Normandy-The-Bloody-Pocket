from dataclasses import dataclass

# =========================================================
# US 3RD ARMY ACTIVATION RESULT
# =========================================================
@dataclass
class UsThirdArmyActivationResult:
    activated: bool
    automatic: bool

# =========================================================
# US 3RD ARMY ACTIVATION DRM RESULT
# =========================================================
@dataclass
class UsThirdArmyActivationDrmResult:
    drm: int
    auto_activate: bool
    reasons: list[str]

# =========================================================
# US 3RD ARMY ACTIVATION TABLE
# =========================================================
def get_us_third_army_activation_result(die_roll: int):
    return US_THIRD_ARMY_ACTIVATION_TABLE[die_roll]

# =========================================================
# US 3RD ARMY ACTIVATION DRM
# =========================================================
def calculate_us_third_army_activation_drm(track_number: int) -> UsThirdArmyActivationDrmResult:
    drm = 0
    reasons = []
    auto_activate = False
    
    if track_number == 6:
        drm = 2
        reasons.append("+2 SAINT-LÔ")

    elif track_number == 5:
        drm = 3
        reasons.append("+3 COUTANCES")

    elif track_number == 4:
        drm = 5
        reasons.append("+5 AVRANCHES")
    elif track_number == 3:
        auto_activate = True
        reasons.append("AUTO MORTAIN")


    return UsThirdArmyActivationDrmResult(drm=drm, reasons=reasons, auto_activate=auto_activate)

# =========================================================
# US 3RD ARMY ACTIVATION TABLE
# =========================================================
US_THIRD_ARMY_ACTIVATION_TABLE = {
    2:  UsThirdArmyActivationResult(activated=False, automatic=False),
    3:  UsThirdArmyActivationResult(activated=False, automatic=False),
    4:  UsThirdArmyActivationResult(activated=False, automatic=False),
    5:  UsThirdArmyActivationResult(activated=False, automatic=False),
    6:  UsThirdArmyActivationResult(activated=False, automatic=False),
    7:  UsThirdArmyActivationResult(activated=False, automatic=False),
    8:  UsThirdArmyActivationResult(activated=False, automatic=False),
    9:  UsThirdArmyActivationResult(activated=False, automatic=False),
    10: UsThirdArmyActivationResult(activated=False, automatic=False),
    11: UsThirdArmyActivationResult(activated=False, automatic=False),
    12: UsThirdArmyActivationResult(activated=True, automatic=False),
    13: UsThirdArmyActivationResult(activated=True, automatic=False),
    14: UsThirdArmyActivationResult(activated=True, automatic=False),
    15: UsThirdArmyActivationResult(activated=True, automatic=False),
    16: UsThirdArmyActivationResult(activated=True, automatic=False),
    17: UsThirdArmyActivationResult(activated=True, automatic=False),
}