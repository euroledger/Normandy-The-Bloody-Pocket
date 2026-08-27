

class Condition:

    def is_met(self, game_state):
        return True
    
# =========================================================
# HITLER INTEVENTION CANCELED
# =========================================================

class HitlerInterventionNoEffect(Condition):

    def __init__(self, passed=True):
        self.passed = passed

    def is_met(self, game_state):

        return (
            getattr(
                game_state,
                "hitler_intervention_no_effect",
                False
            )
            == self.passed
        )