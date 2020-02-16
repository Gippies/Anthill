from anthill.creatures import Ant
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Colony:
    INITIAL_AMOUNT = 100
    START_POS_X = SCREEN_WIDTH // 2
    START_POS_Y = SCREEN_HEIGHT // 2

    def __init__(self):
        self.ants = []
        x = Colony.START_POS_X
        y = Colony.START_POS_Y
        for i in range(0, Colony.INITIAL_AMOUNT):
            self.ants.append(Ant(x, y))
            y += 10
            if y > Colony.START_POS_Y + 100:
                y = Colony.START_POS_Y
                x += 10

    def draw(self):
        for ant in self.ants:
            ant.draw()

    def update(self, delta_time):
        for ant in self.ants:
            ant.update(delta_time)
