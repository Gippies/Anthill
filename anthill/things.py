from anthill.utils.graphics import GraphicComponent


class Carriable(GraphicComponent):
    def __init__(self, current_view, position, color, width, height):
        super().__init__(current_view, position, color, width, height)
        self.being_approached_by = None
        self.being_carried_by = None
        self.is_stored = False

    def pick_up(self):
        """Override this method to do something once picked-up"""
        pass
