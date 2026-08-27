from core.global_game_state import GlobalGameState


def do_move_action_point_to_strategic_reserve():
    print("MOVE ACTION POINT TO STRATEGIC RESERVE")
    print()

    if GlobalGameState.actions_left_this_turn < 1:
        print("NO ACTIONS AVAILABLE")
        return

    if GlobalGameState.reserve_actions >= 2:
        print("STRATEGIC RESERVE IS FULL (TWO RESERVE ACTIONS)")
        return

    GlobalGameState.actions_left_this_turn -= 1
    GlobalGameState.reserve_actions += 1

    print("1 ACTION MOVED TO STRATEGIC RESERVE")
    print(f"ACTIONS REMAINING: {GlobalGameState.actions_left_this_turn}")
    print(f"RESERVE ACTIONS: {GlobalGameState.reserve_actions}")
