
from random import random


class Tile(object):
     
    
    def place_levers(game_map):
        possible_tiles = []
        for tile_positions in game_map:
            possible_tiles.append(tile_positions)
        lever_tiles = random.sample(possible_tiles, 4)
        return lever_tiles
        
    def pull_lever(player_position, lever_tiles):
        if player_position in lever_tiles:
            print("would you like to pull the lever? (y/n)")
            choice = input()
            if choice == "y":
                lever_tiles.remove(player_position)
                
        return False

    def __init__(self):
        pass