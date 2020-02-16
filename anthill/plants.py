import pyglet

from anthill.colors import GREEN_4
from anthill.utils.graphics import GraphicComponent


class Leafy(GraphicComponent):
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        super().__init__(x, y, width, height)

    def draw(self):
        """Ants are represented by a square, as drawn below"""
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_POLYGON,
                                     [0, 1, 2, 3, 0],
                                     ('v2i', (self.x, self.y,
                                              self.x + self.width, self.y,
                                              self.x + self.width, self.y + self.height,
                                              self.x, self.y + self.height)),
                                     GREEN_4
                                     )
