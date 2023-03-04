from functions import *
from get_board import battleship_get_board
from show_game import battleship_show_game

def battleship_menu(settings, difficulty, players, player_types):
    '''
    Alow users to set their own setting.
    Function accepts current settings and return users settings in same format:
    settings = {
        "player1_name": "Player 1",
        "player1_type": "human",        # human / ai
        "player2_name": "Player 2",
        "player2_type": "human",        # human / ai
        "difficulty": "easy"            # easy / medium / hard
    }
    '''
    operation = ""

    while operation != "1":
        text_lines = {
            2: "W grze uczestniczą:",
            4: settings["player1_name"] + " jako " + player_types[settings["player1_type"]],
            5: settings["player2_name"] + " jako " + player_types[settings["player2_type"]],
            7: "Poziom trudności: " + difficulty[settings["difficulty"]]["name"] + "",
            10: "Menu:",
            12: "1. Graj",
            13: "2. Zmień ustawienia dla: " + settings["player1_name"] + "",
            14: "3. Zmień ustawienia dla: " + settings["player2_name"] + "",
            15: "4. Zmień poziom trudności"
        }
        board1 = battleship_get_board(players[1], difficulty[settings["difficulty"]]["board_size"])
        board2 = battleship_get_board(players[2], difficulty[settings["difficulty"]]["board_size"])
        battleship_show_game(players, board1, board2, text_lines)

        operation = input_with_quit("Wybierz opcję z menu: ")

        if operation == "2" or operation == "3":
            operation_player = 0
            if operation == "2": operation_player_number = "1"
            if operation == "3": operation_player_number = "2"

            while operation_player != "3":
                text_lines = {
                    6: "Zmień ustawienia dla: " + settings["player"+operation_player_number+"_name"] + " - " + player_types[settings["player"+operation_player_number+"_type"]],
                    8: "1. Zmień nick",
                    9: "2. Zmień typ gracza (człowiek/SI)",
                    10: "3. Powrót do menu głównego"
                }
                board1 = battleship_get_board(players[1], difficulty[settings["difficulty"]]["board_size"])
                board2 = battleship_get_board(players[2], difficulty[settings["difficulty"]]["board_size"])
                battleship_show_game(players, board1, board2, text_lines)

                operation_player = input_with_quit("Wybierz opcję z menu: ")

                if operation_player == "1":
                    operation_player_name = ""

                    while operation_player_name == "":
                        text_lines = {
                            7: "Zmień ustawienia dla: " + settings["player"+operation_player_number+"_name"] + " - " + player_types[settings["player"+operation_player_number+"_type"]],
                            9: "Zmień nick"
                        }
                        board1 = battleship_get_board(players[1], difficulty[settings["difficulty"]]["board_size"])
                        board2 = battleship_get_board(players[2], difficulty[settings["difficulty"]]["board_size"])
                        battleship_show_game(players, board1, board2, text_lines)
                        
                        operation_player_name = input_with_quit("Wprowadź nowy nick: ")

                        if operation_player_name != "":
                            settings["player" + operation_player_number + "_name"] = operation_player_name
                            players[int(operation_player_number)]["name"] = operation_player_name

                if operation_player == "2":
                    operation_player_type = ""

                    while operation_player_type != "1" and operation_player_type != "2":
                        text_lines = {
                            6: "Zmień ustawienia dla: " + settings["player"+operation_player_number+"_name"] + " - " + player_types[settings["player"+operation_player_number+"_type"]],
                            8: "Zmień typ gracza (człowiek/SI)",
                            10: "1. Człowiek",
                            11: "2. SI"
                        }
                        board1 = battleship_get_board(players[1], difficulty[settings["difficulty"]]["board_size"])
                        board2 = battleship_get_board(players[2], difficulty[settings["difficulty"]]["board_size"])
                        battleship_show_game(players, board1, board2, text_lines)

                        operation_player_type = input_with_quit("Wybierz opcję z menu: ")

                        if operation_player_type == "1":
                            settings["player" + operation_player_number + "_type"] = "human"
                            players[int(operation_player_number)]["type"] = "human"
                            players[int(operation_player_number)]["type_description"] = player_types["human"]
                        elif operation_player_type == "2":
                            settings["player" + operation_player_number + "_type"] = "ai"
                            players[int(operation_player_number)]["type"] = "ai"
                            players[int(operation_player_number)]["type_description"] = player_types["ai"]

        if operation == "4":
            operation_difficulty = ""
            operation_difficulty_values = []

            while not operation_difficulty.isdigit() or int(operation_difficulty) not in range(1, len(difficulty)+1):
                clear()
                print("Witaj w grze - Zmień poziom trudności")

                text_lines = {
                    6: "Zmień poziom trudności",
                }

                i = 1
                for diff in difficulty:
                    text_lines[7+i] = str(i) + ". " + difficulty[diff]["name"]
                    operation_difficulty_values.append(diff)
                    i += 1

                board1 = battleship_get_board(players[1], difficulty[settings["difficulty"]]["board_size"])
                board2 = battleship_get_board(players[2], difficulty[settings["difficulty"]]["board_size"])
                battleship_show_game(players, board1, board2, text_lines)

                operation_difficulty = input_with_quit("Wybierz opcję z menu: ")

                if operation_difficulty.isdigit() and int(operation_difficulty) in list(range(1, len(difficulty)+1)): settings["difficulty"] = operation_difficulty_values[int(operation_difficulty)-1]

    return settings