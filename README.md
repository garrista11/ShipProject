# ShipGameProject

Contains a script for the ShipGame project written in Python.

This is a program that has similar rules to the game Battle Ship, and it played by entering commands into the terminal. Players are able to place an unlimited number of on their own 10 x 10 grid, and are then able to take turns firing at each other's ships until either player wins the game by sinking all of the opposing player's ships. Upon placing a ship successfully or firing a torpedo successfully, the program will return True. If a ship has an invalid placement, the program will return False and not place the ship. If an invalid torpedo is fired, the program will also return False and the current player will still need to take their turn. The rules are as follows:

- A player's ships may not overlap with any of their other ships
- A player's ships must fit on the 10 x 10 grid
- Player's must take turns firing at the opposing player's board ('first' player always goes first)
- A player wins once the opposing player has 0 ships remaining
- Turns may not be taken after a player has won
