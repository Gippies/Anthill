import math

import pyglet

from anthill.colors import SAND_YELLOW_4
from anthill.utils.graphics import GraphicComponent


class Chamber(GraphicComponent):
    NUMBER_OF_VERTICES = 32
    WHITE_32 = ('c3B', tuple(255 for i in range(NUMBER_OF_VERTICES * 3)))
    WIDTH = 100
    HEIGHT = 50

    def __init__(self, position, width=WIDTH, height=HEIGHT):
        super().__init__(position, width, height)

    def get_draw_options(self):
        points = []
        current_step = 0
        for i in range(Chamber.NUMBER_OF_VERTICES):
            points.append(round(self.position.x + self.width * math.cos(current_step)))
            points.append(round(self.position.y + self.height * math.sin(current_step)))
            current_step += math.pi / (Chamber.NUMBER_OF_VERTICES / 2.0)
        return Chamber.NUMBER_OF_VERTICES, pyglet.gl.GL_POINTS, None, ('v2i', points), Chamber.WHITE_32


class Hill(GraphicComponent):
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, position, width=WIDTH, height=HEIGHT):
        super().__init__(position, width, height)
        self.food_store = []

    def get_draw_options(self):
        return (4, pyglet.gl.GL_QUADS, None, (
                 'v2i', (
                     self.position.x, self.position.y,
                     self.position.x + self.width, self.position.y,
                     self.position.x + self.width, self.position.y + self.height,
                     self.position.x, self.position.y + self.height
                 )
                ), SAND_YELLOW_4
                )

    def update(self, delta_time):
        pass
