from core.card_utilities import calculate_attack_modifiers

def assert_attack_strengths(
    test_case,
    armies,
    expected_attack_strengths,
    card,
    num_jabos=0,
    carpet_bombing=0,
    expected_has_air_support=None,
    print_modifiers=False
):
    for army in armies:
        if army not in expected_attack_strengths:
            continue
        result = calculate_attack_modifiers(
            card=card,
            army=army,
            num_jabos=num_jabos,
            carpet_bombing=carpet_bombing,
            print_modifiers=print_modifiers
        )
        attack_strength = result["attack_strength"]
        has_air_support = result["has_air_support"]
        test_case.assertEqual(
            attack_strength,
            expected_attack_strengths[army]
        )
        
        if expected_has_air_support:
            test_case.assertEqual(
                has_air_support,
                expected_has_air_support[army]
        )
        
    print("\n")

