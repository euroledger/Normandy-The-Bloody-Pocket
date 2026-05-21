import unittest

from core.enums import ModifierType

from cards.card_38 import card as card_38
from cards.card_35 import card as card_35
from cards.card_14 import card as card_14

# =========================================================
# HELPER
# =========================================================



# =========================================================
# TEST MODIFIERS
# =========================================================

class TestModifiers(unittest.TestCase):

    def test_card_35_modifiers(self):
        modifiers = card_35.get_action_modifiers()
        expected = [
            {
                "modifier_type": ModifierType.DEFENSE_STRENGTH,
                "value": 2,
                "target": "1st US",
                "label": None
            },
            {
                "modifier_type": ModifierType.DEFENSE_STRENGTH,
                "value": 2,
                "target": "2nd BRIT",
                "label": None
            },
            {
                "modifier_type": ModifierType.DEFENSE_STRENGTH,
                "value": 2,
                "target": "1st CAN",
                "label": None
            },
            {
                "modifier_type": ModifierType.DEFENSE_STRENGTH,
                "value": 2,
                "target": "3rd US",
                "label": None
            }
        ]
        self.assertEqual(modifiers, expected)

    def test_card_14_modifiers(self):
        modifiers = card_14.get_action_modifiers()
        expected = [
            {
                "modifier_type": ModifierType.ATTACK_STRENGTH,
                "value": 1,
                "target": "2nd BRIT",
                "label": None
            },
            {
                "modifier_type": ModifierType.ATTACK_STRENGTH,
                "value": 1,
                "target": "1st CAN",
                "label": None
            },
            {
                "modifier_type": ModifierType.COMMANDER,
                "value": 2,
                "target": "2nd BRIT",
                "label": "Montgomery"
            }
        ]
        self.assertEqual(modifiers, expected)

    def test_card_38_modifiers(self):
        modifiers = card_38.get_action_modifiers()
        expected = [
            {
                "modifier_type": ModifierType.COMMANDER,
                "value": 1,
                "target": None,
                "label": "Model"
            }
        ]
        self.assertEqual(modifiers, expected)