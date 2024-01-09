import sys
from helper import *
from board import *
from car import *

directions = ["u", "d", "l", "r"]
colors = ["Y", "B", "O", "W", "G", "R"]
TARGET_LOCATION = (3, 7)
VERTICAL = 0
HORIZONTAL = 1


class Game:
    """
    A class that builds a board, takes cars from a jason file using
    another helper class, then builds a game, where the user keeps calling is
    asked to enter a color and a direction to move to, once the user gets to
    the end point, the game ends.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(
            "\nNOTE: You can end game with '!'\n*HINT*: You can use '?' for hints \n")
        print(self.board.__str__())
        while True:
            user_input = input(
                "Choose which Car to move and which direction: ")
            if "!" in user_input:
                break

            if len(user_input) < 2 or len(user_input) > 3 or user_input == '':
                continue
            user_input = user_input.split(",")

            color = user_input[0]
            direction = user_input[1]
            if color not in colors or direction not in directions:
                print("\nWrong inputs, try other inputs.\n")
                continue
            valid_move = self.board.move_car(color, direction)
            if not valid_move:
                print("\nAttempt Failed, Try other inputs")
                continue
            if self.board.cell_content(TARGET_LOCATION) == color:
                break
            print(self.board.__str__())

    # implement your code here (and then delete the next line - 'pass')


def valid_data(car):
    if car.get_name() not in colors:
        return False
    if (car.orientation != HORIZONTAL) and (car.orientation != VERTICAL):
        return False
    if (car.length < 2) or (car.length > 4):
        return False
    return True


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    current_board = Board()

    dic = load_json(sys.argv[1])
    for i, k in dic.items():
        new_car = Car(i, k[0], k[1], k[2])
        if valid_data(new_car):
            current_board.add_car(new_car)
    try_game = Game(current_board)
    try_game.play()
