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
from cards.card_47 import card as card_047


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
    card_047
]


# =========================================================
# DECKS
# =========================================================

early_deck = []
mid_deck = []
late_deck = []


# =========================================================
# SORT CARDS INTO DECKS
# =========================================================

for card in all_cards:

    # EARLY DECK
    if 1 <= card.card_id <= 24:
        early_deck.append(card)

    # MID DECK
    elif 25 <= card.card_id <= 36:
        mid_deck.append(card)

    # LATE DECK
    elif 37 <= card.card_id <= 48:
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