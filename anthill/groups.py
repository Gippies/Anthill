import random

from anthill.creatures import Ant
from anthill.plants import Leafy
from anthill.structures import Hill
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Colony:
    INITIAL_AMOUNT = 100
    START_POS_X = SCREEN_WIDTH // 2
    START_POS_Y = SCREEN_HEIGHT // 2

    def __init__(self):
        self.ants = []
        self.hill = Hill()
        x = Colony.START_POS_X
        y = Colony.START_POS_Y
        for i in range(0, Colony.INITIAL_AMOUNT):
            self.ants.append(Ant(x, y))

    def draw(self):
        for ant in self.ants:
            ant.draw()

    def update(self, leafies, delta_time):
        for ant in self.ants:
            ant.update(leafies, self.hill, delta_time)


class PlantKingdom:
    INITIAL_AMOUNT_OF_LEAFIES = 500

    def __init__(self):
        self.leafies = []
        for i in range(0, PlantKingdom.INITIAL_AMOUNT_OF_LEAFIES):
            x = round(random.uniform(0, SCREEN_WIDTH))
            y = round(random.uniform(0, SCREEN_HEIGHT))
            self.leafies.append(Leafy(x, y))

    def draw(self):
        for leafy in self.leafies:
            leafy.draw()

    def update(self, delta_time):
        for leafy in self.leafies:
            leafy.update(delta_time)
