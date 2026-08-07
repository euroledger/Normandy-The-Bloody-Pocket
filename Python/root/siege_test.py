import sys
from random import choice, shuffle, randint

from core.allied_armies import CANADIAN_FIRST_ARMY
from core.tables.weather import get_weather_result
from core.tables.carpet_bombing import get_carpet_bombing_result
from core.tables.carpet_bombing import ATTACK_CANCELLED

from core.card_utilities import calculate_attack_modifiers
from core.card_utilities import get_armies, get_armies_as_objects
from core.tables.siege import calculate_siege_drm, get_siege_result

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
# TERMINAL COLORS
# =========================================================

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


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
    card_024,
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
    card_043,
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
    card_048,
]


# =========================================================
# TRACKING
# =========================================================

cards_drawn = 0
canada_1_army_cards = 0

defense_strength = 8
starting_combat_strength = defense_strength - 4
drawn_cards = []

mid_deck_added = False
late_deck_added = False

current_card = None
current_weather = None

current_carpet_bombing = 0

current_step = 1


# =========================================================
# ATTACK STRENGTHS
# =========================================================


def print_attack_strengths(card, weather, carpet_bombing):

    print(CYAN)

    print()
    print("========================================")
    print("ATTACK STRENGTHS")
    print("========================================")
    print()

    armies = get_armies(card)

    if not armies:
        print("\t=>NO ARMIES ATTACKING")
        print(RESET)
        return

    num_jabos = weather.available_jabos

    for army in armies:
        result = calculate_attack_modifiers(
            card=card, army=army, num_jabos=num_jabos, carpet_bombing=carpet_bombing, print_modifiers=True
        )

        print(result)

    print(RESET)


# =========================================================
# CANADIAN 1ST ARMY SIEGE ROLL
# =========================================================


def perform_canadian_siege_roll(card, weather, carpet_bombing, defense_strength):
    global canada_1_army_cards
    print(CYAN)
    print()
    print("========================================")
    print("CANADIAN 1ST ARMY SIEGE ROLL")
    print("========================================")
    print()
    armies = get_armies(card)

    # =====================================================
    # NO CANADIAN 1ST ARMY
    # =====================================================

    if "1st CAN" not in armies:
        print("\t=>NO ROLL")

        print(RESET)

        return defense_strength

    canada_1_army_cards += 1

    # =====================================================
    # ROLL
    # =====================================================

    siege_roll = randint(1, 6)

    modified_roll = siege_roll

    # =====================================================
    # CALCULATE ATTACK STRENGTH
    # =====================================================

    canadian_result = calculate_attack_modifiers(
        card=card, army=CANADIAN_FIRST_ARMY, num_jabos=weather.available_jabos, carpet_bombing=carpet_bombing
    )

    canadian_attack_strength = canadian_result["attack_strength"]

    has_air_support = canadian_result["has_air_support"]

    # =====================================================
    # CALCULATE DRM
    # =====================================================

    drm_result = calculate_siege_drm(
        attack_strength=canadian_attack_strength, defense_strength=defense_strength, has_air_support=has_air_support
    )

    modified_roll += drm_result.drm

    # =====================================================
    # DISPLAY DRMS
    # =====================================================

    print(f"DEFENSE-ATTACK DIFFERENTIAL: {defense_strength - canadian_attack_strength}")

    for reason in drm_result.reasons:
        print(f"DRM: {reason}")

    # =====================================================
    # CLAMP
    # =====================================================

    modified_roll = max(1, min(6, modified_roll))

    siege_result = get_siege_result(modified_roll)

    print()

    print(f"BASE ROLL: {siege_roll}")
    print(f"MODIFIED ROLL: {modified_roll}")

    print()

    print(f"RESULT: {siege_result.result_type.value}")

    # =====================================================
    # APPLY COMBAT STEP LOSSES
    # =====================================================

    if siege_result.combat_steps_eliminated > 0:
        steps_elim = min(defense_strength - 4, siege_result.combat_steps_eliminated)
        print(f"COMBAT STEPS ELIMINATED: {steps_elim}")

        defense_strength -= siege_result.combat_steps_eliminated

        defense_strength = max(4, defense_strength)

    print()

    print(f"\t=>DEFENSE STRENGTH: {defense_strength}")

    # =====================================================
    # SPACE CAPTURED
    # =====================================================

    if siege_result.space_captured:
        avg_hits_per_attack = starting_combat_strength / canada_1_army_cards
        print("SPACE CAPTURED - END OF SIEGE")
        print(f"=> NUMBER OF ATTACKS NEEDED TO END SIEGE={canada_1_army_cards}")
        print(f"=> HITS PER ATTACK={avg_hits_per_attack:.2f}")
        sys.exit("Bye")

    print(RESET)

    return defense_strength


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
    print(f"Defense Strength: {defense_strength}")

    print(f"Canadian 1st Army Attacks: {canada_1_army_cards}")

    if drawn_cards:
        drawn_ids = [str(card.card_id) for card in drawn_cards]

        print(f"List of Drawn Cards: ({', '.join(drawn_ids)})")

    else:
        print("Drawn Cards: NONE")

    print(f"Cards Remaining: {len(draw_deck)}")

    print()

    if current_card:
        print(f"Current Card: {current_card.card_id}")

    if current_weather:
        print(f"Current Weather: {current_weather.weather_type.value}")

    print()

    # =====================================================
    # STEP DISPLAY
    # =====================================================

    if current_step == 1:
        print(f"{GREEN}> Draw Card{RESET}")
    else:
        print(f"{RED}  Draw Card{RESET}")

    if current_step == 2:
        print(f"{GREEN}> Roll For Weather{RESET}")
    else:
        print(f"{RED}  Roll For Weather{RESET}")

    if current_step == 3:
        print(f"{GREEN}> Calculate Attack Strengths{RESET}")
    else:
        print(f"{RED}  Calculate Attack Strengths{RESET}")

    if current_step == 4:
        print(f"{GREEN}> Canadian 1st Army Siege Roll{RESET}")
    else:
        print(f"{RED}  Canadian 1st Army Siege Roll{RESET}")

    print()
    print("Press ENTER to perform next action")
    print("Press Q to quit")
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

    if current_step == 1 and user_input == "":
        if not draw_deck:
            print()
            print("DRAW DECK EMPTY")
            continue

        drawn_card = choice(draw_deck)

        current_card = drawn_card

        current_weather = None
        current_carpet_bombing = 0

        draw_deck.remove(drawn_card)

        drawn_cards.append(drawn_card)

        cards_drawn += 1

        # =================================================
        # ADD MID DECK
        # =================================================

        if drawn_card.card_id == 20 and not mid_deck_added:
            draw_deck.extend(mid_deck)

            shuffle(draw_deck)

            mid_deck_added = True

            print(CYAN)

            print()
            print("========================================")
            print("MID DECK ADDED")
            print("DRAW DECK SHUFFLED")
            print("========================================")

            print(RESET)

        # =================================================
        # ADD LATE DECK
        # =================================================

        if drawn_card.card_id == 37 and not late_deck_added:
            draw_deck.extend(late_deck)

            shuffle(draw_deck)

            late_deck_added = True

            print(CYAN)

            print()
            print("========================================")
            print("LATE DECK ADDED")
            print("DRAW DECK SHUFFLED")
            print("========================================")

            print(RESET)

        print(CYAN)

        print()
        print("========================================")
        print(f"DREW CARD {drawn_card.card_id}")
        print("========================================")

        drawn_card.summary()

        print(RESET)

        current_step = 2

        continue

    # =====================================================
    # WEATHER
    # =====================================================

    if current_step == 2 and user_input == "":
        weather_roll = randint(1, 6)

        weather = get_weather_result(weather_roll)

        current_weather = weather

        current_carpet_bombing = 0

        print(CYAN)

        print()
        print("========================================")
        print("WEATHER ROLL")
        print("========================================")
        print()

        print(f"ROLL: {weather_roll}")
        print(f"RESULT: {weather.weather_type.value}")

        # =================================================
        # CARPET BOMBING
        # =================================================

        if current_weather.available_jabos > 0 and current_card.air_power.has_carpet_bombing():
            print()
            print("========================================")
            print("CARPET BOMBING")
            print("========================================")
            print()

            carpet_roll = randint(1, 6)

            carpet_result = get_carpet_bombing_result(die_roll=carpet_roll, drm=current_weather.carpet_bombing_drm)

            print(f"ROLL: {carpet_roll}")

            if current_weather.carpet_bombing_drm == 1:
                print("DRM: +1")

            else:
                print("DRM: 0")

            if carpet_result.attack_modifier == ATTACK_CANCELLED:
                print("RESULT: ATTACK CANCELLED")

                current_carpet_bombing = 0

            else:
                current_carpet_bombing = carpet_result.attack_modifier

                print(f"RESULT: {current_carpet_bombing:+} ATTACK STRENGTH")

        print(RESET)

        current_step = 3

        continue

    # =====================================================
    # CALCULATE ATTACK STRENGTHS
    # =====================================================

    if current_step == 3 and user_input == "":
        if current_card is None:
            print()
            print("NO CURRENT CARD")
            print()

            continue

        if current_weather is None:
            print()
            print("NO CURRENT WEATHER")
            print()

            continue

        print_attack_strengths(current_card, current_weather, current_carpet_bombing)

        current_step = 4

        continue

    # =====================================================
    # CANADIAN 1ST ARMY SIEGE ROLL
    # =====================================================

    if current_step == 4 and user_input == "":
        defense_strength = perform_canadian_siege_roll(
            card=current_card,
            weather=current_weather,
            carpet_bombing=current_carpet_bombing,
            defense_strength=defense_strength,
        )

        current_step = 1

        continue
