from core.card_utilities import calculate_attack_modifiers

def assert_attack_strengths(test_case, armies, expected_attack_strengths, card,
                            expected_has_air_support=None, num_jabos=0, carpet_bombing=0, print_modifiers=False):

    if expected_has_air_support is None:
        expected_has_air_support = {}
    for army in armies:
        army_name = army.name if hasattr(army, "name") else army

        if army_name not in expected_attack_strengths:
            raise AssertionError(f"No expected attack strength for {army_name}")

        result = calculate_attack_modifiers(card=card, army=army, num_jabos=num_jabos,
                                            carpet_bombing=carpet_bombing, print_modifiers=print_modifiers)

        attack_strength = result["attack_strength"]
        has_air_support = result["has_air_support"]

        test_case.assertEqual(attack_strength, expected_attack_strengths[army_name])
        test_case.assertEqual(has_air_support, expected_has_air_support[army_name])
