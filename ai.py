from random import randint, choice

from ship_add import *
from shot_check import *

def battleship_ai_ship_add(ships, ship_size, board_size):
    ship = ""

    board_size_nums = battleship_board_size_nums(board_size)
    board_size_chars = battleship_board_size_chars(board_size)

    while isinstance(ship, str):

        num = choice(list(board_size_nums))
        char = choice(list(board_size_chars))

        ship = battleship_ship_add(ships, str(char)+str(num), str(randint(1, 2)), ship_size, board_size)

    return ship

def battleship_ai_shot_check(player, board_size):
    shot = ""

    board_size_nums = battleship_board_size_nums(board_size)
    board_size_chars = battleship_board_size_chars(board_size)

    while isinstance(shot, str):

        num = choice(list(board_size_nums))
        char = choice(list(board_size_chars))

        shot = battleship_shot_check(player, str(char)+str(num), board_size)

    return shot