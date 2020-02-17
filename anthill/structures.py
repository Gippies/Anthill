import pyglet

from anthill.colors import SAND_YELLOW_4
from anthill.utils.graphics import GraphicComponent


class Hill(GraphicComponent):
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        super().__init__(x, y, width, height)
        self.food_store = []

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             (
                                 'v2i', (
                                     self.x, self.y,
                                     self.x + self.width, self.y,
                                     self.x + self.width, self.y + self.height,
                                     self.x, self.y + self.height
                                 )
                             ),
                             SAND_YELLOW_4
                             )

    def update(self, delta_time):
        pass
