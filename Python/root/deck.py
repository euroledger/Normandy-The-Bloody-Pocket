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
from cards.card_33 import card as card_033
from cards.card_35 import card as card_035
from cards.card_36 import card as card_036
from cards.card_37 import card as card_037
from cards.card_34 import card as card_034
from cards.card_38 import card as card_038
from cards.card_40 import card as card_040
from cards.card_41 import card as card_041
from cards.card_43 import card as card_043
from cards.card_44 import card as card_044
from cards.card_46 import card as card_046
from cards.card_47 import card as card_047
from cards.card_48 import card as card_048
from cards.card_32 import card as card_032
from cards.card_45 import card as card_045
from cards.card_39 import card as card_039
from cards.card_42 import card as card_042

# =========================================================
# ALL CARDS
# =========================================================

all_cards = [
    card_001,
    card_002,
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
    card_024,
    card_025,
    card_026,
    card_027,
    card_028,
    card_029,
    card_030,
    card_031,
    card_032,
    card_033,
    card_034,
    card_035,
    card_036,
    card_037,
    card_038,
    card_039,
    card_040,
    card_041,
    card_042,
    card_043,
    card_044,
    card_045,
    card_046,
    card_047,
    card_048,
  
]


# =========================================================
# DECKS
# =========================================================

early_deck = []
mid_deck = []
late_deck = []

MID_DECK_IDS = {
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    33,
    35,
    36,
    37,
    43
}

LATE_DECK_IDS = {
    32,
    34,
    38,
    39,
    40,
    41,
    42,
    44,
    45,
    46,
    47,
    48
}

# =========================================================
# SORT CARDS INTO DECKS
# =========================================================


for card in all_cards:

    # EARLY DECK

    if 1 <= card.card_id <= 24:
        early_deck.append(card)

    # MID DECK

    elif card.card_id in MID_DECK_IDS:
        mid_deck.append(card)

    # LATE DECK

    elif card.card_id in LATE_DECK_IDS:
        late_deck.append(card)


# =========================================================
# CARD LOOKUP
# =========================================================

card_lookup = {}

for card in all_cards:
    card_lookup[card.card_id] = card


# =========================================================
# MAIN LOOP
# =========================================================

while True:

    print()
    print("========================================")
    print("SOS NORMANDY CARD DATABASE")
    print("========================================")
    print()

    print("Available Cards:")

    for card in all_cards:
        print(f"  {card.card_id}: {card.title}")

    print()
    print("Enter a card number to view summary")
    print("Enter Q to quit")
    print()

    user_input = input("> ").strip()

    # -------------------------------------
    # QUIT
    # -------------------------------------

    if user_input.upper() == "Q":
        print("Goodbye.")
        break

    # -------------------------------------
    # VALIDATE NUMBER
    # -------------------------------------

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    card_id = int(user_input)

    # -------------------------------------
    # LOOKUP CARD
    # -------------------------------------

    if card_id not in card_lookup:
        print("Card not found.")
        continue

    # -------------------------------------
    # PRINT SUMMARY
    # -------------------------------------

    selected_card = card_lookup[card_id]
    selected_card.summary()

    print()
    input("Press ENTER to return to menu...")