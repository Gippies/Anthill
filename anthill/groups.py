import random

from anthill.creatures import Ant
from anthill.plants import Leafy
from anthill.structures import Hill
from anthill.utils.graphics import GraphicView
from anthill.utils.vectors import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Colony:
    INITIAL_AMOUNT_OF_ANTS = 50
    START_POS_X = SCREEN_WIDTH // 2
    START_POS_Y = SCREEN_HEIGHT // 2

    def __init__(self):
        self.ants = []
        self.hill = Hill(GraphicView.OUTSIDE, Vector2(Colony.START_POS_X, Colony.START_POS_Y))
        ant_x_start_pos = Colony.START_POS_X + Hill.WIDTH
        ant_y_start_pos = Colony.START_POS_Y + Hill.HEIGHT
        for i in range(Colony.INITIAL_AMOUNT_OF_ANTS):
            self.ants.append(Ant(GraphicView.OUTSIDE, Vector2(ant_x_start_pos, ant_y_start_pos)))

    def update(self, leafies, delta_time):
        for ant in self.ants:
            ant.update(leafies, self.hill, delta_time)


class PlantKingdom:
    INITIAL_AMOUNT_OF_LEAFIES = 250

    def __init__(self):
        self.leafies = []
        for i in range(0, PlantKingdom.INITIAL_AMOUNT_OF_LEAFIES):
            pos = Vector2(random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            self.leafies.append(Leafy(GraphicView.OUTSIDE, pos))

    def update(self, delta_time):
        for leafy in self.leafies:
            leafy.update(delta_time)
