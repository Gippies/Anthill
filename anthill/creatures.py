import random

import pyglet

from anthill.colors import WHITE_4
from anthill.utils.graphics import GraphicComponent
from anthill.utils.vectors import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class State:
    """This is an enum"""
    SEARCH = 1
    GET_FOOD = 2


class Ant(GraphicComponent):
    MAX_SPEED = 50
    MAX_SEARCH_SECONDS = 0.5
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        self.velocity = Vector2.zero()
        self.speed = Ant.MAX_SPEED
        self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
        self.state = State.SEARCH
        super().__init__(x, y, width, height)

    def _update_position(self):
        old_x = self.x
        old_y = self.y
        self.x = round(old_x + self.velocity.x)
        self.y = round(old_y + self.velocity.y)

        # Stay in the screen
        if not 0 < self.x < SCREEN_WIDTH:
            self.x = old_x
        if not 0 < self.y < SCREEN_HEIGHT:
            self.y = old_y

    def update(self, delta_time):
        if self.state == State.SEARCH:
            self.search_seconds -= delta_time
            if self.search_seconds <= 0.0:
                self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) * self.speed * delta_time
                self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)

        self._update_position()

    def draw(self):
        """Ants are represented by a square, as drawn below"""
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_POLYGON,
                                     [0, 1, 2, 3, 0],
                                     ('v2i', (self.x, self.y,
                                              self.x + self.width, self.y,
                                              self.x + self.width, self.y + self.height,
                                              self.x, self.y + self.height)),
                                     WHITE_4
                                     )
