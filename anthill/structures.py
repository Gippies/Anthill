import pyglet

from anthill.colors import SAND_YELLOW_4
from anthill.utils.graphics import GraphicComponent


class Dirt(GraphicComponent):
    WIDTH = 4.0
    HEIGHT = 4.0

    def __init__(self, current_view, position, width=WIDTH, height=HEIGHT):
        super().__init__(current_view, position, width, height)


class Hill(GraphicComponent):
    WIDTH = 8.0
    HEIGHT = 8.0

    def __init__(self, current_view, position, width=WIDTH, height=HEIGHT):
        super().__init__(current_view, position, width, height)
        self.food_store = []

    def get_draw_options(self):
        return (4, pyglet.gl.GL_QUADS, None, (
                 'v2f', (
                     self.position.x, self.position.y,
                     self.position.x + self.width, self.position.y,
                     self.position.x + self.width, self.position.y + self.height,
                     self.position.x, self.position.y + self.height
                 )
                ), SAND_YELLOW_4
                )

    def update(self, delta_time):
        pass
