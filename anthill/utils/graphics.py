class GraphicComponent:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        """Override this to draw an object"""
        pass

    def update(self, *args):
        """Override this to update an object's graphic (i.e. position)"""
        pass
