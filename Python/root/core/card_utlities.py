from core.enums import ModifierType
from core.weather import ALL_JABOS_AVAILABLE


from core.enums import ModifierType
from core.weather import ALL_JABOS_AVAILABLE


def print_modifiers(card):
    modifiers = card.get_action_modifiers()

    print(f"\nMODIFIERS CARD {card.card_id} - {card.title}")

    for modifier in modifiers:
        print(
            f"  "
            f"{modifier['modifier_type'].name:<20} "
            f"value={modifier['value']:<2} "
            f"target={modifier['target']} "
            f"label={modifier['label']}"
        )
        
from core.enums import ModifierType
from core.weather import ALL_JABOS_AVAILABLE


from core.enums import ModifierType
from core.weather import ALL_JABOS_AVAILABLE


def calculate_attack_modifiers(card, army, num_jabos=0, carpet_bombing=0):

    army_name = army.name if hasattr(army, "name") else army
    modifiers = card.get_action_modifiers()

    total_attack_strength = 0
    attack_breakdown = []

    # =========================================================
    # JABOS
    # =========================================================

    jabo_strength = 0

    if num_jabos > 0:

        # CLEAR WEATHER
        # ALL JABOS AVAILABLE

        if num_jabos == ALL_JABOS_AVAILABLE:

            for effect in card.air_power.effects:

                if (
                    effect.modifier_type == ModifierType.AIR_POWER
                    and effect.target.name == army_name
                ):
                    jabo_strength += effect.value

        # PARTLY CLEAR
        # ONLY ONE JABO AVAILABLE

        else:

            first_air_power_target = None

            for effect in card.air_power.effects:

                if effect.modifier_type == ModifierType.AIR_POWER:
                    first_air_power_target = effect.target.name
                    break

            if army_name == first_air_power_target:
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

        if target != army_name:
            continue

        if modifier_type == ModifierType.ATTACK_STRENGTH:
            total_attack_strength += value
            attack_breakdown.append(f"{value:+} Card modifier")

        if modifier_type == ModifierType.COMMANDER:
            total_attack_strength += value
            attack_breakdown.append(f"{value:+} {label}")

    print(
        f"{army_name} "
        f"-> ATTACK STRENGTH: {total_attack_strength} "
        f"({', '.join(attack_breakdown)})"
    )

    return {
        "attack_strength": total_attack_strength,

        "has_air_support": (
            jabo_strength > 0
            or carpet_bombing > 0
        )
    }