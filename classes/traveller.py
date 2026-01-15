import tile

class Traveller(object):
    def __init__(self, position: tuple[int]):
        self.__position = position[0:2]
        self.__gold = 0
    
    def add_gold(self, amount: int):
        if not amount < 0:
            self.__gold += amount

    def get_gold(self):
        return self.__gold
    
    def move_tile(self, direction: str):
        pass

    def get_tile(self):
        return self.__position
    
john = Traveller((1, 1, 3))

print(john.get_tile())