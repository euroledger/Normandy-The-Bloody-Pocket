from core.allied_armies import (US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY)
from core.actions.actions_helper import can_add_unit_to_space, get_german_controlled_spaces, get_german_units_on_map
from core.models import *
from core.enums import *

# =========================================================
# CARD #39
# TACTICAL REDEPLOYMENT
# =========================================================

card = Card(card_id=39, title="Tactical Redeployment")

# =========================================================
# MILITARY
# =========================================================
card.military.text.append("Redeploy any two units on the map"
                          " (costs no Action; no Resource Checks needed)"
                          " to any other location on the map")

def event():
    for _ in range(2):
        german_units = get_german_units_on_map()
        if not german_units:
            print("NO GERMAN UNITS ON MAP")
            return

        print()
        print("TACTICAL REDEPLOYMENT")
        print("====================")
        print()
        print("SELECT GERMAN UNIT TO REDEPLOY")
        print()

        for index, (space, unit) in enumerate(german_units, start=1):
            print(f"{index}. {unit.name} ({unit.combat_value}) - {space.name}")

        print()
        print("0. FINISH REDEPLOYMENT")

        choice = input("Choice: ").strip()

        if choice == "0":
            return

        if not choice.isdigit():
            print("INVALID CHOICE")
            return

        selected_index = int(choice) - 1
        if selected_index < 0 or selected_index >= len(german_units):
            print("INVALID CHOICE")
            return

        source_space, selected_unit = german_units[selected_index]

        print()
        print(f"SELECTED: {selected_unit.name} FROM {source_space.name}")
        print()

        destination_spaces = get_german_controlled_spaces()

        if not destination_spaces:
            print("NO GERMAN-CONTROLLED DESTINATIONS AVAILABLE")
            return

        print("SELECT GERMAN-CONTROLLED DESTINATION")
        print()

        for index, space in enumerate(destination_spaces, start=1):
            print(f"{index}. {space.name}")

        print()
        print("0. CANCEL REDEPLOYMENT")

        destination_choice = input("Choice: ").strip()

        if destination_choice == "0":
            return

        if not destination_choice.isdigit():
            print("INVALID CHOICE")
            return

        destination_index = int(destination_choice) - 1
        if destination_index < 0 or destination_index >= len(destination_spaces):
            print("INVALID CHOICE")
            return

        destination_space = destination_spaces[destination_index]

        if not can_add_unit_to_space(destination_space, selected_unit):
            print("STACKING LIMIT REACHED, INVALID MOVE")
            return

        source_space.units.remove(selected_unit)
        destination_space.units.append(selected_unit)

        print()
        print(f"{selected_unit.name} REDEPLOYED FROM {source_space.name} TO {destination_space.name}")
        

card.event = event

card.military.formations.extend(
    [US_FIRST_ARMY, US_THIRD_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY])

# =========================================================
# AIR POWER
# =========================================================

card.air_power.effects.append(

    # +1 Jabos 2nd BRIT
    Effect(modifier_type=ModifierType.AIR_POWER,
           value=1,
           target=BRITISH_SECOND_ARMY))

# =========================================================
# RESOURCES
# ==================== =====================================

card.resources.effects.append(

    # Lose 1 Supply
    Effect(modifier_type=ModifierType.RESOURCE_LOSS,
           value=-1,
           resource_type=ResourceType.SUPPLY))

# =========================================================
# ACTIONS
# =========================================================

card.actions.actions_available = 1
