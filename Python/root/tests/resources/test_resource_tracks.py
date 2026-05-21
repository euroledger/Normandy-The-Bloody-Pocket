import unittest

from cards.card_6 import card as card_006
from cards.card_36 import card as card_036


from core.map.map_model import (
    transport_track,
    supply_track,
    hitler_approval_track
)

from core.card_utilities import (
    apply_resource_modifiers
)

class TestResourceTracks(unittest.TestCase):
    def setUp(self):
        transport_track.value = 5
        supply_track.value = 4
        hitler_approval_track.value = 6

    def test_french_resistance_card(self):
        apply_resource_modifiers(card_006)

        self.assertEqual(
            transport_track.value,
            4
        )

        self.assertEqual(
            supply_track.value,
            3
        )

        self.assertEqual(
            hitler_approval_track.value,
            5
        )
        
    def test_card_36_resource_changes(self):
        transport_track.value = 3
        supply_track.value = 3
        hitler_approval_track.value = 3

        apply_resource_modifiers(card_036)

        self.assertEqual(
            transport_track.value,
            3
        )

        self.assertEqual(
            supply_track.value,
            5
        )

        self.assertEqual(
            hitler_approval_track.value,
            4
        )