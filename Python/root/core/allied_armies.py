# core/armies.py

from core.models import AlliedArmy
from core.enums import Nation

# FIRST_US = AlliedArmy("1st US", Nation.US_1)
# THIRD_US = AlliedArmy("3rd US", Nation.US_3)
# SECOND_BRIT = AlliedArmy("2nd BRIT", Nation.BRIT_2)
# FIRST_CAN = AlliedArmy("1st CAN", Nation.CAN_1)

BRITISH_SECOND_ARMY = AlliedArmy(name="BRITISH XXX CORPS",
                                 nation=Nation.BRIT_2,
                                 reverse_name="BRITISH 2nd ARMY",
                                 _strength=2,
                                 reverse_strength=4)

CANADIAN_FIRST_ARMY = AlliedArmy(name="BRITISH I CORPS",
                                 nation=Nation.CAN_1,
                                 reverse_name="CANADIAN 1st ARMY",
                                 _strength=2,
                                 reverse_strength=4)

US_FIRST_ARMY = AlliedArmy(name="US 1st ARMY",
                           nation=Nation.US_1,
                           reverse_name="US 1st ARMY",
                           _strength=3,
                           reverse_strength=4)

US_VIII_CORPS = AlliedArmy(name="US VIII CORPS",
                           nation=Nation.US_3,
                           _strength=2)

US_XV_CORPS = AlliedArmy(name="US XV CORPS", nation=Nation.US_3, _strength=2)

US_THIRD_ARMY = AlliedArmy(name="US 3rd ARMY", nation=Nation.US_3, _strength=4)
