from core.allied_armies import BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_FIRST_ARMY, US_THIRD_ARMY, US_VIII_CORPS, US_XV_CORPS
from core.enums import ModifierType, ResourceType
from core.weather import ALL_JABOS_AVAILABLE
from core.map.map_model import TerrainType, transport_track, supply_track, hitler_approval_track


def print_modifiers(card):
    modifiers = card.get_action_modifiers()

    print(f"\nMODIFIERS CARD {card.card_id} - {card.title}")

    for modifier in modifiers:
        print(f"  {modifier['modifier_type'].name:<20} value={modifier['value']:<2} target={modifier['target']} label={modifier['label']}")


def get_modifier_target(army):
    if army in [US_VIII_CORPS, US_XV_CORPS]:
        return US_THIRD_ARMY
    return army


def calculate_attack_modifiers(card, army, num_jabos=0, carpet_bombing=0, print_modifiers=False):
    modifiers = card.get_action_modifiers()
    total_attack_strength = 0
    attack_breakdown = []

    modifier_target = get_modifier_target(army)

    print("\n==============================")
    print("CALCULATE ATTACK MODIFIERS")
    print("==============================")
    print("army =", army)
    # print("num_jabos =", num_jabos)
    print("modifier_target =", modifier_target)

    # =========================================================
    # JABOS
    # =========================================================

    jabo_strength = 0
    if num_jabos > 0:

        # CLEAR WEATHER
        # ALL JABOS AVAILABLE
        if num_jabos == ALL_JABOS_AVAILABLE:
            for effect in card.air_power.effects:
                if effect.modifier_type == ModifierType.AIR_POWER and modifier_target == effect.target:
                    jabo_strength += effect.value

        # PARTLY CLEAR
        # ONLY ONE JABO AVAILABLE
        else:
            first_air_power_target = None

            for effect in card.air_power.effects:
                if effect.modifier_type == ModifierType.AIR_POWER:
                    first_air_power_target = effect.target
                    break
            if army == first_air_power_target:
                jabo_strength = num_jabos

    if jabo_strength > 0:
        total_attack_strength += jabo_strength
        attack_breakdown.append(f"{jabo_strength:+} Jabo")

    # =========================================================
    # CARPET BOMBING
    # =========================================================

    if carpet_bombing > 0:
        total_attack_strength += carpet_bombing
        attack_breakdown.append(f"{carpet_bombing:+} Carpet Bombing")

    # =========================================================
    # CARD MODIFIERS
    # =========================================================

    for modifier in modifiers:
        modifier_type = modifier["modifier_type"]
        target = modifier["target"]
        value = modifier["value"]
        label = modifier["label"]

        if target != modifier_target:
            continue

        if modifier_type == ModifierType.ATTACK_STRENGTH:
            total_attack_strength += value
            attack_breakdown.append(f"{value:+} Card modifier")

        if modifier_type == ModifierType.COMMANDER:
            total_attack_strength += value
            attack_breakdown.append(f"{value:+} {label}")

    has_air_support = jabo_strength > 0 or carpet_bombing > 0

    if print_modifiers:
        print(f"{army.name} -> ATTACK STRENGTH: {total_attack_strength} ({', '.join(attack_breakdown)}) ; AIR SUPPORT={has_air_support}")

    return {"attack_strength": total_attack_strength, "has_air_support": has_air_support}


def calculate_defense_modifiers(card, army, weather, print_modifiers=False):
    modifiers = card.get_action_modifiers()
    terrain_strength = army.location.terrain_value
    army_strength = army.strength
    num_jabos = weather.available_jabos
    total_defense_strength = terrain_strength + army_strength
    defense_breakdown = [f"{terrain_strength:+} Terrain", f"{army_strength:+} Army"]

    # =========================================================
    # JABOS
    # =========================================================

    jabo_strength = 0

    modifier_target = get_modifier_target(army)

    if num_jabos > 0:
        # CLEAR WEATHER
        # ALL JABOS AVAILABLE
        if num_jabos == ALL_JABOS_AVAILABLE:
            for effect in card.air_power.effects:
                if effect.modifier_type == ModifierType.AIR_POWER and effect.target == modifier_target:
                    jabo_strength += effect.value

        # PARTLY CLEAR
        # ONLY ONE JABO AVAILABLE
        else:
            first_air_power_target = None
            for effect in card.air_power.effects:
                if effect.modifier_type == ModifierType.AIR_POWER:
                    first_air_power_target = effect.target
                    break

            if army == first_air_power_target:
                jabo_strength = num_jabos

    if jabo_strength > 0:
        total_defense_strength += jabo_strength
        defense_breakdown.append(f"{jabo_strength:+} Jabo")

    # =========================================================
    # CARD MODIFIERS
    # =========================================================

    print("\nCARD MODIFIERS")
    print("modifier_target =", modifier_target)

    for modifier in modifiers:
        modifier_type = modifier["modifier_type"]
        target = modifier["target"]
        value = modifier["value"]
        label = modifier["label"]

        # if target != army:
        #     continue

        print("modifier:", modifier_type, "target=", target, "value=", value)

        if target != modifier_target:
            print("SKIP")
            continue

        if modifier_type == ModifierType.DEFENSE_STRENGTH:
            total_defense_strength += value
            defense_breakdown.append(f"{value:+} Defense modifier")

        if modifier_type == ModifierType.COMMANDER:
            total_defense_strength += value
            defense_breakdown.append(f"{value:+} {label}")

    has_air_support = jabo_strength > 0

    if print_modifiers:
        print(f"{army.name} -> DEFENSE STRENGTH: {total_defense_strength} ({', '.join(defense_breakdown)}) ; AIR SUPPORT={has_air_support}")

    return {"defense_strength": total_defense_strength, "has_air_support": has_air_support}


def get_armies_as_objects(card):
    armies = []
    for army in card.military.formations:
        if army == US_THIRD_ARMY and not army.merged:
            armies.extend([US_VIII_CORPS, US_XV_CORPS])
        else:
            armies.append(army)
    return armies


# def get_armies(card):
#     armies = get_armies_as_objects(card)
#     return [army.name for army in armies]


def get_armies(card):
    print("GET ARMIES!")
    armies = []
    for army in get_armies_as_objects(card):
        print("ARMY:", army, "merged=", army.merged)
        if army == US_THIRD_ARMY and not army.merged:
            armies.extend([US_VIII_CORPS.name, US_XV_CORPS.name])
        else:
            armies.append(army.name)
    return armies


def get_all_defending_armies():
    armies = []

    for army in [US_FIRST_ARMY, BRITISH_SECOND_ARMY, CANADIAN_FIRST_ARMY, US_THIRD_ARMY]:
        if army.location is None:
            continue

        if army.location.terrain == TerrainType.START_BOX or army.location.terrain == TerrainType.FORTRESS:
            continue

        armies.append(army)

    return armies


# def get_armies(card):
#     return [
#         formation.name
#         for formation in card.military.formations
#     ]


def adjust_resource_track(track, amount):

    track.value += amount

    if track.value > track.maximum:
        track.value = track.maximum

    if track.value < track.minimum:
        track.value = track.minimum


def apply_resource_modifiers(card):
    for effect in card.resources.effects:
        if effect.modifier_type not in [ModifierType.RESOURCE_LOSS, ModifierType.RESOURCE_GAIN]:
            continue

        if effect.resource_type == ResourceType.TRANSPORT:
            adjust_resource_track(transport_track, effect.value)
        elif effect.resource_type == ResourceType.SUPPLY:
            adjust_resource_track(supply_track, effect.value)
        elif effect.resource_type == ResourceType.HITLER_APPROVAL:
            adjust_resource_track(hitler_approval_track, effect.value)
