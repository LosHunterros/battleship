from functions import *

settings = {
    "player1_name": "Player 1",
    "player1_type": "human",        # human / ai
    "player2_name": "Player 2",
    "player2_type": "human",        # human / ai
    "difficulty": "easy"            # easy / medium / hard
}

difficulty = {
    "easy" : {
        "board_size" : [5, 5],
        "ships" : [3, 2, 1]
    },
    "medium" : {
        "board_size" : [7, 7],
        "ships" : [3, 3, 2, 2, 1, 1]
    },
    "hard" : {
        "board_size" : [10, 10],
        "ships" : [4, 3, 3, 3, 2, 2, 2, 1, 1, 1]
    }
}

def battleship_menu(settings, difficulty):
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
    clear()

    result = 0

    while result != "1" and result != "Quit":
        print("Witaj w grze")
        print("Wybierz opcję z menu")
        print("Player 1: nick " + settings["player1_name"] + " ; człowiek/SI: " + settings["player1_type"])
        print("Wybierz opcję z menu")
        print("1. Graj")
        print("2. Zmień ustawienia player 1")
        print("3. Zmień ustawienia player 2")
        print("4. Zmień poziom trudności")
        print("Wpisz 'Quit' aby zakończyć grę")

        if result == "2":
            result_player_1 = 0
            clear()
            print("Witaj w grze - Zmień ustawienia player 1")
            print("1. Zmień nick")
            print("2. Ustaw człowiek lub SI")
            print("3. Powrót do głównego menu")

            result_player_1 = input("Wybierz opcję z menu: ")

            if result_player_1 == "1":
                clear()
                print("Witaj w grze - Zmień nick player 1")
                
                result_player_1_nick = input("Wprowadz nick dla player 1: ")

                if result_player_1_nick == "":
                    result_player_1 = "1"
                else:
                    result_player_1 = "0"
                    settings["player1_name"] = result_player_1_nick
            
            if result_player_1 == "3":
                result_player_1 == 0

        if result == "3":
            zmienna = 1

        if result == "4":
            mienna = 1

        result = input("Wybierz opcję z menu: ")

    return settings

battleship_menu(settings, difficulty)