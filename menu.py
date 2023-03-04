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
            5: settings["player1_name"] + " jako " + player_types[settings["player1_type"]],
            7: "Poziom trudności: " + difficulty[settings["difficulty"]]["name"] + "",
            10: "Menu:",
            12: "1. Graj",
            13: "2. Zmień ustawienia player 1",
            14: "3. Zmień ustawienia player 2",
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
                clear()
                print("Witaj w grze - Zmień ustawienia player " + operation_player_number + "")
                print("1. Zmień nick")
                print("2. Ustaw człowiek lub SI")
                print("3. Powrót do głównego menu")

                operation_player = input_with_quit("Wybierz opcję z menu: ")

                if operation_player == "1":
                    operation_player_name = ""

                    while operation_player_name == "":
                        clear()
                        print("Witaj w grze - Zmień nick player " + operation_player_number + "")
                        
                        operation_player_name = input_with_quit("Wprowadz nick dla player " + operation_player_number + ": ")

                        if operation_player_name != "": settings["player" + operation_player_number + "_name"] = operation_player_name

                if operation_player == "2":
                    operation_player_type = ""

                    while operation_player_type != "1" and operation_player_type != "2":
                        clear()
                        print("Witaj w grze - Zmień type dla player " + operation_player_number + "")
                        print("1. Człowiek")
                        print("2. SI")
                        
                        operation_player_type = input_with_quit("Wybierz z menu typ gracza: ")

                        if operation_player_type == "1": settings["player" + operation_player_number + "_type"] = "human"
                        elif operation_player_type == "2": settings["player" + operation_player_number + "_type"] = "ai"

        if operation == "4":
            operation_difficulty = ""
            operation_difficulty_values = []

            while not operation_difficulty.isdigit() or int(operation_difficulty) not in range(1, len(difficulty)+1):
                clear()
                print("Witaj w grze - Zmień poziom trudności")
                
                i = 1
                for diff in difficulty:
                    print(str(i) + ". " + difficulty[diff]["name"])
                    operation_difficulty_values.append(diff)
                    i += 1

                operation_difficulty = input_with_quit("Wybierz opcję z menu: ")

                if operation_difficulty.isdigit() and int(operation_difficulty) in list(range(1, len(difficulty)+1)): settings["difficulty"] = operation_difficulty_values[int(operation_difficulty)-1]

    return settings