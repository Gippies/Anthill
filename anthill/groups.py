import random

from anthill.colors import YELLOW, get_color_by_vertices
from anthill.creatures import Ant, Role
from anthill.plants import Leafy
from anthill.structures import Hill, Dirt
from anthill.utils.graphics import GraphicView
from anthill.utils.vectors import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Colony:
    INITIAL_AMOUNT_OF_GATHERERS = 40
    INITIAL_AMOUNT_OF_DIGGERS = 10
    HILL_START_POS_X = SCREEN_WIDTH / 2.0
    HILL_START_POS_Y = SCREEN_HEIGHT / 2.0
    GATHERER_START_POS_X = HILL_START_POS_X + Hill.WIDTH
    GATHERER_START_POS_Y = HILL_START_POS_Y
    DIGGER_START_POS_X = HILL_START_POS_X
    DIGGER_START_POS_Y = SCREEN_HEIGHT

    def __init__(self):
        self.ants = []
        self.hill = Hill(GraphicView.OUTSIDE, Vector2(Colony.HILL_START_POS_X, Colony.HILL_START_POS_Y))
        for i in range(Colony.INITIAL_AMOUNT_OF_GATHERERS):
            self.ants.append(Ant(GraphicView.OUTSIDE, Role.GATHERER, Vector2(Colony.GATHERER_START_POS_X, Colony.GATHERER_START_POS_Y)))
        for i in range(Colony.INITIAL_AMOUNT_OF_DIGGERS):
            self.ants.append(Ant(GraphicView.UNDERGROUND, Role.DIGGER, Vector2(Colony.DIGGER_START_POS_X, Colony.DIGGER_START_POS_Y), color=get_color_by_vertices(4, *YELLOW)))

    def update(self, leafies, dirts, delta_time):
        for ant in self.ants:
            ant.update(leafies, dirts, self.hill, delta_time)


class Earth:
    INITIAL_AMOUNT_OF_DIRT = 9
    START_POS_X = SCREEN_WIDTH / 2.0
    START_POS_Y = SCREEN_HEIGHT - Dirt.HEIGHT

    def __init__(self):
        self.dirts = []
        start_x = Earth.START_POS_X - 2 * Dirt.WIDTH
        start_y = Earth.START_POS_Y

        # Start dirt in 'u' shape:
        for i in range(Earth.INITIAL_AMOUNT_OF_DIRT // 3):
            self.dirts.append(Dirt(GraphicView.UNDERGROUND, Vector2(start_x, start_y)))
            start_y -= Dirt.HEIGHT

        for i in range(5):
            self.dirts.append(Dirt(GraphicView.UNDERGROUND, Vector2(start_x, start_y)))
            start_x += Dirt.WIDTH

        for i in range(Earth.INITIAL_AMOUNT_OF_DIRT // 3 + 1):
            self.dirts.append(Dirt(GraphicView.UNDERGROUND, Vector2(start_x, start_y)))
            start_y += Dirt.HEIGHT


class PlantKingdom:
    INITIAL_AMOUNT_OF_LEAFIES = 250

    def __init__(self):
        self.leafies = []
        for i in range(0, PlantKingdom.INITIAL_AMOUNT_OF_LEAFIES):
            pos = Vector2(random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            self.leafies.append(Leafy(GraphicView.OUTSIDE, pos))
