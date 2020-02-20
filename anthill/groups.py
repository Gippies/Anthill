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
        self.all_dirts = []
        self.viewable_dirts = []

        all_dirts = []
        r_counter = 0
        c_counter = 0
        for i in range(0, SCREEN_WIDTH, int(Dirt.WIDTH)):
            temp_dirts = []
            for j in range(0, SCREEN_HEIGHT, int(Dirt.HEIGHT)):
                new_dirt = Dirt(None, Vector2(i, j))
                temp_dirts.append(new_dirt)

                if c_counter - 1 >= 0:
                    new_dirt.left = temp_dirts[c_counter - 1]
                    temp_dirts[c_counter - 1].right = new_dirt

                if c_counter - 1 >= 0 and r_counter - 1 >= 0:
                    new_dirt.bottom_left = all_dirts[r_counter - 1][c_counter - 1]
                    all_dirts[r_counter - 1][c_counter - 1].top_right = new_dirt

                if r_counter - 1 >= 0:
                    new_dirt.bottom = all_dirts[r_counter - 1][c_counter]
                    all_dirts[r_counter - 1][c_counter].top = new_dirt

                if r_counter - 1 >= 0 and c_counter + 1 < len(all_dirts[r_counter - 1]):
                    new_dirt.bottom_right = all_dirts[r_counter - 1][c_counter + 1]
                    all_dirts[r_counter - 1][c_counter + 1].top_left = new_dirt
                c_counter += 1
            all_dirts.append(temp_dirts)
            c_counter = 0
            r_counter += 1

        start_x = int((Earth.START_POS_X - 2 * Dirt.WIDTH) / Dirt.WIDTH)
        start_y = int(Earth.START_POS_Y / Dirt.HEIGHT)

        # Start dirt in 'u' shape:
        for i in range(3):
            for j in range(5):
                all_dirts[start_x][start_y].pick_up()
                all_dirts[start_x][start_y] = None
                start_x += 1
            start_x = int((Earth.START_POS_X - 2 * Dirt.WIDTH) / Dirt.WIDTH)
            start_y -= 1

        for i in range(len(all_dirts)):
            for j in range(len(all_dirts[0])):
                if all_dirts[i][j] is not None:
                    self.all_dirts.append(all_dirts[i][j])

    def update(self):
        for dirt in self.all_dirts:
            if dirt.is_viewable and dirt not in self.viewable_dirts:
                self.viewable_dirts.append(dirt)


class PlantKingdom:
    INITIAL_AMOUNT_OF_LEAFIES = 250

    def __init__(self):
        self.leafies = []
        for i in range(0, PlantKingdom.INITIAL_AMOUNT_OF_LEAFIES):
            pos = Vector2(random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            self.leafies.append(Leafy(GraphicView.OUTSIDE, pos))
