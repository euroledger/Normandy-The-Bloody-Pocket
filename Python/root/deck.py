from random import choice, shuffle

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
from cards.card_33 import card as card_033
from cards.card_35 import card as card_035
from cards.card_36 import card as card_036
from cards.card_37 import card as card_037
from cards.card_43 import card as card_043

from cards.card_32 import card as card_032
from cards.card_34 import card as card_034
from cards.card_38 import card as card_038
from cards.card_39 import card as card_039
from cards.card_40 import card as card_040
from cards.card_41 import card as card_041
from cards.card_42 import card as card_042
from cards.card_44 import card as card_044
from cards.card_45 import card as card_045
from cards.card_46 import card as card_046
from cards.card_47 import card as card_047
from cards.card_48 import card as card_048


# =========================================================
# EARLY DECK
# =========================================================

draw_deck = [

    card_003,
    card_004,
    card_005,
    card_006,
    card_007,
    card_008,
    card_009,
    card_010,
    card_011,
    card_012,
    card_013,
    card_014,
    card_015,
    card_016,
    card_017,
    card_018,
    card_019,
    card_020,
    card_021,
    card_022,
    card_023,
    card_024
]


# =========================================================
# MID DECK
# =========================================================

mid_deck = [

    card_025,
    card_026,
    card_027,
    card_028,
    card_029,
    card_030,
    card_031,
    card_033,
    card_035,
    card_036,
    card_037,
    card_043
]


# =========================================================
# LATE DECK
# =========================================================

late_deck = [

    card_032,
    card_034,
    card_038,
    card_039,
    card_040,
    card_041,
    card_042,
    card_044,
    card_045,
    card_046,
    card_047,
    card_048
]


# =========================================================
# TRACKING
# =========================================================

cards_drawn = 0

drawn_cards = []

mid_deck_added = False
late_deck_added = False


# =========================================================
# SIEGE TEST ENGINE
# =========================================================

while True:

    print()
    print("========================================")
    print("SIEGE TEST ENGINE")
    print("========================================")
    print()

    print(f"Cards Drawn: {cards_drawn}")

    if drawn_cards:

        drawn_ids = [
            str(card.card_id)
            for card in drawn_cards
        ]

        print(f"Drawn Cards: {', '.join(drawn_ids)}")

    else:

        print("Drawn Cards: NONE")

    print(f"Cards Remaining: {len(draw_deck)}")

    print()
    print("1. Draw Card")
    print("Q. Quit")
    print()

    user_input = input("> ").strip().upper()

    # =====================================================
    # QUIT
    # =====================================================

    if user_input == "Q":

        print("Goodbye.")
        break

    # =====================================================
    # DRAW CARD
    # =====================================================

    if user_input == "1":

        if not draw_deck:

            print()
            print("DRAW DECK EMPTY")
            input("Press ENTER to continue...")
            continue

        drawn_card = choice(draw_deck)

        # Remove from deck

        draw_deck.remove(drawn_card)

        # Track

        drawn_cards.append(drawn_card)

        cards_drawn += 1

        # =================================================
        # ADD MID DECK
        # =================================================

        if (
            drawn_card.card_id == 20
            and not mid_deck_added
        ):

            draw_deck.extend(mid_deck)

            shuffle(draw_deck)

            mid_deck_added = True

            print()
            print("========================================")
            print("MID DECK ADDED")
            print("DRAW DECK SHUFFLED")
            print("========================================")

        # =================================================
        # ADD LATE DECK
        # =================================================

        if (
            drawn_card.card_id == 37
            and not late_deck_added
        ):

            draw_deck.extend(late_deck)

            shuffle(draw_deck)

            late_deck_added = True

            print()
            print("========================================")
            print("LATE DECK ADDED")
            print("DRAW DECK SHUFFLED")
            print("========================================")

        print()
        print("========================================")
        print(f"DREW CARD {drawn_card.card_id}")
        print("========================================")

        drawn_card.summary()

        print()
        input("Press ENTER to continue...")