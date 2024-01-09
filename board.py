import copy

WINNING_LOCATION = (3, 7)
BOARD_SIZE = 7
EMPTY_CELLS = "_"
RIGHT = "r"
LEFT = "l"
UP = "u"
DOWN = "d"
VERTICAL = 0
HORIZONTAL = 1


class Board:
    """
    A class that builds a board that is 7x7, that contains "_" for empty
    places and a car name for occupied places, the main constructor receives
    nothing but builds an empty cars list that contains all the cars
    a board filled with 7x7 "_".
    """

    def __init__(self):
        self.__cars = []
        self.__board = []

        for i in range(BOARD_SIZE):
            temp = [EMPTY_CELLS] * BOARD_SIZE
            self.__board.append(temp)
        self.__board[3].append("")

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_str = ""
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                board_str += " " + self.__board[i][j]
            board_str += "\n"

        return board_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cells = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                cells.append((row, col))
        cells.append(WINNING_LOCATION)
        return cells

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        lst = []

        for i in self.__cars:
            car_moves_dic = i.possible_moves()
            for j in car_moves_dic.keys():
                temp_location = i.movement_requirements(j)
                if temp_location[0] == WINNING_LOCATION:
                    lst.append((i.get_name(), j, car_moves_dic[j]))
                    continue
                elif BOARD_SIZE > temp_location[0][0] >= 0:
                    if BOARD_SIZE > temp_location[0][1] >= 0:
                        if self.cell_content(temp_location[0]) is None:
                            lst.append((i.get_name(), j, car_moves_dic[j]))
        return lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return WINNING_LOCATION

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # if coordinate == WINNING_LOCATION:
        #     return
        loc = self.__board[coordinate[0]][coordinate[1]]
        if loc == EMPTY_CELLS or loc == "":
            return
        else:
            return loc

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # if car.get_name() not in colors:
        #     return False
        # if (car.orientation != HORIZONTAL) and (
        #         car.orientation != VERTICAL):
        #     return False
        # if (car.length < 2) or (car.length > 4):
        #     return False
        # if car.length >= BOARD_SIZE:
        #     return False
        # if car.orientation == 0:
        #     if car.location[0] + car.length - 1 > 7:
        #         print(car.location[0])
        #         print("len", car.length)
        #         return False
        # else:
        #     if car.location[1] + car.length - 1 > 7:
        #         print(car.location[0])
        #         print("len", car.length)
        #         return False

        coordinates = car.car_coordinates()
        temp_board = copy.deepcopy(self.__board[:])
        if not coordinates:
            return False
        if len(self.__cars) != 0:
            for cars in self.__cars:
                if car == cars:
                    return False


        for i in coordinates:
            if i not in self.cell_list():
                return False

            if self.cell_content(i) is not None:
                self.__board = temp_board
                return False
            self.__board[i[0]][i[1]] = car.get_name()
        self.__cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        possiblemoves = self.possible_moves()
        cars = self.__cars
        car = False
        for i in cars:
            if i.get_name() == name:
                car = i
        if not car:
            return False
        for tuples in possiblemoves:
            if tuples[0] == car.get_name() and tuples[1] == movekey:
                is_valid = True
                coordination_old = car.car_coordinates()
                if car.move(movekey):
                    coordination_new = car.car_coordinates()
                    if movekey == DOWN or movekey == RIGHT:
                        loc = coordination_old[0]
                        new_loc = coordination_new[-1]
                        self.__board[loc[0]][loc[1]] = "_"
                        self.__board[new_loc[0]][new_loc[1]] = car.get_name()
                    else:
                        loc = coordination_old[-1]
                        new_loc = coordination_new[0]
                        self.__board[loc[0]][loc[1]] = "_"
                        self.__board[new_loc[0]][new_loc[1]] = car.get_name()
                    return True
                else:
                    return False
        return False

