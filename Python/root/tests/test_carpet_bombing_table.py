import unittest
from core.carpet_bombing import get_carpet_bombing_result
from core.carpet_bombing import CarpetBombingResultType
from core.carpet_bombing import ATTACK_CANCELLED

# =========================================================
# TEST CARPET BOMBING
# =========================================================

class TestCarpetBombing(unittest.TestCase):
    def test_roll_1_no_drm(self):
        result = get_carpet_bombing_result(1, 0)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_TWO)
        self.assertEqual(result.attack_modifier, 2)

    def test_roll_2_no_drm(self):
        result = get_carpet_bombing_result(2, 0)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_TWO)
        self.assertEqual(result.attack_modifier, 2)

    def test_roll_3_no_drm(self):
        result = get_carpet_bombing_result(3, 0)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_TWO)
        self.assertEqual(result.attack_modifier, 2)

    def test_roll_4_no_drm(self):
        result = get_carpet_bombing_result(4, 0)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_TWO)
        self.assertEqual(result.attack_modifier, 2)

    def test_roll_5_no_drm(self):
        result = get_carpet_bombing_result(5, 0)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_ONE)
        self.assertEqual(result.attack_modifier, 1)

    def test_roll_6_no_drm(self):
        result = get_carpet_bombing_result(6, 0)
        self.assertEqual(result.result_type, CarpetBombingResultType.CANCELLED)
        self.assertEqual(result.attack_modifier, ATTACK_CANCELLED)

    def test_roll_1_with_plus_1_drm(self):
        result = get_carpet_bombing_result(1, 1)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_TWO)
        self.assertEqual(result.attack_modifier, 2)

    def test_roll_4_with_plus_1_drm(self):
        result = get_carpet_bombing_result(4, 1)
        self.assertEqual(result.result_type, CarpetBombingResultType.PLUS_ONE)
        self.assertEqual(result.attack_modifier, 1)

    def test_roll_5_with_plus_1_drm(self):
        result = get_carpet_bombing_result(5, 1)
        self.assertEqual(result.result_type, CarpetBombingResultType.CANCELLED)
        self.assertEqual(result.attack_modifier, ATTACK_CANCELLED)

    def test_roll_6_with_plus_1_drm(self):
        result = get_carpet_bombing_result(6, 1)
        self.assertEqual(result.result_type, CarpetBombingResultType.CANCELLED)
        self.assertEqual(result.attack_modifier, ATTACK_CANCELLED)