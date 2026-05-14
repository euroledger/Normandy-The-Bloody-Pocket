# core/armies.py

from core.models import AlliedArmy
from core.enums import Nation


FIRST_US = AlliedArmy("1st US", Nation.US_1)
THIRD_US = AlliedArmy("3rd US", Nation.US_3)
SECOND_BRIT = AlliedArmy("2nd BRIT", Nation.BRIT_2)
FIRST_CAN = AlliedArmy("1st CAN", Nation.CAN_1)