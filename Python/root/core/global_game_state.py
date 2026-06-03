from core.models import Strategy


class GlobalGameState:
    us_1_front_line = 11
    brit_2_front_line = 7
    can_1_front_line = 7
    us_3_front_line = 8

    # RESOURCE ROLL DRMs
    transport_roll_drm = 0
    supply_roll_drm = 0

    # RESOURCE CHECK DRMs
    transport_check_drm = 0
    supply_check_drm = 0
    hitler_approval_check_drm = 0

    # BOCAGE MODIFIER, -1 ONCE EVENT CARD DRAWN FOR GERMAN DEFENSE ONLY
    bocage_defense_modifier = 0

    # HUMAN/AI TOGGLES
    german_casualty_strategy = Strategy.HUMAN
