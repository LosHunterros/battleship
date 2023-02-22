def battleship_shot_is_in_board(shot, board_size):

    return False

def battleship_shot_is_repeated(player, shot):

    return False

def battleship_shot_check(player, shot, board_size):
    '''
    Validation of shot. Return False is something went wront or result in format:
    ["a1", "hit"]
    ["a1", "miss"]
    '''
    shot = battleship_shot_is_in_board(shot, board_size)
    shot = battleship_shot_is_repeated(player, shot)
    
    return False