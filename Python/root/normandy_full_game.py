from random import shuffle, randint
from cards.decks import draw_deck, mid_deck, late_deck
from core.actions import do_action_phase
from core.military import do_military_phase
from core.save_load_game import load_game, save_game
from core.weather import get_weather_result
from core.resources import do_resource_phase_drms, do_resource_phase_reinforcements
from core.carpet_bombing import get_carpet_bombing_result, ATTACK_CANCELLED
from core.map.map_utilities import do_opening_setup
from core.game_summary import print_game_summary
from core.global_game_state import GlobalGameState

from core.card_utilities import (
    calculate_attack_modifiers,
    get_all_defending_armies,
    get_armies_as_objects,
    calculate_defense_modifiers,
)

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


do_opening_setup()

opening_cards = draw_deck[:2]
random_cards = draw_deck[2:]

shuffle(random_cards)

draw_deck[:] = opening_cards + random_cards


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

    for army in armies:
        calculate_attack_modifiers(
            card=card,
            army=army,
            num_jabos=weather.available_jabos,
            carpet_bombing=carpet_bombing,
            print_modifiers=True,
        )

    print(RESET)


def print_defense_strengths(card, weather):
    print(CYAN)
    print()
    print("========================================")
    print("DEFENSE STRENGTHS")
    print("========================================")
    print()

    if GlobalGameState.cards_drawn == 0:
        print()
        print("N/A")
        print()

    armies = get_all_defending_armies()

    print("********** DEFENDING ARMIES=", armies)

    for army in armies:
        calculate_defense_modifiers(
            card=card,
            army=army,
            weather=weather,
            print_modifiers=True,
        )


while True:
    print()
    print("========================================")
    print("NORMANDY - THE BLOODY POCKET")
    print("========================================")
    print()

    print(f"Cards Drawn: {GlobalGameState.cards_drawn}")

    if GlobalGameState.drawn_cards:
        drawn_ids = [str(card.card_id) for card in GlobalGameState.drawn_cards]

        print(f"List of Drawn Cards: ({', '.join(drawn_ids)})")
    else:
        print("List of Drawn Cards: []")

    cards_remaining = 48 - GlobalGameState.cards_drawn

    print(f"Cards Remaining: {cards_remaining}")
    print(f"Cards Remaining in Deck: {len(draw_deck)}")

    print()

    if GlobalGameState.current_card:
        print(f"Current Card: {GlobalGameState.current_card.card_id}")

    if GlobalGameState.current_weather:
        print(f"Current Weather: {GlobalGameState.current_weather.weather_type.value}")

    print()

    menu_items = [
        "Draw Card",
        "Roll For Weather",
        "Resource Phase",
        "Deploy Non Panzer Div Reinforcements",
        "Military Phase",
        "Action Phase",
    ]

    for index, text in enumerate(menu_items, start=1):
        if GlobalGameState.current_step == index:
            print(f"{GREEN}> {text}{RESET}")
        else:
            print(f"{RED}  {text}{RESET}")

    print()
    print("Press ENTER to perform next action")
    print("Press G to see game summary")

    can_save_game = (
        GlobalGameState.current_step == 1
        and GlobalGameState.current_card is not None
    )

    can_load_game = GlobalGameState.current_step == 1

    if can_save_game:
        print("Press S to save game")

    if can_load_game:
        print("Press L to load saved game")

        print("Press Q to quit")
        print()

    user_input = input("> ").strip().upper()

    if user_input == "Q":
        print("Goodbye.")
        break

    if user_input == "G":
        print_game_summary()
        print()
        input("Press ENTER to continue...")
        continue

    if user_input == "S" and can_save_game:
        save_game()
        print()
        input("Press ENTER to continue...")
        continue

    if user_input == "L" and can_load_game:
        load_game()
        print()
        input("Press ENTER to continue...")
        continue

    if GlobalGameState.current_step == 1 and user_input == "":
        if not draw_deck:
            print()
            print("DRAW DECK EMPTY")
            continue

        drawn_card = draw_deck[0]

        GlobalGameState.current_card = drawn_card
        GlobalGameState.current_weather = None
        GlobalGameState.current_carpet_bombing = 0

        draw_deck.remove(drawn_card)
        GlobalGameState.drawn_cards.append(drawn_card)
        GlobalGameState.cards_drawn += 1

        if drawn_card.card_id == 20 and not GlobalGameState.mid_deck_added:
            draw_deck.extend(mid_deck)
            shuffle(draw_deck)
            GlobalGameState.mid_deck_added = True

            print(CYAN)
            print()
            print("========================================")
            print("MID DECK ADDED")
            print("DRAW DECK SHUFFLED")
            print("========================================")
            print(RESET)

        if drawn_card.card_id == 37 and not GlobalGameState.late_deck_added:
            draw_deck.extend(late_deck)
            shuffle(draw_deck)
            GlobalGameState.late_deck_added = True

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
        GlobalGameState.current_step = 2
        continue

    if GlobalGameState.current_step == 2 and user_input == "":
        weather_roll = randint(1, 6)

        weather = get_weather_result(weather_roll)

        GlobalGameState.current_weather = weather
        GlobalGameState.current_carpet_bombing = 0

        print(CYAN)
        print()
        print("========================================")
        print("WEATHER ROLL")
        print("========================================")
        print()

        print(f"ROLL: {weather_roll}")
        print(f"RESULT: {weather.weather_type.value}")

        if (
            GlobalGameState.current_weather.available_jabos > 0
            and GlobalGameState.current_card.air_power.has_carpet_bombing()
        ):
            print()
            print("========================================")
            print("CARPET BOMBING")
            print("========================================")
            print()

            carpet_roll = randint(1, 6)

            carpet_result = get_carpet_bombing_result(
                die_roll=carpet_roll,
                drm=GlobalGameState.current_weather.carpet_bombing_drm,
            )

            print(f"ROLL: {carpet_roll}")

            if GlobalGameState.current_weather.carpet_bombing_drm == 1:
                print("DRM: +1")
            else:
                print("DRM: 0")

            if carpet_result.attack_modifier == ATTACK_CANCELLED:
                print("RESULT: ATTACK CANCELLED")
                GlobalGameState.current_carpet_bombing = 0
            else:
                GlobalGameState.current_carpet_bombing = carpet_result.attack_modifier
                print(f"RESULT: {GlobalGameState.current_carpet_bombing:+} ATTACK STRENGTH")

        print(RESET)
        input("Press ENTER to continue...")
        GlobalGameState.current_step = 3
        continue

    if GlobalGameState.current_step == 3 and user_input == "":
        do_resource_phase_drms(
            GlobalGameState.current_weather.weather_type,
            GlobalGameState.current_card,
        )
        print(f"RESOURCE PHASE - weather is {GlobalGameState.current_weather.weather_type.value}\n")
        print_attack_strengths(
            GlobalGameState.current_card,
            GlobalGameState.current_weather,
            GlobalGameState.current_carpet_bombing,
        )
        print_defense_strengths(
            GlobalGameState.current_card,
            GlobalGameState.current_weather,
        )
        print(CYAN)
        do_resource_phase_reinforcements(GlobalGameState.current_card)
        print(RESET)
        input("Press ENTER to continue...")
        GlobalGameState.current_step = 4
        continue

    if GlobalGameState.current_step == 4 and user_input == "":
        # TBD will be used when we have Nebelwerfer, Flak or Kampfgruppen to deploy
        print(CYAN)
        print("NONE")
        print(RESET)
        input("Press ENTER to continue...")
        GlobalGameState.current_step = 5
        continue

    if GlobalGameState.current_step == 5 and user_input == "":
        print(CYAN)
        do_military_phase(
            GlobalGameState.current_card,
            GlobalGameState.current_weather,
        )
        print(RESET)
        input("Press ENTER to continue...")
        GlobalGameState.current_step = 6
        continue

    if GlobalGameState.current_step == 6 and user_input == "":
        print(CYAN)
        do_action_phase(
            GlobalGameState.current_card,
            GlobalGameState.current_weather,
        )
        print(RESET)
        input("Press ENTER to continue...")
        GlobalGameState.current_step = 1
        continue
