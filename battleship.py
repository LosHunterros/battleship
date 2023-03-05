from functions import *
from menu import battleship_menu
from ship_add import battleship_ship_add
from shot_check import battleship_shot_check, battleship_shot_is_ship_sunk
from game_result import battleship_game_result
from get_board import battleship_get_board
from show_game import battleship_show_game

difficulty = {
    "easy" : {
        "board_size" : [5, 5],
        "ships" : [3, 2, 1],
        "name": "Łatwy"
    },
    "medium" : {
        "board_size" : [7, 7],
        "ships" : [3, 3, 2, 2, 1, 1],
        "name": "Średni"
    },
    "hard" : {
        "board_size" : [10, 10],
        "ships" : [4, 3, 3, 3, 2, 2, 2, 1, 1, 1],
        "name": "Trudny"
    }
}

settings = {
    "player1_name": "Player 1",
    "player1_type": "human",        # human / ai
    "player2_name": "Player 2",
    "player2_type": "human",        # human / ai
    "difficulty": "easy"            # easy / medium / hard
}

player_types = {
    "human": "Człowiek",
    "ai": "SI"
}

players = {
    1: {
        "name": settings["player1_name"],
        "type": settings["player1_type"],
        "type_description": player_types[settings["player1_type"]],
        "ships": [],
        "ships_shots_hit": [],
        "ships_shots_sunk": [],
        "ships_shots_miss": []
    },
    2: {
        "name": settings["player2_name"],
        "type": settings["player2_type"],
        "type_description": player_types[settings["player2_type"]],
        "ships": [],
        "ships_shots_hit": [],
        "ships_shots_sunk": [],
        "ships_shots_miss": []
    }
}

while True:

    # Initial parameters

    players[1]["ships"] = []
    players[1]["ships_shots_hit"] = []
    players[1]["ships_shots_sunk"] = []
    players[1]["ships_shots_miss"] = []
    players[2]["ships"] = []
    players[2]["ships_shots_hit"] = []
    players[2]["ships_shots_sunk"] = []
    players[2]["ships_shots_miss"] = []

    settings = battleship_menu(settings, difficulty, players, player_types)

    board_size = difficulty[settings["difficulty"]]["board_size"]
    ships = difficulty[settings["difficulty"]]["ships"]

    players[1]["name"] = settings["player1_name"]
    players[1]["type"] = settings["player1_type"]
    players[1]["type_description"] = player_types[settings["player2_type"]]
    players[2]["name"] = settings["player2_name"]
    players[2]["type"] = settings["player2_type"]
    players[2]["type_description"] = player_types[settings["player2_type"]]

    # Add ships
    for number, player in players.items():

        for ship in ships:
            ship_to_add = False

            while not isinstance(ship_to_add, list):

                text_lines = {
                    6: "Przygotowywanie rozgrywki",
                    7: player["name"] + " Wprowadza statki",
                    9: "Wprowadź statek o długości " + str(ship),
                    10: "Podaj współrzędne pierwszego pola statku"
                }
                board1 = battleship_get_board(players[1], board_size, True)
                board2 = battleship_get_board(players[2], board_size, True)
                battleship_show_game(players, board1, board2, text_lines)
                ship_add_start_coordinates = input_with_quit("Podaj współrzędne pierwszego pola statku: ")

                text_lines = {
                    6: "Przygotowywanie rozgrywki",
                    7: player["name"] + " Wprowadza statki",
                    9: "Wprowadź statek o długości " + str(ship),
                    11: "Podaj położenie statku:",
                    12: "1. Poziome",
                    13: "2. Pionowe"
                }
                board1 = battleship_get_board(players[1], board_size, True)
                board2 = battleship_get_board(players[2], board_size, True)
                battleship_show_game(players, board1, board2, text_lines)
                ship_add_orientation = input_with_quit("Podaj położenie statku: ")

                ship_to_add = battleship_ship_add(player["ships"], ship_add_start_coordinates.lower(), ship_add_orientation, ship, board_size)

                if isinstance(ship_to_add, str):
                    text_lines = {
                        6: "Przygotowywanie rozgrywki",
                        7: player["name"] + " Wprowadza statki",
                        9: ship_to_add,
                        11: "Spróbuj ponownie",
                        12: "Naciśnij enter aby kontynuować"
                    }
                    board1 = battleship_get_board(players[1], board_size, True)
                    board2 = battleship_get_board(players[2], board_size, True)
                    battleship_show_game(players, board1, board2, text_lines)
                    input_with_quit("Naciśnij enter aby kontynuować ")
                    
                else: players[number]["ships"].append(ship_to_add)

    # Begin shooting
    player_active = 1
    player_oponent = 2
    winner = False

    while winner == False:

        shot = False
        while not isinstance(shot, list):
            text_lines = {
                7: "Strzela:",
                9: players[player_active]["name"]
            }
            board1 = battleship_get_board(players[1], board_size)
            board2 = battleship_get_board(players[2], board_size)
            battleship_show_game(players, board1, board2, text_lines)

            shot = input("Podaj współrzędne strzału: ")
            shot = battleship_shot_check(players[player_oponent], shot, board_size)

            if isinstance(shot, str):
                text_lines = {
                    7: "Strzela:",
                    9: players[player_active]["name"],
                    11: shot,
                    12: "Spróbuj ponownie",
                    13: "Naciśnij enter aby kontynuować"
                }
                board1 = battleship_get_board(players[1], board_size)
                board2 = battleship_get_board(players[2], board_size)
                battleship_show_game(players, board1, board2, text_lines)
                input_with_quit("Naciśnij enter aby kontynuować ")

            elif shot[1] == "hit":
                shot_is_ship_sunk = battleship_shot_is_ship_sunk(players[player_oponent], shot[0])
                if shot_is_ship_sunk != None:
                    for ship_part in players[player_oponent]["ships"][shot_is_ship_sunk]:
                        players[player_oponent]["ships_shots_sunk"].append(ship_part)
                    shot_is_ship_sunk_message = " ZATOPIONY!"
                else: shot_is_ship_sunk_message = ""

                players[player_oponent]["ships_shots_hit"].append(shot[0])
                text_lines = {
                    7: "Strzela:",
                    9: players[player_active]["name"],
                    11: "TRAFIONY" + shot_is_ship_sunk_message,
                    13: "Naciśnij enter aby kontynuować"
                }
                board1 = battleship_get_board(players[1], board_size)
                board2 = battleship_get_board(players[2], board_size)
                battleship_show_game(players, board1, board2, text_lines)
                input_with_quit("Naciśnij enter aby kontynuować ")
            elif shot[1] == "miss":
                players[player_oponent]["ships_shots_miss"].append(shot[0])
                text_lines = {
                    7: "Strzela:",
                    9: players[player_active]["name"],
                    11: "Pudło...",
                    13: "Naciśnij enter aby kontynuować"
                }
                board1 = battleship_get_board(players[1], board_size)
                board2 = battleship_get_board(players[2], board_size)
                battleship_show_game(players, board1, board2, text_lines)
                input_with_quit("Naciśnij enter aby kontynuować ")

        winner = battleship_game_result(players[player_oponent])

        if winner == True:
            text_lines = {
                7: "Zwycięża",
                9: players[player_active]["name"],
                11: "GRATULACJE",
                13: "Naciśnij enter aby kontynuować"
            }
            board1 = battleship_get_board(players[1], board_size)
            board2 = battleship_get_board(players[2], board_size)
            battleship_show_game(players, board1, board2, text_lines)
            input_with_quit("Naciśnij enter aby kontynuować ")
        else:
            if player_active == 1:
                player_active = 2
                player_oponent = 1
            else:
                player_active = 1
                player_oponent = 2