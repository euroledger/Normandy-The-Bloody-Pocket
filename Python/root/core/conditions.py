

class Condition:

    def is_met(self, game_state):
        return True
    
# =========================================================
# HITLER APPROVAL CHECK
# =========================================================

class HitlerApprovalCheck(Condition):

    def __init__(self, passed=True):
        self.passed = passed

    def is_met(self, game_state):

        return (
            getattr(
                game_state,
                "hitler_approval_check_passed",
                False
            )
            == self.passed
        )