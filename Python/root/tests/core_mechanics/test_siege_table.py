# tests/test_siege.py

import unittest

from core.tables.siege import (
    get_siege_result,
    SiegeResultType
)


class TestSiegeTable(unittest.TestCase):

    # =====================================================
    # ROLL 1
    # =====================================================

    def test_roll_1_no_effect(self):

        result = get_siege_result(1)

        self.assertEqual(
            result.result_type,
            SiegeResultType.NO_EFFECT
        )

        self.assertEqual(
            result.combat_steps_eliminated,
            0
        )

        self.assertFalse(
            result.space_captured
        )

    # =====================================================
    # ROLL 2
    # =====================================================

    def test_roll_2_eliminate_1_step(self):

        result = get_siege_result(2)

        self.assertEqual(
            result.result_type,
            SiegeResultType.ELIMINATE_1_STEP
        )

        self.assertEqual(
            result.combat_steps_eliminated,
            1
        )

        self.assertFalse(
            result.space_captured
        )

    # =====================================================
    # ROLL 3
    # =====================================================

    def test_roll_3_eliminate_2_steps(self):

        result = get_siege_result(3)

        self.assertEqual(
            result.result_type,
            SiegeResultType.ELIMINATE_2_STEPS
        )

        self.assertEqual(
            result.combat_steps_eliminated,
            2
        )

        self.assertFalse(
            result.space_captured
        )

    # =====================================================
    # ROLL 4
    # =====================================================

    def test_roll_4_eliminate_3_steps(self):

        result = get_siege_result(4)

        self.assertEqual(
            result.result_type,
            SiegeResultType.ELIMINATE_3_STEPS
        )

        self.assertEqual(
            result.combat_steps_eliminated,
            3
        )

        self.assertFalse(
            result.space_captured
        )

    # =====================================================
    # ROLL 5
    # =====================================================

    def test_roll_5_eliminate_3_steps(self):

        result = get_siege_result(5)

        self.assertEqual(
            result.result_type,
            SiegeResultType.ELIMINATE_3_STEPS
        )

        self.assertEqual(
            result.combat_steps_eliminated,
            3
        )

        self.assertFalse(
            result.space_captured
        )

    # =====================================================
    # ROLL 6
    # =====================================================

    def test_roll_6_space_captured(self):

        result = get_siege_result(6)

        self.assertEqual(
            result.result_type,
            SiegeResultType.SPACE_CAPTURED
        )

        self.assertEqual(
            result.combat_steps_eliminated,
            0
        )

        self.assertTrue(
            result.space_captured
        )

# =====================================================
# SIEGE DRM
# =====================================================

from core.tables.siege import (
    calculate_siege_drm
)


class TestSiegeDrm(unittest.TestCase):

    # =====================================================
    # NO DRM
    # =====================================================

    def test_no_drm(self):

        result = calculate_siege_drm(
            attack_strength=8,
            defense_strength=8,
            has_air_support=True
        )

        self.assertEqual(
            result.drm,
            0
        )

        self.assertEqual(
            result.reasons,
            []
        )

    # =====================================================
    # DEFENSE DIFFERENTIAL >= 6
    # =====================================================

    def test_defense_differential_6(self):

        result = calculate_siege_drm(
            attack_strength=4,
            defense_strength=10,
            has_air_support=True
        )

        self.assertEqual(
            result.drm,
            -1
        )

        self.assertIn(
            "-1 DEFENSE DIFFERENTIAL >= 6",
            result.reasons
        )

    # =====================================================
    # DEFENSE DIFFERENTIAL >= 10
    # =====================================================

    def test_defense_differential_10(self):

        result = calculate_siege_drm(
            attack_strength=2,
            defense_strength=12,
            has_air_support=True
        )

        self.assertEqual(
            result.drm,
            -2
        )

        self.assertIn(
            "-2 DEFENSE DIFFERENTIAL >= 10",
            result.reasons
        )

    # =====================================================
    # NO AIR SUPPORT
    # =====================================================

    def test_no_air_support(self):

        result = calculate_siege_drm(
            attack_strength=8,
            defense_strength=8,
            has_air_support=False
        )

        self.assertEqual(
            result.drm,
            -1
        )

        self.assertIn(
            "-1 NO AIR SUPPORT",
            result.reasons
        )

    # =====================================================
    # NO COMBAT STEPS IN FORTRESS
    # =====================================================

    def test_no_combat_steps_in_fortress(self):
        result = calculate_siege_drm(
            attack_strength=4,
            defense_strength=4,
            has_air_support=True
        )
        self.assertEqual(
            result.drm,
            1
        )
        self.assertIn(
            "+1 NO COMBAT STEPS IN FORTRESS",
            result.reasons
        )

    # =====================================================
    # MULTIPLE DRMS
    # =====================================================

    def test_multiple_drms(self):
        result = calculate_siege_drm(
            attack_strength=2,
            defense_strength=12,
            has_air_support=False
        )
        self.assertEqual(
            result.drm,
            -3
        )
        self.assertIn(
            "-2 DEFENSE DIFFERENTIAL >= 10",
            result.reasons
        )
        self.assertIn(
            "-1 NO AIR SUPPORT",
            result.reasons
        )

    # =====================================================
    # FORTRESS PLUS AIR SUPPORT PENALTY
    # =====================================================

    def test_fortress_and_no_air_support(self):
        result = calculate_siege_drm(
            attack_strength=4,
            defense_strength=4,
            has_air_support=False
        )

        self.assertEqual(
            result.drm,
            0
        )

        self.assertIn(
            "-1 NO AIR SUPPORT",
            result.reasons
        )

        self.assertIn(
            "+1 NO COMBAT STEPS IN FORTRESS",
            result.reasons
        )