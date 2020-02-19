from anthill.colors import SAND_YELLOW, get_color_by_vertices, BROWN
from anthill.utils.graphics import GraphicComponent


class Dirt(GraphicComponent):
    WIDTH = 4.0
    HEIGHT = 4.0
    COLOR = get_color_by_vertices(4, *BROWN)

    def __init__(self, current_view, position, color=COLOR, width=WIDTH, height=HEIGHT):
        super().__init__(current_view, position, color, width, height)


class Hill(GraphicComponent):
    WIDTH = 8.0
    HEIGHT = 8.0
    COLOR = get_color_by_vertices(4, *SAND_YELLOW)

    def __init__(self, current_view, position, color=COLOR, width=WIDTH, height=HEIGHT):
        super().__init__(current_view, position, color, width, height)
        self.food_store = []

    def update(self, delta_time):
        pass
