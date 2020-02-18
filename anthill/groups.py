import random

from anthill.creatures import Ant
from anthill.plants import Leafy
from anthill.structures import Hill
from anthill.utils.vectors import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Colony:
    INITIAL_AMOUNT = 100
    START_POS_X = SCREEN_WIDTH // 2
    START_POS_Y = SCREEN_HEIGHT // 2

    def __init__(self):
        self.ants = []
        self.hill = Hill(Vector2(Colony.START_POS_X, Colony.START_POS_Y))
        x = Colony.START_POS_X
        y = Colony.START_POS_Y
        for i in range(0, Colony.INITIAL_AMOUNT):
            self.ants.append(Ant(Vector2(x, y)))

    def update(self, leafies, delta_time):
        for ant in self.ants:
            ant.update(leafies, self.hill, delta_time)


class PlantKingdom:
    INITIAL_AMOUNT_OF_LEAFIES = 250

    def __init__(self):
        self.leafies = []
        for i in range(0, PlantKingdom.INITIAL_AMOUNT_OF_LEAFIES):
            pos = Vector2(round(random.uniform(0, SCREEN_WIDTH)), round(random.uniform(0, SCREEN_HEIGHT)))
            self.leafies.append(Leafy(pos))

    def update(self, delta_time):
        for leafy in self.leafies:
            leafy.update(delta_time)
