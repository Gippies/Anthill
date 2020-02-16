from anthill.creatures import Ant


class Colony:
    INITIAL_AMOUNT = 100

    def __init__(self):
        self.ants = []
        for i in range(0, Colony.INITIAL_AMOUNT):
            self.ants.append(Ant(200, 200))

    def draw(self):
        for ant in self.ants:
            ant.draw()

    def update(self, delta_time):
        for ant in self.ants:
            ant.update(delta_time)
