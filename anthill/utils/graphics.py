class GraphicComponent:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def draw(self):
        """Override this to draw an object"""
        pass

    def update(self, *args):
        """Override this to update an object's graphic (i.e. position)"""
        pass

    def is_touching(self, other):
        return other.position.x <= self.position.x + self.width and \
        other.position.x + other.width >= self.position.x and \
        other.position.y <= self.position.y + self.height and \
        other.position.y + other.height >= self.position.y
