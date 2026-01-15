from tile import Tile
import random

class World(object):
    def __init__(self, width: int=3, height: int=3):
        self.__width = width
        self.__height = height

        self.__tile_list = self.__generate_map()

    def __generate_map(self):
        tile_list = list()

        for x in range(1, self.__width + 1):
            for y in range(1, self.__height + 1):
                tile_list.append(Tile(x, y))

        return tile_list