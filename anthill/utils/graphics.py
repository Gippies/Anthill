from pyglet.graphics import Batch


class GraphicComponent:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def draw(self):
        """Override this to draw an object"""
        pass

    def get_draw_options(self):
        """Override this to get the draw options for an object to be sent to the view"""
        pass

    def update(self, *args):
        """Override this to update an object's graphic (i.e. position)"""
        pass

    def is_touching(self, other):
        return other.position.x <= self.position.x + self.width and \
            other.position.x + other.width >= self.position.x and \
            other.position.y <= self.position.y + self.height and \
            other.position.y + other.height >= self.position.y


class GraphicView:
    def __init__(self, graphic_components):
        self.graphic_components = graphic_components

    def draw(self):
        batch_to_draw = Batch()
        for c in self.graphic_components:
            options = c.get_draw_options()
            batch_to_draw.add(*options)
        batch_to_draw.draw()
