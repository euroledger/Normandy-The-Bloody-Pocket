import unittest

from core.enums import ResourceType
from core.models import GermanReinforcement
from core.enums import ReinforcementType

from cards.card_1 import card as card_1
from cards.card_9 import card as card_9
from cards.card_10 import card as card_10
from cards.card_19 import card as card_19
from cards.card_25 import card as card_25
from cards.card_26 import card as card_26
from cards.card_31 import card as card_31
from cards.card_34 import card as card_34


class TestResourcesAndReinforcements(unittest.TestCase):

    # =====================================================
    # RESOURCE CHANGES
    # =====================================================

    def test_card_9_resource_changes(self):

        self.assertEqual(

            card_9.resource_changes(),

            [
                (ResourceType.HITLER_APPROVAL, 2),
                (ResourceType.SUPPLY, 1)
            ]
        )

    def test_card_10_resource_changes(self):

        self.assertEqual(

            card_10.resource_changes(),

            [
                (ResourceType.HITLER_APPROVAL, 2)
            ]
        )

    def test_card_25_resource_changes(self):

        self.assertEqual(

            card_25.resource_changes(),

            [
                (ResourceType.TRANSPORT, -1),
                (ResourceType.HITLER_APPROVAL, -1),
                (ResourceType.SUPPLY, -1)
            ]
        )

    def test_card_26_resource_changes(self):

        self.assertEqual(

            card_26.resource_changes(),

            [
                (ResourceType.HITLER_APPROVAL, 1)
            ]
        )

    # =====================================================
    # REINFORCEMENTS
    # =====================================================

    def test_card_1_reinforcements(self):

        self.assertEqual(

            card_1.reinforcements(),

            [
                (
                    GermanReinforcement(
                        ReinforcementType.PZ_DIV,
                        "Pz Lehr"
                    ),
                    1
                ),

                (
                    GermanReinforcement(
                        ReinforcementType.PZ_DIV,
                        "12 SS Pz"
                    ),
                    1
                )
            ]
        )

    def test_card_19_reinforcements(self):

        self.assertEqual(

            card_19.reinforcements(),

            [
                (
                    GermanReinforcement(
                        ReinforcementType.FLAK_88,
                        "88mm Flak"
                    ),
                    3
                )
            ]
        )

    def test_card_31_reinforcements(self):

        self.assertEqual(

            card_31.reinforcements(),

            [
                (
                    GermanReinforcement(
                        ReinforcementType.FLAK_88,
                        "88mm Flak"
                    ),
                    2
                )
            ]
        )
        
    def test_card_34_reinforcements(self):
        self.assertEqual(
            card_34.reinforcements(),
            [
                (
                    GermanReinforcement(
                        ReinforcementType.KAMPFGRUPPE,
                        "Kampfgruppe"
                    ),
                    1
                )
            ]
        )
        
    def test_card_25_has_no_reinforcements(self):

        self.assertEqual(

            card_25.reinforcements(),

            []
        )


if __name__ == "__main__":
    unittest.main()