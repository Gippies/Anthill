import pyglet
from pyglet.graphics import Batch


class GraphicComponent:
    def __init__(self, current_view, position, color, width, height):
        self.current_view = current_view
        self.position = position
        self.color = color
        self.width = width
        self.height = height

    def draw(self):
        """Override this to draw an object"""
        pass

    def get_draw_options(self):
        return (4, pyglet.gl.GL_QUADS, None, (
            'v2f', (
                self.position.x, self.position.y,
                self.position.x + self.width, self.position.y,
                self.position.x + self.width, self.position.y + self.height,
                self.position.x, self.position.y + self.height
            )
        ), self.color
        )

    def update(self, *args):
        """Override this to update an object's graphic (i.e. position)"""
        pass

    def is_touching(self, other):
        return other.position.x <= self.position.x + self.width and \
            other.position.x + other.width >= self.position.x and \
            other.position.y <= self.position.y + self.height and \
            other.position.y + other.height >= self.position.y


class GraphicView:
    OUTSIDE = 1
    UNDERGROUND = 2

    def __init__(self, graphic_components):
        self.graphic_components = graphic_components

    def draw(self, current_view):
        batch_to_draw = Batch()
        for c in self.graphic_components:
            if c.current_view == current_view:
                options = c.get_draw_options()
                batch_to_draw.add(*options)
        batch_to_draw.draw()
