def battleship_game_result(player):
    '''
    Check if all ships are destroyed. If yes return True, if no return False
    '''
    ships_parts = 0

    for ship in player["ships"]:
        ships_parts += len(ship)

    if len(player["ships_shots_hit"]) == ships_parts: return True

    return False