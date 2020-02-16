import pyglet

from anthill.utils.graphics import GraphicComponent


class Ant(GraphicComponent):
    MAX_SPEED = 100
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        self.max_speed = Ant.MAX_SPEED
        super().__init__(x, y, width, height)

    def update(self, delta_time):
        self.x += int(self.max_speed * delta_time)

    def draw(self):
        """Ants are represented by a square, as drawn below"""
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_POLYGON,
                                     [0, 1, 2, 3, 0],
                                     ('v2i', (self.x, self.y,
                                              self.x + self.width, self.y,
                                              self.x + self.width, self.y + self.height,
                                              self.x, self.y + self.height))
                                     )
