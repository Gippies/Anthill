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
    RETURN_TO_HILL = 3


class Ant(GraphicComponent):
    MAX_SPEED = 25
    MAX_SEARCH_SECONDS = 0.5
    MAX_SEARCH_RADIUS = 20
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        self.velocity = Vector2.zero()
        self.speed = Ant.MAX_SPEED
        self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
        self.state = State.SEARCH

        self.approaching = None
        self.carrying = None
        self.direction_to_go = 0
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

    def update(self, leafies, hill, delta_time):
        if self.state == State.SEARCH:
            self.search_seconds -= delta_time
            if self.search_seconds <= 0.0:
                self.direction_to_go = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).get_normalized_vector()
                self.velocity = self.direction_to_go * self.speed * delta_time
                self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
            for leafy in leafies:
                if self.x - Ant.MAX_SEARCH_RADIUS <= leafy.x <= self.x + Ant.MAX_SEARCH_RADIUS and \
                        self.y - Ant.MAX_SEARCH_RADIUS <= leafy.y <= self.y + Ant.MAX_SEARCH_RADIUS and \
                        leafy.being_approached_by is None and leafy.being_carried_by is None and leafy not in hill.food_store:
                    self.state = State.GET_FOOD
                    self.approaching = leafy
                    leafy.being_approached_by = self
                    break
        elif self.state == State.GET_FOOD:
            if self.approaching.x != self.x and self.approaching.y != self.y:
                self.direction_to_go = Vector2(self.approaching.x - self.x, self.approaching.y - self.y).get_normalized_vector()
            self.velocity = self.direction_to_go * self.speed * delta_time
            if self.approaching.x == self.x and self.approaching.y == self.y:
                self.state = State.RETURN_TO_HILL
                self.carrying = self.approaching
                self.approaching = None
                self.carrying.being_carried_by = self
                self.carrying.being_approached_by = None
        elif self.state == State.RETURN_TO_HILL:
            if SCREEN_WIDTH / 2.0 != self.x and SCREEN_HEIGHT / 2.0 != self.y:
                self.direction_to_go = Vector2(SCREEN_WIDTH / 2.0 - self.x, SCREEN_HEIGHT / 2.0 - self.y).get_normalized_vector()
            self.carrying.x = self.x
            self.carrying.y = self.y
            self.velocity = self.direction_to_go * self.speed * delta_time
            if round(SCREEN_WIDTH / 2.0) == self.x and round(SCREEN_HEIGHT / 2.0) == self.y:
                self.state = State.SEARCH
                hill.food_store.append(self.carrying)
                self.carrying.being_carried_by = None
                self.carrying = None

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
