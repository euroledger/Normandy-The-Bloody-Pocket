import sys
from random import choice, shuffle, randint
import matplotlib.pyplot as plt
import numpy as np
from core.allied_armies import CANADIAN_FIRST_ARMY

from core.weather import get_weather_result
from core.carpet_bombing import get_carpet_bombing_result
from core.carpet_bombing import ATTACK_CANCELLED

from core.card_utilities import calculate_attack_modifiers, get_armies_as_objects

from core.siege import (calculate_siege_drm, get_siege_result)

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
# CONFIG
# =========================================================

NUM_RUNS = 100000

# DEFENSE_STRENGTHS = [4, 8, 11, 13, 15]
# DEFENSE_STRENGTHS = [11]

# =========================================================
# MID DECK
# =========================================================

mid_deck = [
    card_025, card_026, card_027, card_028, card_029, card_030, card_031,
    card_033, card_035, card_036, card_037, card_043
]

# =========================================================
# LATE DECK
# =========================================================

late_deck = [
    card_032, card_034, card_038, card_039, card_040, card_041, card_042,
    card_044, card_045, card_046, card_047, card_048
]

# =========================================================
# CANADIAN 1ST ARMY SIEGE ROLL
# =========================================================


def perform_canadian_siege_roll(card, weather, carpet_bombing,
                                defense_strength, canada_1_army_cards):

    armies = get_armies_as_objects(card)

    if CANADIAN_FIRST_ARMY not in armies:

        return {
            "siege_ended": False,
            "defense_strength": defense_strength,
            "canada_1_army_cards": canada_1_army_cards
        }

    canada_1_army_cards += 1

    siege_roll = randint(1, 6)

    modified_roll = siege_roll

    canadian_result = calculate_attack_modifiers(
        card=card,
        army=CANADIAN_FIRST_ARMY,
        num_jabos=weather.available_jabos,
        carpet_bombing=carpet_bombing)

    canadian_attack_strength = (canadian_result["attack_strength"])

    has_air_support = (canadian_result["has_air_support"])

    drm_result = calculate_siege_drm(attack_strength=canadian_attack_strength,
                                     defense_strength=defense_strength,
                                     has_air_support=has_air_support)

    modified_roll += drm_result.drm

    modified_roll = max(1, min(6, modified_roll))

    siege_result = get_siege_result(modified_roll)

    if siege_result.combat_steps_eliminated > 0:

        defense_strength -= (siege_result.combat_steps_eliminated)

        defense_strength = max(4, defense_strength)

    if siege_result.space_captured:

        return {"siege_ended": True, "attacks_needed": canada_1_army_cards}

    return {
        "siege_ended": False,
        "defense_strength": defense_strength,
        "canada_1_army_cards": canada_1_army_cards
    }


# =========================================================
# RUN MONTE CARLO
# =========================================================


def run_monte_carlo(starting_defense_strength):

    attacks_needed_results = []

    cards_drawn_results = []

    total_attacks_needed = 0

    total_hits = 0

    total_cards_drawn = 0

    for run_number in range(1, NUM_RUNS + 1):

        if (run_number % 10000 == 0):

            print()
            print(f"RUN {run_number}")
            print()

        cards_drawn = 0

        canada_1_army_cards = 0

        defense_strength = starting_defense_strength

        starting_combat_strength = (defense_strength - 4)

        drawn_cards = []

        mid_deck_added = False

        late_deck_added = False

        current_card = None

        current_weather = None

        current_carpet_bombing = 0

        draw_deck = [
            card_003, card_004, card_005, card_006, card_007, card_008,
            card_009, card_010, card_011, card_012, card_013, card_014,
            card_015, card_016, card_017, card_018, card_019, card_020,
            card_021, card_022, card_023, card_024
        ]

        while True:

            if not draw_deck:
                total_attacks_needed += (canada_1_army_cards)
                total_hits += (starting_combat_strength)
                total_cards_drawn += (cards_drawn)
                break

            drawn_card = choice(draw_deck)
            current_card = drawn_card
            current_weather = None
            current_carpet_bombing = 0
            draw_deck.remove(drawn_card)
            drawn_cards.append(drawn_card)
            cards_drawn += 1

            if (drawn_card.card_id == 20 and not mid_deck_added):

                draw_deck.extend(mid_deck)

                shuffle(draw_deck)

                mid_deck_added = True

            if (drawn_card.card_id == 37 and not late_deck_added):

                draw_deck.extend(late_deck)

                shuffle(draw_deck)

                late_deck_added = True

            weather_roll = randint(1, 6)

            weather = get_weather_result(weather_roll)

            current_weather = weather

            current_carpet_bombing = 0

            if (current_weather.available_jabos > 0
                    and current_card.air_power.has_carpet_bombing()):

                carpet_roll = randint(1, 6)

                carpet_result = (get_carpet_bombing_result(
                    die_roll=carpet_roll,
                    drm=(current_weather.carpet_bombing_drm)))

                if (carpet_result.attack_modifier == ATTACK_CANCELLED):

                    current_carpet_bombing = 0

                else:

                    current_carpet_bombing = (carpet_result.attack_modifier)

            siege_result = (perform_canadian_siege_roll(
                card=current_card,
                weather=current_weather,
                carpet_bombing=(current_carpet_bombing),
                defense_strength=(defense_strength),
                canada_1_army_cards=(canada_1_army_cards)))

            if siege_result["siege_ended"]:

                attacks_needed_results.append(siege_result["attacks_needed"])

                cards_drawn_results.append(cards_drawn)

                total_attacks_needed += (siege_result["attacks_needed"])

                total_hits += (starting_combat_strength)

                total_cards_drawn += (cards_drawn)

                break

            defense_strength = (siege_result["defense_strength"])

            canada_1_army_cards = (siege_result["canada_1_army_cards"])

    print()
    print("===================================")
    print(f"DEFENSE STRENGTH "
          f"{starting_defense_strength}")
    print("===================================")

    print(f"AVG ATTACKS NEEDED="
          f"{total_attacks_needed / NUM_RUNS:.2f}")

    print(f"AVG HITS PER ATTACK="
          f"{total_hits / total_attacks_needed:.2f}")

    print(f"AVG CARDS DRAWN="
          f"{total_cards_drawn / NUM_RUNS:.2f}")

    return {
        "attacks_needed": attacks_needed_results,
        "cards_drawn": cards_drawn_results
    }


# =========================================================
# RUN SIMULATIONS
# =========================================================


results_4 = run_monte_carlo(4)

results_8 = run_monte_carlo(8)

results_11 = run_monte_carlo(11)

results_13 = run_monte_carlo(13)

results_15 = run_monte_carlo(15)

results_21 = run_monte_carlo(21
                             )
# =========================================================
# SUBPLOTS
# =========================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))

# =========================================================
# ATTACKS NEEDED HISTOGRAM
# =========================================================

all_attacks = (results_4["attacks_needed"] + results_8["attacks_needed"] +
               results_11["attacks_needed"] + results_13["attacks_needed"] +
               results_15["attacks_needed"] + results_21["attacks_needed"])

attack_bins = range(min(all_attacks), max(all_attacks) + 2)

ax1.hist(results_4["attacks_needed"],
         bins=attack_bins,
         alpha=0.5,
         label="Defense 4")

ax1.hist(results_8["attacks_needed"],
         bins=attack_bins,
         alpha=0.5,
         label="Defense 8")

ax1.hist(results_11["attacks_needed"],
         bins=attack_bins,
         alpha=0.5,
         label="Defense 11")

ax1.hist(results_13["attacks_needed"],
         bins=attack_bins,
         alpha=0.5,
         label="Defense 13")

ax1.hist(results_15["attacks_needed"],
         bins=attack_bins,
         alpha=0.5,
         label="Defense 15")

ax1.hist(results_21["attacks_needed"],
         bins=attack_bins,
         alpha=0.5,
         label="Defense 21")

mode_4 = max(set(results_4["attacks_needed"]),
             key=results_4["attacks_needed"].count)

mode_8 = max(set(results_8["attacks_needed"]),
             key=results_8["attacks_needed"].count)

mode_11 = max(set(results_11["attacks_needed"]),
              key=results_11["attacks_needed"].count)

mode_13 = max(set(results_13["attacks_needed"]),
              key=results_13["attacks_needed"].count)

mode_15 = max(set(results_15["attacks_needed"]),
              key=results_15["attacks_needed"].count)

mode_21 = max(set(results_21["attacks_needed"]),
              key=results_21["attacks_needed"].count)

attack_mode_x = [mode_4, mode_8, mode_11, mode_13, mode_15, mode_21]

attack_mode_y = [1000, 2000, 3000, 4000, 5000, 6000]

ax1.plot(attack_mode_x,
         attack_mode_y,
         marker="o",
         linewidth=3,
         label="Mode Trend")

ax1.set_xlabel("Number of Attacks Needed")

ax1.set_ylabel("Frequency")

ax1.set_title("Canadian 1st Army Siege Results")

ax1.legend()

# =========================================================
# CARDS DRAWN HISTOGRAM
# =========================================================

all_cards_drawn = (results_4["cards_drawn"] + results_8["cards_drawn"] +
                   results_11["cards_drawn"] + results_13["cards_drawn"] +
                   results_15["cards_drawn"] + results_21["cards_drawn"])

cards_bins = range(min(all_cards_drawn), max(all_cards_drawn) + 2)

ax2.hist(results_4["cards_drawn"],
         bins=cards_bins,
         alpha=0.5,
         label="Defense 4")

ax2.hist(results_8["cards_drawn"],
         bins=cards_bins,
         alpha=0.5,
         label="Defense 8")

ax2.hist(results_11["cards_drawn"],
         bins=cards_bins,
         alpha=0.5,
         label="Defense 11")

ax2.hist(results_13["cards_drawn"],
         bins=cards_bins,
         alpha=0.5,
         label="Defense 13")

ax2.hist(results_15["cards_drawn"],
         bins=cards_bins,
         alpha=0.5,
         label="Defense 15")

ax2.hist(results_21["cards_drawn"],
         bins=cards_bins,
         alpha=0.5,
         label="Defense 21")

mode_4 = max(set(results_4["cards_drawn"]), key=results_4["cards_drawn"].count)

mode_8 = max(set(results_8["cards_drawn"]), key=results_8["cards_drawn"].count)

mode_11 = max(set(results_11["cards_drawn"]),
              key=results_11["cards_drawn"].count)

mode_13 = max(set(results_13["cards_drawn"]),
              key=results_13["cards_drawn"].count)

mode_15 = max(set(results_15["cards_drawn"]),
              key=results_15["cards_drawn"].count)

mode_21 = max(set(results_21["cards_drawn"]),
              key=results_21["cards_drawn"].count)

cards_mode_x = [mode_4, mode_8, mode_11, mode_13, mode_15, mode_21]

cards_mode_y = [1000, 2000, 3000, 4000, 5000, 6000]

ax2.plot(cards_mode_x,
         cards_mode_y,
         marker="o",
         linewidth=3,
         label="Mode Trend")

ax2.set_xlabel("Cards Drawn")

ax2.set_ylabel("Frequency")

ax2.set_title("Cards Drawn Distribution")

ax2.legend()

plt.tight_layout()

plt.show()
mode_15 = max(set(results_15["cards_drawn"]),
              key=results_15["cards_drawn"].count)