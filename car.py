UP = "u"
DOWN = "d"
LEFT = "l"
RIGHT = "r"
VERTICAL = 0
HORIZONTAL = 1


class Car:
    """
    The Car class builds a car with a specific length, location and name and
    orientation, the car either moves up , down or right and left,
    the Class contains a couple of methods that either move a car,
    gets the car coordinates, or method that returns a car possible moves

    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """

        coordination = []
        for i in range(self.length):
            if self.orientation == VERTICAL:
                temp = (self.location[0] + i, self.location[1])


            elif self.orientation == HORIZONTAL:
                temp = (self.location[0], self.location[1] + i)

            else:

                return []
            coordination.append(temp)
        return coordination

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        result = dict()
        if self.orientation == 0:
            result["u"] = "This car can go up"
            result["d"] = "This car can go down"
        if self.orientation == 1:
            result["r"] = "This car can go right"
            result["l"] = "This car can go left"

        return result

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        temp = []
        coordinations = self.car_coordinates()
        if movekey == UP:
            row = coordinations[0][0] - 1
            col = coordinations[0][1]
            temp = (row, col)
        if movekey == DOWN:
            row = coordinations[-1][0] + 1
            col = coordinations[-1][1]
            temp = (row, col)
        if movekey == RIGHT:
            row = coordinations[-1][0]
            col = coordinations[-1][1] + 1
            temp = (row, col)
        if movekey == LEFT:
            row = coordinations[0][0]
            col = coordinations[0][1] - 1
            temp = (row, col)

        return [temp]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        possible_moves = self.possible_moves()
        if movekey in possible_moves.keys():
            if movekey == DOWN:
                self.location = [self.location[0] + 1, self.location[1]]
            elif movekey == UP:
                self.location = [self.location[0] - 1, self.location[1]]
            elif movekey == RIGHT:
                self.location = [self.location[0], self.location[1] + 1]
            else:
                self.location = [self.location[0], self.location[1] - 1]
            return True
        else:
            return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.name

if __name__ == '__main__':
    new_car = Car("name",3,[1,2],0)
    new_car.move("u")