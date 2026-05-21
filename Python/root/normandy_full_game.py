import sys
from random import shuffle, randint
from cards.decks import draw_deck, mid_deck, late_deck
from core.weather import get_weather_result
from core.resources import do_resource_phase
from core.carpet_bombing import get_carpet_bombing_result, ATTACK_CANCELLED
from core.map.map_utilities import do_opening_setup
from core.game_summary import print_game_summary
from core.card_utilities import calculate_attack_modifiers, get_armies
from core.siege import calculate_siege_drm, get_siege_result

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

do_opening_setup()

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
        result = calculate_attack_modifiers(card=card,
                                            army=army,
                                            num_jabos=num_jabos,
                                            carpet_bombing=carpet_bombing,
                                            print_modifiers=True)
        print(result)

    print(RESET)


def perform_canadian_siege_roll(card, weather, carpet_bombing,
                                defense_strength):
    global canada_1_army_cards

    print(CYAN)
    print()
    print("========================================")
    print("CANADIAN 1ST ARMY SIEGE ROLL")
    print("========================================")
    print()

    armies = get_armies(card)

    if "1st CAN" not in armies:
        print("\t=>NO ROLL")
        print(RESET)
        return defense_strength

    canada_1_army_cards += 1

    siege_roll = randint(1, 6)
    modified_roll = siege_roll

    canadian_result = calculate_attack_modifiers(
        card=card,
        army="1st CAN",
        num_jabos=weather.available_jabos,
        carpet_bombing=carpet_bombing)

    canadian_attack_strength = canadian_result["attack_strength"]
    has_air_support = canadian_result["has_air_support"]

    drm_result = calculate_siege_drm(attack_strength=canadian_attack_strength,
                                     defense_strength=defense_strength,
                                     has_air_support=has_air_support)

    modified_roll += drm_result.drm

    print(
        f"DEFENSE-ATTACK DIFFERENTIAL: {defense_strength - canadian_attack_strength}"
    )

    for reason in drm_result.reasons:
        print(f"DRM: {reason}")

    modified_roll = max(1, min(6, modified_roll))

    siege_result = get_siege_result(modified_roll)

    print()
    print(f"BASE ROLL: {siege_roll}")
    print(f"MODIFIED ROLL: {modified_roll}")
    print()
    print(f"RESULT: {siege_result.result_type.value}")

    if siege_result.combat_steps_eliminated > 0:
        steps_elim = min(defense_strength - 4,
                         siege_result.combat_steps_eliminated)

        print(f"COMBAT STEPS ELIMINATED: {steps_elim}")

        defense_strength -= siege_result.combat_steps_eliminated
        defense_strength = max(4, defense_strength)

    print()
    print(f"\t=>DEFENSE STRENGTH: {defense_strength}")

    if siege_result.space_captured:
        avg_hits_per_attack = starting_combat_strength / canada_1_army_cards

        print("SPACE CAPTURED - END OF SIEGE")
        print(
            f"=> NUMBER OF ATTACKS NEEDED TO END SIEGE={canada_1_army_cards}")
        print(f"=> HITS PER ATTACK={avg_hits_per_attack:.2f}")

        sys.exit("Bye")

    print(RESET)

    return defense_strength


while True:
    print()
    print("========================================")
    print("NORMANDY - THE BLOODY POCKET")
    print("========================================")
    print()

    print(f"Cards Drawn: {cards_drawn}")
    print(f"Defense Strength: {defense_strength}")
    print(f"Canadian 1st Army Attacks: {canada_1_army_cards}")

    if drawn_cards:
        drawn_ids = [str(card.card_id) for card in drawn_cards]
        print(f"List of Drawn Cards: ({', '.join(drawn_ids)})")
    else:
        print("List of Drawn Cards: []")

    cards_remaining = 48 - cards_drawn

    print(f"Cards Remaining: {cards_remaining}")
    print(f"Cards Remaining in Deck: {len(draw_deck)}")

    print()

    if current_card:
        print(f"Current Card: {current_card.card_id}")

    if current_weather:
        print(f"Current Weather: {current_weather.weather_type.value}")

    print()

    if current_step == 1:
        print(f"{GREEN}> Draw Card{RESET}")
    else:
        print(f"{RED}  Draw Card{RESET}")

    if current_step == 2:
        print(f"{GREEN}> Roll For Weather{RESET}")
    else:
        print(f"{RED}  Roll For Weather{RESET}")

    if current_step == 3:
        print(f"{GREEN}> Resource Phase{RESET}")
    else:
        print(f"{RED}  Resource Phase{RESET}")

    if current_step == 4:
        print(f"{GREEN}> Calculate Attack Strengths{RESET}")
    else:
        print(f"{RED}  Calculate Attack Strengths{RESET}")

    if current_step == 5:
        print(f"{GREEN}> Canadian 1st Army Siege Roll{RESET}")
    else:
        print(f"{RED}  Canadian 1st Army Siege Roll{RESET}")

    print()
    print("Press ENTER to perform next action")
    print("Press S to see game summary")
    print("Press Q to quit")
    print()

    user_input = input("> ").strip().upper()

    if user_input == "Q":
        print("Goodbye.")
        break

    if user_input == "S":
        print_game_summary()
        print()
        input("Press ENTER to continue...")
        continue

    if current_step == 1 and user_input == "":
        if not draw_deck:
            print()
            print("DRAW DECK EMPTY")
            continue

        drawn_card = draw_deck[0]

        current_card = drawn_card
        current_weather = None
        current_carpet_bombing = 0

        draw_deck.remove(drawn_card)

        drawn_cards.append(drawn_card)

        cards_drawn += 1

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

        input("Press ENTER to continue...")

        current_step = 2

        continue

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

        if current_weather.available_jabos > 0 and current_card.air_power.has_carpet_bombing(
        ):
            print()
            print("========================================")
            print("CARPET BOMBING")
            print("========================================")
            print()

            carpet_roll = randint(1, 6)

            carpet_result = get_carpet_bombing_result(
                die_roll=carpet_roll, drm=current_weather.carpet_bombing_drm)

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

        input("Press ENTER to continue...")

        current_step = 3

        continue

    if current_step == 3 and user_input == "":
        do_resource_phase(current_weather.weather_type)

        input("Press ENTER to continue...")
        current_step = 4
        continue

    if current_step == 4 and user_input == "":
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

        print_attack_strengths(current_card, current_weather,
                               current_carpet_bombing)

        input("Press ENTER to continue...")

        current_step = 5

        continue

    if current_step == 5 and user_input == "":
        defense_strength = perform_canadian_siege_roll(
            card=current_card,
            weather=current_weather,
            carpet_bombing=current_carpet_bombing,
            defense_strength=defense_strength)

        input("Press ENTER to continue...")

        current_step = 1

        continue
