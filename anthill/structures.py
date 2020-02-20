from anthill.colors import SAND_YELLOW, get_color_by_vertices, BROWN
from anthill.things import Carriable
from anthill.utils.graphics import GraphicComponent, GraphicView


class Dirt(Carriable):
    WIDTH = 4.0
    HEIGHT = 4.0
    COLOR = get_color_by_vertices(4, *BROWN)

    def __init__(self, current_view, position, color=COLOR, width=WIDTH, height=HEIGHT):
        self.top_left = None
        self.top = None
        self.top_right = None

        self.left = None
        self.right = None

        self.bottom_left = None
        self.bottom = None
        self.bottom_right = None

        self.is_viewable = False
        super().__init__(current_view, position, color, width, height)

    def _show_neighbor(self, neighbor_str, self_str):
        if getattr(self, neighbor_str) is not None:
            setattr(getattr(self, neighbor_str), 'current_view', GraphicView.UNDERGROUND)
            setattr(getattr(self, neighbor_str), 'is_viewable', True)
            setattr(getattr(self, neighbor_str), self_str, None)

    def pick_up(self):
        self._show_neighbor('top_left', 'bottom_right')
        self._show_neighbor('top', 'bottom')
        self._show_neighbor('top_right', 'bottom_left')

        self._show_neighbor('left', 'right')
        self._show_neighbor('right', 'left')

        self._show_neighbor('bottom_left', 'top_right')
        self._show_neighbor('bottom', 'top')
        self._show_neighbor('bottom_right', 'top_left')


class Hill(GraphicComponent):
    WIDTH = 8.0
    HEIGHT = 8.0
    COLOR = get_color_by_vertices(4, *SAND_YELLOW)

    def __init__(self, current_view, position, color=COLOR, width=WIDTH, height=HEIGHT):
        super().__init__(current_view, position, color, width, height)
        self.food_store = []

    def update(self, delta_time):
        pass
