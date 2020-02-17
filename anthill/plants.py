from anthill.utils.graphics import GraphicComponent


class Leafy(GraphicComponent):
    WIDTH = 4
    HEIGHT = 4

    def __init__(self, position, width=WIDTH, height=HEIGHT):
        super().__init__(position, width, height)
        self.being_approached_by = None
        self.being_carried_by = None
