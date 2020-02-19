import random

from anthill.colors import WHITE, get_color_by_vertices, YELLOW
from anthill.structures import Hill
from anthill.utils.graphics import GraphicComponent, GraphicView
from anthill.utils.vectors import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class State:
    """This is an enum"""
    SEARCH = 1
    GET_THING = 2
    RETURN_TO_HILL = 3


class Role:
    """This is an enum"""
    GATHERER = 1
    DIGGER = 2


class Ant(GraphicComponent):
    MAX_SPEED = 40.0
    MAX_SEARCH_SECONDS = 0.5
    MAX_SEARCH_RADIUS = 20.0
    WIDTH = 4.0
    HEIGHT = 4.0
    GATHERER_COLOR = get_color_by_vertices(4, *WHITE)
    DIGGER_COLOR = get_color_by_vertices(4, *YELLOW)

    def __init__(self, current_view, role, position, color=GATHERER_COLOR, width=WIDTH, height=HEIGHT):
        self.velocity = Vector2.zero()
        self.speed = Ant.MAX_SPEED
        self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
        self.state = State.SEARCH
        self.role = role

        self.approaching = None
        self.carrying = None
        self.direction_to_go = 0
        super().__init__(current_view, position, color, width, height)

    def _update_position(self):
        old_position = self.position
        self.position = old_position + self.velocity

        # Stay in the screen
        if not 0 < self.position.x < SCREEN_WIDTH:
            self.position.x = old_position.x
        if not 0 < self.position.y < SCREEN_HEIGHT:
            self.position.y = old_position.y

    def _set_position_to_view(self):
        if self.current_view == GraphicView.OUTSIDE:
            self.position.x = SCREEN_WIDTH / 2.0 + Hill.WIDTH
            self.position.y = SCREEN_HEIGHT / 2.0 + Hill.HEIGHT
        elif self.current_view == GraphicView.UNDERGROUND:
            self.position.x = SCREEN_WIDTH / 2.0
            self.position.y = SCREEN_HEIGHT
        if self.carrying is not None:
            self.carrying.position.x = self.position.x - self.carrying.width
            self.carrying.position.y = self.position.y

    def _search(self, carriables, delta_time):
        self.search_seconds -= delta_time
        if self.search_seconds <= 0.0:
            self.direction_to_go = Vector2(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)).get_normalized_vector()
            self.velocity = self.direction_to_go * self.speed * delta_time
            self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
        for carriable in carriables:
            if self.position.x - Ant.MAX_SEARCH_RADIUS <= carriable.position.x <= self.position.x + Ant.MAX_SEARCH_RADIUS and \
                    self.position.y - Ant.MAX_SEARCH_RADIUS <= carriable.position.y <= self.position.y + Ant.MAX_SEARCH_RADIUS and \
                    carriable.being_approached_by is None and carriable.being_carried_by is None and carriable.is_stored is False:
                self.state = State.GET_THING
                self.approaching = carriable
                carriable.being_approached_by = self
                break

    def _get_thing(self, delta_time):
        self.direction_to_go = (self.approaching.position - self.position).get_normalized_vector()
        self.velocity = self.direction_to_go * self.speed * delta_time
        if self.is_touching(self.approaching):
            self.state = State.RETURN_TO_HILL
            self.carrying = self.approaching
            self.approaching = None
            self.carrying.being_carried_by = self
            self.carrying.being_approached_by = None

    def _return_to_hill(self, hill, delta_time):
        self.direction_to_go = (hill.position - self.position).get_normalized_vector()
        self.carrying.position.x = self.position.x - self.width
        self.carrying.position.y = self.position.y
        self.velocity = self.direction_to_go * self.speed * delta_time
        if self.is_touching(hill):
            self.current_view = GraphicView.UNDERGROUND
            self.carrying.current_view = GraphicView.UNDERGROUND
            self._set_position_to_view()

            # self.state = State.SEARCH
            # self.carrying.is_stored = True
            # self.carrying.being_carried_by = None
            # self.carrying = None

    def update(self, leafies, dirts, hill, delta_time):
        if self.state == State.SEARCH:
            if self.role == Role.GATHERER:
                self._search(leafies, delta_time)
            elif self.role == Role.DIGGER:
                self._search(dirts, delta_time)
        elif self.state == State.GET_THING:
            self._get_thing(delta_time)
        elif self.state == State.RETURN_TO_HILL:
            self._return_to_hill(hill, delta_time)
        self._update_position()
