import pyglet

from anthill.utils.graphics import GraphicComponent


class Ant(GraphicComponent):
    def __init__(self, x, y, width=4, height=4):
        super().__init__(x, y, width, height)

    def update(self, delta_time):
        self.x += 1

    def draw(self):
        """Ants are represented by a square, as drawn below"""
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_POLYGON,
                                     [0, 1, 2, 3, 0],
                                     ('v2i', (self.x, self.y,
                                              self.x + self.width, self.y,
                                              self.x + self.width, self.y + self.height,
                                              self.x, self.y + self.height))
                                     )
