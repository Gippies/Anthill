from anthill.colors import GREEN, get_color_by_vertices
from anthill.utils.graphics import GraphicComponent


class Leafy(GraphicComponent):
    WIDTH = 4.0
    HEIGHT = 4.0
    COLOR = get_color_by_vertices(4, *GREEN)

    def __init__(self, current_view, position, color=COLOR, width=WIDTH, height=HEIGHT):
        super().__init__(current_view, position, color, width, height)
        self.being_approached_by = None
        self.being_carried_by = None
