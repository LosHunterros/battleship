from functions import *

def battleship_get_board(player, board_size, show_ships = False):
    '''
    Return board of chosen player
    '''
    board = {}

    for i in range(board_size[1]):
        char = chr(ord('a')+i) + "-1"
        board[char] = {}
        for j in range(1, board_size[0]+1):
            board[char][str(j) + "-1"] = " "
            board[char][str(j) + "-2"] = "┌"
            board[char][str(j) + "-3"] = "┐"
            board[char][str(j) + "-4"] = " "
        char = chr(ord('a')+i) + "-2"
        board[char] = {}
        for j in range(1, board_size[0]+1):
            board[char][str(j) + "-1"] = " "
            board[char][str(j) + "-2"] = "└"
            board[char][str(j) + "-3"] = "┘"
            board[char][str(j) + "-4"] = " "

    if show_ships:
        for ship in player["ships"]:
            for ship_part in ship:
                board[ship_part[0]+"-1"][ship_part[1]+"-1"] = "█"
                board[ship_part[0]+"-1"][ship_part[1]+"-2"] = "█"
                board[ship_part[0]+"-1"][ship_part[1]+"-3"] = "█"
                board[ship_part[0]+"-1"][ship_part[1]+"-4"] = "█"
                board[ship_part[0]+"-2"][ship_part[1]+"-1"] = "█"
                board[ship_part[0]+"-2"][ship_part[1]+"-2"] = "█"
                board[ship_part[0]+"-2"][ship_part[1]+"-3"] = "█"
                board[ship_part[0]+"-2"][ship_part[1]+"-4"] = "█"

    for ship_part in player["ships_shots_hit"]:
        board[ship_part[0]+"-1"][ship_part[1]+"-1"] = "█"
        board[ship_part[0]+"-1"][ship_part[1]+"-2"] = "█"
        board[ship_part[0]+"-1"][ship_part[1]+"-3"] = "█"
        board[ship_part[0]+"-1"][ship_part[1]+"-4"] = "█"
        board[ship_part[0]+"-2"][ship_part[1]+"-1"] = "█"
        board[ship_part[0]+"-2"][ship_part[1]+"-2"] = "█"
        board[ship_part[0]+"-2"][ship_part[1]+"-3"] = "█"
        board[ship_part[0]+"-2"][ship_part[1]+"-4"] = "█"

    for ship_part in player["ships_shots_sunk"]:
        board[ship_part[0]+"-1"][ship_part[1]+"-1"] = "█"
        board[ship_part[0]+"-1"][ship_part[1]+"-2"] = "▀"
        board[ship_part[0]+"-1"][ship_part[1]+"-3"] = "▀"
        board[ship_part[0]+"-1"][ship_part[1]+"-4"] = "█"
        board[ship_part[0]+"-2"][ship_part[1]+"-1"] = "█"
        board[ship_part[0]+"-2"][ship_part[1]+"-2"] = "▄"
        board[ship_part[0]+"-2"][ship_part[1]+"-3"] = "▄"
        board[ship_part[0]+"-2"][ship_part[1]+"-4"] = "█"

    for ship_part in player["ships_shots_miss"]:
        board[ship_part[0]+"-1"][ship_part[1]+"-1"] = " "
        board[ship_part[0]+"-1"][ship_part[1]+"-2"] = "▄"
        board[ship_part[0]+"-1"][ship_part[1]+"-3"] = "▄"
        board[ship_part[0]+"-1"][ship_part[1]+"-4"] = " "
        board[ship_part[0]+"-2"][ship_part[1]+"-1"] = " "
        board[ship_part[0]+"-2"][ship_part[1]+"-2"] = "▀"
        board[ship_part[0]+"-2"][ship_part[1]+"-3"] = "▀"
        board[ship_part[0]+"-2"][ship_part[1]+"-4"] = " "

    first_line = ""
    for i in range(board_size[0]):
        first_line += " " + chr(ord('A')+i) + "  "

    board_height = board_size[1] * 2 + 3
    board_height_target = 23
    board_width_target = 45

    lines_before = ( board_height_target - board_height ) // 2
    lines_after = board_height_target - board_height - lines_before


    board_final = []

    for i in range(lines_before): board_final.append(string_fill(" ", board_width_target))

    board_final.append(string_fill("    " + first_line + " ", board_width_target))
    board_final.append(string_fill("   ┌" + "─" * board_size[0] * 4 + "┐", board_width_target))

    i = 0
    for line in board:
        if i % 2 == 0:
            number = str(int((i+2)/2))
            line_final = f"{number.rjust(2)} │"
        else: line_final = "   │"
        for char in board[line]:
            line_final += board[line][char]
        line_final += "│"
        board_final.append(string_fill(line_final, board_width_target))
        i += 1

    board_final.append(string_fill("   └" + "─" * board_size[0] * 4 + "┘", board_width_target))

    for i in range(lines_after): board_final.append(string_fill(" ", board_width_target))

    for line in board_final:
        print(line)

    return board_final