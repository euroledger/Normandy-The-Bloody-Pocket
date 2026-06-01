import unittest

from cards.card_1 import card as card_001
from cards.card_2 import card as card_002
from cards.card_3 import card as card_003
from cards.card_4 import card as card_004
from cards.card_5 import card as card_005
from cards.card_6 import card as card_006
from cards.card_7 import card as card_007
from cards.card_8 import card as card_008
from cards.card_9 import card as card_009
from cards.card_10 import card as card_010
from cards.card_11 import card as card_011
from cards.card_12 import card as card_012
from cards.card_13 import card as card_013
from cards.card_14 import card as card_014
from cards.card_15 import card as card_015
from cards.card_16 import card as card_016
from cards.card_17 import card as card_017
from cards.card_18 import card as card_018
from cards.card_19 import card as card_019
from cards.card_20 import card as card_020
from cards.card_21 import card as card_021
from cards.card_22 import card as card_022
from cards.card_23 import card as card_023
from cards.card_24 import card as card_024
from cards.card_25 import card as card_025
from cards.card_26 import card as card_026
from cards.card_27 import card as card_027
from cards.card_28 import card as card_028
from cards.card_29 import card as card_029
from cards.card_30 import card as card_030
from cards.card_31 import card as card_031
from cards.card_32 import card as card_032
from cards.card_33 import card as card_033
from cards.card_34 import card as card_034
from cards.card_35 import card as card_035
from cards.card_36 import card as card_036
from cards.card_37 import card as card_037
from cards.card_38 import card as card_038
from cards.card_39 import card as card_039
from cards.card_40 import card as card_040
from cards.card_41 import card as card_041
from cards.card_42 import card as card_042
from cards.card_43 import card as card_043
from cards.card_44 import card as card_044
from cards.card_45 import card as card_045
from cards.card_46 import card as card_046
from cards.card_47 import card as card_047
from cards.card_48 import card as card_048

from core.resources import do_resource_phase_drms
from core.global_game_state import GlobalGameState
from core.weather import WeatherType


class TestResourcePhase(unittest.TestCase):
    def setUp(self):
        GlobalGameState.transport_roll_drm = 0
        GlobalGameState.supply_roll_drm = 0
        GlobalGameState.transport_check_drm = 0
        GlobalGameState.supply_check_drm = 0
        GlobalGameState.hitler_approval_check_drm = 0

    def test_resource_roll_drms(self):
        do_resource_phase_drms(WeatherType.OVERCAST, card_001)
        self.assertEqual(GlobalGameState.transport_roll_drm, 1)
        self.assertEqual(GlobalGameState.supply_roll_drm, 1)

        GlobalGameState.transport_roll_drm = 5
        GlobalGameState.supply_roll_drm = 5
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_001)
        self.assertEqual(GlobalGameState.transport_roll_drm, 0)
        self.assertEqual(GlobalGameState.supply_roll_drm, 0)

    def test_card_1_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_001)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_2_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_002)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)

    def test_card_3_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_003)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_4_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_004)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_5_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_005)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_6_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_006)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_7_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_007)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_8_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_008)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_9_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_009)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_10_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_010)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_11_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_011)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_12_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_012)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_13_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_013)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_14_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_014)
        self.assertEqual(GlobalGameState.transport_check_drm, 1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_15_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_015)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_16_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_016)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_17_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_017)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_18_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_018)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_19_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_019)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_20_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_020)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_21_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_021)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_22_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_022)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_23_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_023)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_24_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_024)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_25_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_025)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_26_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_026)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_27_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_027)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_28_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_028)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_29_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_029)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_30_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_030)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_31_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_031)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_32_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_032)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_33_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_033)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_34_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_034)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_35_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_035)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_36_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_036)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_37_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_037)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_38_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_038)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_39_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_039)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_40_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_040)
        self.assertEqual(GlobalGameState.transport_check_drm, -1)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_41_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_041)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_42_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_042)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_43_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_043)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_44_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_044)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_45_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_045)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_46_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_046)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_47_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_047)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)

    def test_card_48_resource_check_drms(self):
        do_resource_phase_drms(WeatherType.PARTLY_CLEAR, card_048)
        self.assertEqual(GlobalGameState.transport_check_drm, 0)
        self.assertEqual(GlobalGameState.supply_check_drm, 0)
        self.assertEqual(GlobalGameState.hitler_approval_check_drm, 0)


if __name__ == "__main__":
    unittest.main()
