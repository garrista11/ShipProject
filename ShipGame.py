# Author: Taylor Garrison
# Github username: garrista11
# Date: 04/04/2022
# Description: This script contains two classes which are used to play the Ship Game (Battleship). This game is played
# by two players wherein the players first place ships on their individual boards. Players can place as many ships of
# any length on their boards before beginning the game, however ships may not share the same spaces and they must fit
# on the board (which is 10x10). After players place their ships, they will take turns firing at each other's boards
# (with the 'first' player going first). Player's must take their turns in order, with one player firing a shot per
# turn, until one of the player's has no ships remaining, at which the other player wins.


class Ship:
    """Represents a Ship object, which has a length, a list containing the spaces it occupies, and a status (either sunk
    or not sunk). Used by the ShipGame class to represent individual ships."""

    def __init__(self, length):
        """Creates a Ship object and takes the ship length as a parameter. Initializes spaces_in to an empty list and
        the status to NOT_SUNK."""
        self._length = length
        self._spaces_in = []
        self._status = "NOT_SUNK"

    def get_length(self):
        """Returns the length of the Ship."""
        return self._length

    def get_status(self):
        """Returns the status of the Ship."""
        return self._status

    def record_hit(self, space):
        """Takes a coordinate that the ship occupies as a parameter and removes that space from the ships occupied
        spaces and the decrements the ships length by 1. Used to record a successful hit on a Ship."""
        self._spaces_in.remove(space)
        self._length -= 1

    def get_spaces_in(self):
        """Returns a list containing the spaces a Ship occupies."""
        return self._spaces_in

    def add_space_in(self, space):
        """Takes as a parameter a space the ship has been determined to occupy and adds it to the list containing the
        coordinates a ship is in."""
        self._spaces_in.append(space)

    def check_if_sunk(self):
        """Takes no parameters and checks to see if the length of the ship is 0. If it is, the status of the ship is
        changed to "SUNK" and returns True. Otherwise, returns False."""
        if self._length == 0:
            self._status = "SUNK"
            return True
        else:
            return False


class ShipGame:
    """Represents the ShipGame, which is a two player game similar to BattleShip. The game has parameters for the state
    of the game, the current player's turn, the number of ships remaining for both players, a list containing the first
    and second player's Ship objects, and a grid representing each player's boards (stored as a list of lists)."""

    def __init__(self):
        """Creates a ShipGame object which takes no parameters and initializes the game_state to 'UNFINISHED',
        the player's turn. """
        self._current_state = "UNFINISHED"
        self._whose_turn = "first"
        self._fp_ships_remaining = 0
        self._sp_ships_remaining = 0
        self._fp_ships = []
        self._sp_ships = []
        self._fp_grid = [
            ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['A', '', '', '', '', '', '', '', '', '', ''],
            ['B', '', '', '', '', '', '', '', '', '', ''],
            ['C', '', '', '', '', '', '', '', '', '', ''],
            ['D', '', '', '', '', '', '', '', '', '', ''],
            ['E', '', '', '', '', '', '', '', '', '', ''],
            ['F', '', '', '', '', '', '', '', '', '', ''],
            ['G', '', '', '', '', '', '', '', '', '', ''],
            ['H', '', '', '', '', '', '', '', '', '', ''],
            ['I', '', '', '', '', '', '', '', '', '', ''],
            ['J', '', '', '', '', '', '', '', '', '', ''],
        ]
        self._sp_grid = [
            ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['A', '', '', '', '', '', '', '', '', '', ''],
            ['B', '', '', '', '', '', '', '', '', '', ''],
            ['C', '', '', '', '', '', '', '', '', '', ''],
            ['D', '', '', '', '', '', '', '', '', '', ''],
            ['E', '', '', '', '', '', '', '', '', '', ''],
            ['F', '', '', '', '', '', '', '', '', '', ''],
            ['G', '', '', '', '', '', '', '', '', '', ''],
            ['H', '', '', '', '', '', '', '', '', '', ''],
            ['I', '', '', '', '', '', '', '', '', '', ''],
            ['J', '', '', '', '', '', '', '', '', '', ''],
        ]

    def get_whose_turn(self):
        """Returns the player whose turn it is."""
        return self._whose_turn

    def get_current_state(self):
        """Returns the game state."""
        return self._current_state

    def get_fp_ships(self):
        """Returns the first player's grid."""
        return self._fp_ships

    def get_sp_ships(self):
        """Returns the second player's grid."""
        return self._sp_ships

    def get_num_ships_remaining_ships(self, player):
        """Takes a player as a parameter and returns that player's remaining ships."""
        if player == 'first':
            return self._fp_ships_remaining
        else:
            return self._sp_ships_remaining

    def get_fp_grid(self):
        """Returns the first player's grid."""
        for sublist in self._fp_grid:
            print(sublist)

    def get_sp_grid(self):
        """Returns the second player's grid."""
        for sublist in self._sp_grid:
            print(sublist)

    def add_fp_ship(self, ship_length, coord, orientation):
        """Takes the length of the ship, the starting coordinate, and it's orientation as parameters. Uses the
        validate_ship method to determine if the placement is valid, and if it is, adds it to the first player's
        board, creates a Ship object, and adds it to the first player's list."""
        row = coord[0]
        column = coord[1]
        player = 'first'
        if self.validate_ship(player, ship_length, row, column, orientation):
            new_ship = Ship(ship_length)
            self._fp_ships.append(new_ship)
            self._fp_ships_remaining += 1
            if orientation == 'R':
                for sublist in self._fp_grid:
                    if sublist[0] == row:
                        for index in range(ship_length):
                            sublist[index + int(column)] = 'x'
                            new_ship.add_space_in(str(row) + str(index + int(column)))
                        return True
                    else:
                        continue

            elif orientation == 'C':
                row_index = 0
                for sublist in self._fp_grid:
                    if sublist[0] == row:
                        for next_row in range(ship_length):
                            self._fp_grid[row_index + next_row][int(column)] = 'x'
                            new_ship.add_space_in(str(self._fp_grid[row_index + next_row][0]) + str(column))
                        return True
                    else:
                        row_index += 1

        else:
            return False

    def add_sp_ship(self, ship_length, coord, orientation):
        """Takes the length of the ship, the starting coordinate, and it's orientation as parameters. Uses the
        validate_ship method to determine if the placement is valid, and if it is, adds it to the second player's
        board, creates a Ship object, and adds it to the second player's list."""
        row = coord[0]
        column = coord[1]
        player = 'second'
        if self.validate_ship(player, ship_length, row, column, orientation):
            new_ship = Ship(ship_length)
            self._sp_ships.append(new_ship)
            self._sp_ships_remaining += 1
            if orientation == 'R':
                for sublist in self._sp_grid:
                    if sublist[0] == row:
                        for index in range(ship_length):
                            sublist[index + int(column)] = 'x'
                            new_ship.add_space_in(str(row) + str(index + int(column)))
                        return True
                    else:
                        continue
            elif orientation == 'C':
                row_index = 0
                for sublist in self._sp_grid:
                    if sublist[0] == row:
                        for next_row in range(ship_length):
                            self._sp_grid[row_index + next_row][int(column)] = 'x'
                            new_ship.add_space_in(str(self._sp_grid[row_index + next_row][0]) + str(column))
                        return True
                    else:
                        row_index += 1
        else:
            return False

    def validate_ship(self, player, length, row, column, orientation):
        """Used by the place ship method to determine if a ship placement is valid. Takes the player placing the ship,
        the length, row, and column of the ship, and the ship's orientation. Returns True if the placement is valid,
        otherwise returns False."""
        if length < 2:
            return False
        if player == 'first':
            if orientation == 'R':
                needed_row = 0
                for sublist in self._fp_grid:
                    if row == sublist[0]:
                        needed_row = sublist
                if len(needed_row) < length + int(column):
                    return False
                for index in range(length):
                    if needed_row[index + int(column)] == 'x':
                        return False
                return True
            elif orientation == "C":
                row_index = 0
                for sublist in self._fp_grid:
                    if row == sublist[0]:
                        if len(self._fp_grid) < row_index + length:
                            return False
                        else:
                            for index in range(length):
                                if self._fp_grid[row_index][index] == 'x':
                                    return False
                                else:
                                    continue
                    else:
                        row_index += 1
                return True
        elif player == 'second':
            if orientation == 'R':
                needed_row = 0
                for sublist in self._sp_grid:
                    if row == sublist[0]:
                        needed_row = sublist
                if len(needed_row) < length + int(column):
                    return False
                for index in range(length):
                    if needed_row[index + int(column)] == 'x':
                        return False
                return True
            elif orientation == "C":
                row_index = 0
                for sublist in self._sp_grid:
                    if row == sublist[0]:
                        if len(self._sp_grid) < row_index + length:
                            return False
                        else:
                            for index in range(length):
                                if self._sp_grid[row_index][index] == 'x':
                                    return False
                                else:
                                    continue
                    else:
                        row_index += 1
                return True

    def place_ship(self, player, ship_length, coord, orientation):
        """Allows a player to place a ship. The player must enter who is placing a ship, the length of the ship, the
        coordinates of the ship, and the orientation of the ship."""
        if player == 'first':
            return self.add_fp_ship(ship_length, coord, orientation)
        elif player == 'second':
            return self.add_sp_ship(ship_length, coord, orientation)
        else:
            return False

    def fire_torpedo(self, player, coord):
        """Allows a player to fire a torpedo at the opposing player. Takes the player taking the shot and the
        coordinate they want to hit as parameters. Returns True if the shot is valid, otherwise returns False using
        the validate_torpedo method."""

        if self.validate_torpedo(player):
            row = coord[0]
            column = coord[1]
            if player == 'first':
                row_index = 0
                for sublist in self._fp_grid:
                    if sublist[0] == row:
                        if self._sp_grid[row_index][int(column)] == 'x':
                            self._sp_grid[row_index][int(column)] = '*'
                            for ship in self._sp_ships:
                                if coord in ship.get_spaces_in():
                                    ship.record_hit(coord)
                                    if ship.check_if_sunk():
                                        self._sp_ships_remaining -= 1
                                        if self._sp_ships_remaining == 0:
                                            self._current_state = "FIRST_WON"
                                            return True
                                        else:
                                            self._whose_turn = 'second'
                                            return True
                                    else:
                                        self._whose_turn = 'second'
                                        return True
                                else:
                                    continue
                        else:
                            self._whose_turn = 'second'
                            return True

                    else:
                        row_index += 1
            else:
                row_index = 0
                for sublist in self._fp_grid:
                    if sublist[0] == row:
                        if self._fp_grid[row_index][int(column)] == 'x':
                            self._fp_grid[row_index][int(column)] = '*'
                            for ship in self._fp_ships:
                                if coord in ship.get_spaces_in():
                                    ship.record_hit(coord)
                                    if ship.check_if_sunk():
                                        self._fp_ships_remaining -= 1
                                        if self._fp_ships_remaining == 0:
                                            self._current_state = "SECOND_WON"
                                            return True
                                        else:
                                            self._whose_turn = 'first'
                                            return True
                                    else:
                                        self._whose_turn = 'first'
                                        return True
                                else:
                                    continue
                        else:
                            self._whose_turn = 'first'
                            return True
                    else:
                        row_index += 1
        else:
            return False

    def validate_torpedo(self, player):
        """Used by the fire_torpedo method to see if the shot is valid. Takes the player making the shot as a parameter.
        Checks to see if the player matches the current player's turn, and that the game is ongoing. Returns True if
        both conditions are True, otherwise returns False."""
        if self._whose_turn != player:
            return False
        elif self._current_state != "UNFINISHED":
            return False
        else:
            return True