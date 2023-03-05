def battleship_board_size_chars(board_size):
    board_size_chars = set()
    for i in range(board_size[1]):
        board_size_chars.add(chr(ord('a')+i))
    return board_size_chars

def battleship_board_size_nums(board_size):
    board_size_nums = set(range(1, board_size[0]+1))
    board_size_nums = set(map(lambda x: str(x), board_size_nums))
    return board_size_nums

def battleship_shot_is_in_board(shot, board_size):
    board_size_chars = battleship_board_size_chars(board_size)
    board_size_nums = battleship_board_size_nums(board_size)

    if len(shot) not in [2, 3]: return "Nieprawidłowe współrzędne"
    if len(shot) == 2:
        if ( shot[0] not in board_size_chars or shot[1] not in board_size_nums ) and ( shot[1] not in board_size_chars or shot[0] not in board_size_nums ): return "Nieprawidłowe współrzędne"
    elif len(shot) == 3:
        if ( shot[0] not in board_size_chars or shot[1:] not in board_size_nums ) and ( shot[2] not in board_size_chars or shot[0:2] not in board_size_nums ): return "Nieprawidłowe współrzędne"

    return True

def battleship_shot_is_repeated(player, shot):
    if shot in player["ships_shots_hit"] or shot in player["ships_shots_sunk"] or shot in player["ships_shots_miss"]: return "Strzał w to miejsce był już wykonany"
    return False

def battleship_shot_check(player, shot, board_size):
    '''
    Validation of shot. Return False is something went wront or result in format:
    ["a1", "hit"]
    ["a1", "miss"]
    '''

    board_size_chars = battleship_board_size_chars(board_size)

    shot_is_in_board = battleship_shot_is_in_board(shot, board_size)
    if isinstance(shot_is_in_board, str): return shot_is_in_board

    shot_is_repeated = battleship_shot_is_repeated(player, shot)
    if isinstance(shot_is_repeated, str): return shot_is_repeated

    if shot[0] not in board_size_chars:
        if len(shot) == 2: shot = shot[::-1]
        elif len(shot) == 3: shot = shot[2]+shot[0]+shot[1]

    for ship in player["ships"]:
        if shot in ship: return [shot, "hit"]

    return [shot, "miss"]