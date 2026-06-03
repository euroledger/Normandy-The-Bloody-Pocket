import sys
from random import shuffle, randint
from cards.decks import draw_deck, mid_deck, late_deck
from core.military import do_military_phase
from core.weather import get_weather_result
from core.resources import do_resource_phase_drms, do_resource_phase_reinforcements
from core.carpet_bombing import get_carpet_bombing_result, ATTACK_CANCELLED
from core.map.map_utilities import do_opening_setup
from core.game_summary import print_game_summary
from core.card_utilities import calculate_attack_modifiers, get_all_defending_armies, get_armies_as_objects, calculate_defense_modifiers

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

do_opening_setup()

opening_cards = draw_deck[:2]
random_cards = draw_deck[2:]

shuffle(random_cards)

draw_deck[:] = opening_cards + random_cards

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
    print("ATTACK STRENGTHS (ALLIED ARMIES)")
    print("========================================")
    print()
    armies = get_armies_as_objects(card)

    if not armies:
        print("\t=>NO ARMIES ATTACKING")
        print(RESET)
        return

    num_jabos = weather.available_jabos

    for army in armies:
        calculate_attack_modifiers(card=card, army=army, num_jabos=num_jabos, carpet_bombing=carpet_bombing, print_modifiers=True)

    print(RESET)


def print_defense_strengths(card, weather):
    print(CYAN)
    print()
    print("========================================")
    print("DEFENSE STRENGTHS")
    print("========================================")
    print()

    if cards_drawn == 0:
        print()
        print("N/A")
        print()
        # turn 1 no defense strength

    # get all armies except inactive US 3rd Army and any army in start box or on beach after turn 2

    armies = get_all_defending_armies()

    print("********** DEFENDING ARMIES=", armies)
    for army in armies:
        calculate_defense_modifiers(card=card, army=army, weather=weather, print_modifiers=True)


while True:
    print()
    print("========================================")
    print("NORMANDY - THE BLOODY POCKET")
    print("========================================")
    print()

    print(f"Cards Drawn: {cards_drawn}")

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
        print(f"{GREEN}> Deploy Non Panzer Div Reinforcements{RESET}")
    else:
        print(f"{RED}  Deploy Non Panzer Div Reinforcements{RESET}")
    if current_step == 5:
        print(f"{GREEN}> Military Phase{RESET}")
    else:
        print(f"{RED}  Military Phase{RESET}")
    # if current_step == 5:
    #     print(f"{GREEN}> Canadian 1st Army Siege Roll{RESET}")
    # else:
    #     print(f"{RED}  Canadian 1st Army Siege Roll{RESET}")

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

        input("Press ENTER to continue...")

        current_step = 3

        continue

    if current_step == 3 and user_input == "":
        do_resource_phase_drms(current_weather.weather_type, current_card)

        print(f"RESOURCE PHASE - weather is {current_weather.weather_type.value}\n")

        print_attack_strengths(current_card, current_weather, current_carpet_bombing)
        print_defense_strengths(current_card, current_weather)

        print(CYAN)
        do_resource_phase_reinforcements(current_card)
        print(RESET)
        input("Press ENTER to continue...")
        current_step = 4

        continue

    if current_step == 4 and user_input == "":
        # TBD will be used when we have Nebelwerfer, Flak or Kampfgruppen to deploy
        print(CYAN)
        print("NONE")
        print(RESET)

        input("Press ENTER to continue...")
        current_step = 5
        continue

    if current_step == 5 and user_input == "":
        print(CYAN)
        do_military_phase(current_card, current_weather)
        print(RESET)
        input("Press ENTER to continue...")
        current_step = 1
        continue

