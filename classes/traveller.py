import tile

class Traveller(object):
    def __init__(self, position: tuple[int]):
        self.__position = position[0:2]
        self.__gold = 0
    
    def add_gold(self, amount = 1):
        self.__gold += amount

    def get_gold(self):
        return self.__gold
    
    def move_tile(self, direction: str):
        if direction in ["N", "n"]:
            self.__position = (self.__position[0], self.__position[1] - 1)
        elif direction in ["E", "e"]:
            self.__position = (self.__position[0] + 1, self.__position[1])
        elif direction in ["S", "s"]:
            self.__position = (self.__position[0], self.__position[1] + 1)
        elif direction in ["W", "w"]:
            self.__position = (self.__position[0] - 1, self.__position[1])

    def get_tile(self):
        return self.__position