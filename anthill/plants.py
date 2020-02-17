from anthill.utils.graphics import GraphicComponent


class Leafy(GraphicComponent):
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, x, y, width=WIDTH, height=HEIGHT):
        super().__init__(x, y, width, height)
        self.being_approached_by = None
        self.being_carried_by = None
