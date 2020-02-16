
class Hill:
    def __init__(self):
        self.food_store = []

    def draw(self):
        for f in self.food_store:
            f.draw()

    def update(self, delta_time):
        pass
