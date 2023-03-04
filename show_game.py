import time
from random import randint

from functions import *

def battleship_show_game(players, board1, board2, text_lines = {}):
    '''
    Show actual stat of the game with messages and boards
    How to configure

    Messages to users
    text_lines = {
        0: "", // string of skip this index
        1: "", // string of skip this index
        2: "", // string of skip this index
        3: "", // string of skip this index
        4: "", // string of skip this index
        5: "", // string of skip this index
        6: "", // string of skip this index
        7: "", // string of skip this index
        8: "", // string of skip this index
        9: "", // string of skip this index
        10: "", // string of skip this index
        11: "", // string of skip this index
        12: "", // string of skip this index
        13: "", // string of skip this index
        14: "", // string of skip this index
        15: "", // string of skip this index
        16: "", // string of skip this index
        17: ""  // string of skip this index
    }
    '''

    # Validating argument text_lines
    i = 0
    while i < 18:
        try:
            if not isinstance(text_lines[i], str):
                text_lines[i] = ""
        except:
            text_lines[i] = ""
        i += 1

    quit_info = "Wpisz 'Quit' aby zakończyć grę"
    player_1_description = players[1]["name"] + " - " + players[1]["type_description"] + ""
    player_2_description = players[2]["name"] + " - " + players[2]["type_description"] + ""

    # Filled template from which chars will be taken to successive "frames" of animation
    graphic = [
        "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄",
        "█                                                                                                                                                     █",
        "█       █▀▌  █  ▀█▀ ▀█▀ █  █▀▀ ▐▀█ █ █ █ ██▄ ▐▀█         " + string_fill(player_1_description, 45) + "  " + string_fill(player_2_description, 45) + " █",
        "█       █▄█ ▐ ▌  █   █  █  █   █▄  █▄█ █ █ █ █▄                                                                                                       █",
        "█       █ █ █▄█  █   █  █  █▀   ▀█ █▀█ █ █▀▀  ▀█         " + board1[0] +                             "  " + board2[0] +                             " █",
        "█       █▄▌ █ █  █   █  ██ █▄▄ █▄▌ █ █ █ █   █▄▌         " + board1[1] +                             "  " + board2[1] +                             " █",
        "█                                                        " + board1[2] +                             "  " + board2[2] +                             " █",
        "█ "+string_fill(text_lines[0], 52)+                  "   " + board1[3] +                             "  " + board2[3] +                             " █",
        "█ "+string_fill(text_lines[1], 52)+                  "   " + board1[4] +                             "  " + board2[4] +                             " █",
        "█ "+string_fill(text_lines[2], 52)+                  "   " + board1[5] +                             "  " + board2[5] +                             " █",
        "█ "+string_fill(text_lines[3], 52)+                  "   " + board1[6] +                             "  " + board2[6] +                             " █",
        "█ "+string_fill(text_lines[4], 52)+                  "   " + board1[7] +                             "  " + board2[7] +                             " █",
        "█ "+string_fill(text_lines[5], 52)+                  "   " + board1[8] +                             "  " + board2[8] +                             " █",
        "█ "+string_fill(text_lines[6], 52)+                  "   " + board1[9] +                             "  " + board2[9] +                             " █",
        "█ "+string_fill(text_lines[7], 52)+                  "   " + board1[10] +                            "  " + board2[10] +                            " █",
        "█ "+string_fill(text_lines[8], 52)+                  "   " + board1[11] +                            "  " + board2[11] +                            " █",
        "█ "+string_fill(text_lines[9], 52)+                  "   " + board1[12] +                            "  " + board2[12] +                            " █",
        "█ "+string_fill(text_lines[10], 52)+                 "   " + board1[13] +                            "  " + board2[13] +                            " █",
        "█ "+string_fill(text_lines[11], 52)+                 "   " + board1[14] +                            "  " + board2[14] +                            " █",
        "█ "+string_fill(text_lines[12], 52)+                 "   " + board1[15] +                            "  " + board2[15] +                            " █",
        "█ "+string_fill(text_lines[13], 52)+                 "   " + board1[16] +                            "  " + board2[16] +                            " █",
        "█ "+string_fill(text_lines[14], 52)+                 "   " + board1[17] +                            "  " + board2[17] +                            " █",
        "█ "+string_fill(text_lines[15], 52)+                 "   " + board1[18] +                            "  " + board2[18] +                            " █",
        "█ "+string_fill(text_lines[16], 52)+                 "   " + board1[19] +                            "  " + board2[19] +                            " █",
        "█ "+string_fill(text_lines[17], 52)+                 "   " + board1[20] +                            "  " + board2[20] +                            " █",
        "█                                                        " + board1[21] +                            "  " + board2[21] +                            " █",
        "█ "+string_fill(quit_info, 52)+                      "   " + board1[22] +                            "  " + board2[22] +                            " █",
        "█                                                                                                                                                     █",
        "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
    ]

    clear()
    print("\n".join(map(lambda x: ("").join(x), graphic)))