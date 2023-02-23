from functions import *
from menu import battleship_menu
from ship_add import battleship_ship_add
from shot_check import battleship_shot_check
from game_result import battleship_game_result

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

settings = {
    "player1_name": "Player 1",
    "player1_type": "human",        # human / ai
    "player2_name": "Player 2",
    "player2_type": "human",        # human / ai
    "difficulty": "easy"            # easy / medium / hard
}

while True:

    # Initial parameters
    settings = battleship_menu(settings, difficulty)

    board_size = difficulty[settings["difficulty"]]["board_size"]
    ships = difficulty[settings["difficulty"]]["ships"]

    players = {
        1: {
            "name": settings["player1_name"],
            "type": settings["player1_type"],
            "ships": [],
            "ships_shots_hit": [],
            "ships_shots_miss": []
        },
        2: {
            "name": settings["player1_name"],
            "type": settings["player1_type"],
            "ships": [],
            "ships_shots_hit": [],
            "ships_shots_miss": []
        }
    }

    # Add ships
    for number, player in players.items():

        for ship in ships:
            ship_to_add = False

            while ship_to_add == False:
                ship_add_start_coordinates = input(player["name"] + ": Podaj współrzędne pierwszego pola statku o długości " + ship +": ")
                ship_add_orintation = input("Podaj Podaj orientację statku. 1 - pozioma ; 2 - pionowa: ")

                ship_to_add = battleship_ship_add(player, ship_add_start_coordinates, ship_add_orintation, ship, board_size)

                if ship_to_add == False: print("Błędne parametry, spróbuj ponownie")
                else: players[number]["ships"].append(ship_to_add)

    # Begin shooting
    player_active = 1
    player_oponent = 2
    winner = False

    while winner == False:

        shot = False
        while shot == False:
            shot = input(players[player_active]["name"] + ": Podaj współrzędne strzału: ")
            shot = battleship_shot_check(players[player_oponent], shot, board_size)

            if shot == False: print("Błędne parametry, spróbuj ponownie")
            elif shot[1] == "hit": players[player_oponent]["ships_shots_hit"].append(shot[0])
            elif shot[1] == "miss": players[player_oponent]["ships_shots_miss"].append(shot[0])

        winner = battleship_game_result(players[player_oponent])

        if winner == True:
            print("Zwycięża " + players[player_active]["name"])
        else:
            if player_active == 1:
                player_active == 2
                player_oponent == 1
            else:
                player_active == 1
                player_oponent == 2