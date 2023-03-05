from shot_check import *

def battleship_ship_add(ships, start_coordinates, orientation, ship_size, board_size):
    '''
    Ads ship to player at game start.
    Function return list with coordinates of all ship fields in format:
    ship = ["a1", "a2", "a3", "a4"]
    If error (out of board size or too close to other ship) return error message
    '''
    ship = []

    board_size_chars = battleship_board_size_chars(board_size)

    shot_is_in_board = battleship_shot_is_in_board(start_coordinates, board_size)
    if isinstance(shot_is_in_board, str): return shot_is_in_board

    if orientation != "1" and orientation != "2": return "Nieprawidłowe położenie"

    if start_coordinates[0] not in board_size_chars:
        if len(start_coordinates) == 2: start_coordinates = start_coordinates[::-1]
        elif len(start_coordinates) == 3: start_coordinates = start_coordinates[2]+start_coordinates[0]+start_coordinates[1]

    if orientation == "1":
        if int(start_coordinates[1]) + ship_size - 1 > board_size[1]: return "Statek nie mieści się na planszy"
        for i in range(ship_size):
            start_coordinates_increment = str(int(start_coordinates[1:]) + i)
            ship_string = start_coordinates[0] + start_coordinates_increment

            for ship_old in ships:
                if ship_string in ship_old: return "Współrzędne zajęte"
                if chr(ord(start_coordinates[0]) + 1 ) + start_coordinates_increment in ship_old: return "Zbyt blisko innego statku"
                if chr(ord(start_coordinates[0]) - 1 ) + start_coordinates_increment in ship_old: return "Zbyt blisko innego statku"
                if start_coordinates[0] + str(int(start_coordinates_increment) + 1 ) in ship_old: return "Zbyt blisko innego statku"
                if start_coordinates[0] + str(int(start_coordinates_increment) - 1 ) in ship_old: return "Zbyt blisko innego statku"

            ship.append(ship_string)

    elif orientation == "2":
        if ord(start_coordinates[0]) + ship_size > ord("a") + board_size[0]: return "Statek nie mieści się na planszy"
        for i in range(ship_size):
            start_coordinates_increment = chr(ord(start_coordinates[0]) + i)
            ship_string = start_coordinates_increment + start_coordinates[1:]

            for ship_old in ships:
                if ship_string in ship_old: return "Współrzędne zajęte"
                if chr(ord(start_coordinates_increment) + 1 ) + start_coordinates[1:] in ship_old: return "Zbyt blisko innego statku"
                if chr(ord(start_coordinates_increment) - 1 ) + start_coordinates[1:] in ship_old: return "Zbyt blisko innego statku"
                if start_coordinates_increment + str(int(start_coordinates[1:]) + 1 ) in ship_old: return "Zbyt blisko innego statku"
                if start_coordinates_increment + str(int(start_coordinates[1:]) - 1 ) in ship_old: return "Zbyt blisko innego statku"

            ship.append(ship_string)

    return ship