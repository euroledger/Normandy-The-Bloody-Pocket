import pytest

from core.allied_armies import (
    US_FIRST_ARMY,
    BRITISH_SECOND_ARMY,
    CANADIAN_FIRST_ARMY,
    US_VIII_CORPS,
    US_XV_CORPS,
    US_THIRD_ARMY,
)

@pytest.fixture(autouse=True)
def clean_army_flags():
    for army in [
        US_FIRST_ARMY,
        BRITISH_SECOND_ARMY,
        CANADIAN_FIRST_ARMY,
        US_VIII_CORPS,
        US_XV_CORPS,
        US_THIRD_ARMY,
    ]:
        army.flipped = False
        army.merged = False