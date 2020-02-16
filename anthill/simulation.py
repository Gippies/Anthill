from anthill.groups import Colony, PlantKingdom


class Simulation:
    def __init__(self):
        self.colony = Colony()
        self.plant_kingdom = PlantKingdom()

    def draw(self):
        self.colony.draw()
        self.plant_kingdom.draw()

    def update(self, delta_time):
        self.colony.update(delta_time)
        self.plant_kingdom.update(delta_time)
