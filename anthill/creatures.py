import random

from anthill.colors import WHITE, get_color_by_vertices, YELLOW
from anthill.structures import Hill
from anthill.utils.circular_queue import CircularQueue
from anthill.utils.graphics import GraphicComponent, GraphicView
from anthill.utils.vectors import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class State:
    """This is an enum"""
    SEARCH = 1
    GET_THING = 2
    RETURN_TO_HILL = 3
    RETURN_TO_SURFACE = 4
    DROP_THING = 5

    GATHERER_STATES = [SEARCH, GET_THING, RETURN_TO_HILL, DROP_THING, RETURN_TO_SURFACE]
    DIGGER_STATES = [SEARCH, GET_THING, RETURN_TO_SURFACE, DROP_THING, RETURN_TO_HILL]


class Role:
    """This is an enum"""
    GATHERER = 1
    DIGGER = 2


class Ant(GraphicComponent):
    MAX_SPEED = 40.0
    MAX_SEARCH_SECONDS = 0.5
    MAX_DROP_ITERATIONS = 5
    MAX_SEARCH_RADIUS = 20.0
    WIDTH = 4.0
    HEIGHT = 4.0
    GATHERER_COLOR = get_color_by_vertices(4, *WHITE)
    DIGGER_COLOR = get_color_by_vertices(4, *YELLOW)

    def __init__(self, current_view, role, position, color=GATHERER_COLOR, width=WIDTH, height=HEIGHT):
        self.velocity = Vector2.zero()
        self.speed = Ant.MAX_SPEED
        self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
        self.role = role
        if self.role == Role.GATHERER:
            self.state_queue = CircularQueue(*State.GATHERER_STATES)
        elif self.role == Role.DIGGER:
            self.state_queue = CircularQueue(*State.DIGGER_STATES)
        self.state = self.state_queue.dequeue()

        self.approaching = None
        self.carrying = None
        self.direction_to_go = 0
        self.drop_iterations = Ant.MAX_DROP_ITERATIONS
        super().__init__(current_view, position, color, width, height)

    def _update_position(self, dirts):
        old_position = self.position
        self.position = old_position + self.velocity

        # Stay in the boundaries
        if not 0 < self.position.x < SCREEN_WIDTH:
            self.position.x = old_position.x
        if not 0 < self.position.y < SCREEN_HEIGHT:
            self.position.y = old_position.y
        if self.current_view == GraphicView.UNDERGROUND:
            for dirt in dirts:
                if self.is_touching(dirt) and self.carrying is not None and self.carrying != dirt and dirt.being_carried_by is None:
                    self.position = old_position
                    break

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
            if self.current_view == carriable.current_view and \
                    self.position.x - Ant.MAX_SEARCH_RADIUS <= carriable.position.x <= self.position.x + Ant.MAX_SEARCH_RADIUS and \
                    self.position.y - Ant.MAX_SEARCH_RADIUS <= carriable.position.y <= self.position.y + Ant.MAX_SEARCH_RADIUS and \
                    carriable.being_approached_by is None and carriable.being_carried_by is None and carriable.is_stored is False:
                self.state = self.state_queue.dequeue()
                self.approaching = carriable
                carriable.being_approached_by = self
                break

    def _get_thing(self, delta_time):
        self.direction_to_go = (self.approaching.position - self.position).get_normalized_vector()
        self.velocity = self.direction_to_go * self.speed * delta_time
        if self.is_touching(self.approaching):
            self.state = self.state_queue.dequeue()
            self.carrying = self.approaching
            self.approaching = None
            self.carrying.being_carried_by = self
            self.carrying.being_approached_by = None
            self.carrying.pick_up()

    def _return_to_hill(self, hill, delta_time):
        self.direction_to_go = (hill.position - self.position).get_normalized_vector()
        if self.carrying is not None:
            self.carrying.position.x = self.position.x - self.width
            self.carrying.position.y = self.position.y
        self.velocity = self.direction_to_go * self.speed * delta_time
        if self.is_touching(hill):
            if self.carrying is not None:
                self.state = self.state_queue.dequeue()
                self.drop_iterations = Ant.MAX_DROP_ITERATIONS
                self.carrying.current_view = GraphicView.UNDERGROUND
            else:
                self.state = self.state_queue.dequeue()
            self.current_view = GraphicView.UNDERGROUND
            self._set_position_to_view()
            self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)

    def _return_to_surface(self, delta_time):
        self.direction_to_go = (Vector2(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT) - self.position).get_normalized_vector()
        if self.carrying is not None:
            self.carrying.position.x = self.position.x - self.width
            self.carrying.position.y = self.position.y
        self.velocity = self.direction_to_go * self.speed * delta_time
        if self.current_view == GraphicView.UNDERGROUND and \
                self.position.x <= SCREEN_WIDTH / 2.0 <= self.position.x + self.width and \
                self.position.y <= SCREEN_HEIGHT <= self.position.y + self.height:
            if self.carrying is not None:
                self.state = self.state_queue.dequeue()
                self.drop_iterations = Ant.MAX_DROP_ITERATIONS
                self.carrying.current_view = GraphicView.OUTSIDE
            else:
                self.state = self.state_queue.dequeue()
            self.current_view = GraphicView.OUTSIDE
            self._set_position_to_view()
            self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)

    def _drop_thing(self, delta_time):
        self.search_seconds -= delta_time
        if self.carrying is not None:
            self.carrying.position.x = self.position.x - self.width
            self.carrying.position.y = self.position.y
        if self.search_seconds <= 0.0:
            if self.drop_iterations > 0:
                self.drop_iterations -= 1
                self.direction_to_go = Vector2(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)).get_normalized_vector()
                self.velocity = self.direction_to_go * self.speed * delta_time
                self.search_seconds = random.uniform(0.0, Ant.MAX_SEARCH_SECONDS)
            else:
                self.state = self.state_queue.dequeue()
                self.carrying.is_stored = True
                self.carrying.being_carried_by = None
                self.carrying = None

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
        elif self.state == State.RETURN_TO_SURFACE:
            self._return_to_surface(delta_time)
        elif self.state == State.DROP_THING:
            self._drop_thing(delta_time)

        self._update_position(dirts)
