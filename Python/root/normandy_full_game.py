from random import shuffle, randint
from cards.decks import draw_deck, mid_deck, late_deck
from core.actions.actions_menu import do_action_phase
from core.actions.strategic_reserve_actions import do_move_other_unit_from_strategic_reserve, get_other_units_in_strategic_reserve
from core.allied_advances_phase import do_allied_advances_phase
from core.game_constants import CYAN, GREEN, RED, RESET
from core.save_load_game import load_game, save_game
from core.tables.weather import get_weather_result
from core.resources import do_event, do_resource_phase_adjustments, do_resource_phase_drms, do_resource_phase_reinforcements
from core.tables.carpet_bombing import get_carpet_bombing_result, ATTACK_CANCELLED
from core.map.map_utilities import do_opening_setup
from core.game_summary import print_game_summary
from core.global_game_state import GlobalGameState
from datetime import datetime


# Cards Drawn: 7
# List of Drawn Cards: (1, 2, 9, 18, 22, 8, 3)
# Cards Remaining: 41
# Cards Remaining in Deck: 17

from core.card_utilities import (
    calculate_attack_modifiers,
    get_all_defending_armies,
    get_armies_as_objects,
    calculate_defense_modifiers,
    remove_model,
    remove_rommel,
    remove_wittmann,
    remove_meyer
)


GAME_WON = "won"
GAME_LOST = "lost"
GAME_CONTINUES = None

do_opening_setup()

opening_cards = draw_deck[:2]
random_cards = draw_deck[2:]

shuffle(random_cards)

# TEST MICHAEL WITTMANN CARD 9
# from cards.card_9 import card as card_009

# random_cards[0] = card_009

# TEST ROMMEL CARD
from cards.card_8 import card as card_008

random_cards[0] = card_008

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


from core.map.map_model import hitler_approval_track


def check_for_game_end():
    if hitler_approval_track.value == -2:
        print()
        print("========================================")
        print("HITLER APPROVAL HAS FALLEN TO -2")
        print("YOU ARE RELIEVED OF COMMAND")
        print()
        print("YOU LOSE!")
        print("========================================")
        return GAME_LOST

    if GlobalGameState.cards_drawn == 48:
        return GAME_WON
    return GAME_CONTINUES


def print_defense_strengths(card, weather):
    print(CYAN)
    print()
    print("========================================")
    print("DEFENSE STRENGTHS (ALLIED ARMIES)")
    print("========================================")
    print()

    if GlobalGameState.cards_drawn == 0:
        print()
        print("N/A")
        print()

    armies = get_all_defending_armies()

    for army in armies:
        calculate_defense_modifiers(
            card=card,
            army=army,
            weather=weather,
            print_modifiers=True,
        )


while True:
    print()
    print("=========================================")
    print("NORMANDY SOLITAIRE! D-Day to Falaise 1944")
    print("=========================================")
    print()

    print(f"Cards Drawn: {len(GlobalGameState.drawn_cards)}")

    game_result = check_for_game_end()
    if game_result == GAME_LOST:
        break

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
        "Resources Phase",
        "Deploy Non Panzer Div Reinforcements",
        "Allied Advances Phase",
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

    can_save_game = GlobalGameState.current_step == 1 and GlobalGameState.current_card is not None

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
        if cards_remaining == 0:
            print()
            print("DRAW DECK EMPTY")
            break

        drawn_card = draw_deck[0]

        GlobalGameState.current_card = drawn_card
        GlobalGameState.current_weather = None
        GlobalGameState.current_carpet_bombing = 0

        draw_deck.remove(drawn_card)
        GlobalGameState.drawn_cards.append(drawn_card)

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
        if GlobalGameState.current_card.card_id == 13: # Great Storm
            weather = get_weather_result(1)
            weather_roll = "N/A"
        else:
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
        do_event(GlobalGameState.current_card)
        do_resource_phase_adjustments(GlobalGameState.current_card)
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
        while get_other_units_in_strategic_reserve():
            choice = input("Deploy a non-Panzer unit from Strategic Reserve? (Y/N): ").strip().lower()
            if choice != "y":
                break
            deployed = do_move_other_unit_from_strategic_reserve()
            if not deployed:
                break
        GlobalGameState.current_step = 5
        continue
    if GlobalGameState.current_step == 5 and user_input == "":
        print(CYAN)
        do_allied_advances_phase(
            GlobalGameState.current_card,
            GlobalGameState.current_weather,
        )
        print(RESET)
        # input("Press ENTER to continue...")
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

        # AutoSave game at end of each turn
        save_name = (f"{datetime.now():%y-%m-%d}-end-turn{GlobalGameState.cards_drawn}-card{GlobalGameState.current_card.card_id}").upper()

        GlobalGameState.cards_drawn += 1

        remove_wittmann()
        remove_meyer()
        remove_rommel()
        remove_model()

        GlobalGameState.current_step = 1
        GlobalGameState.counter_attacked_armies.clear()

        if GlobalGameState.monte_carlo == False:
            save_game(save_name )
        continue

print()
print("========================================")
print("GAME OVER")
print()

if game_result == GAME_WON:
    print("You won!")
else:
    print("You lost!")

print("========================================")
