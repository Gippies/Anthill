from anthill.groups import Colony, PlantKingdom


class Simulation:
    def __init__(self):
        self.colony = Colony()
        self.plant_kingdom = PlantKingdom()

    def draw(self):
        self.plant_kingdom.draw()
        self.colony.draw()

    def update(self, delta_time):
        self.plant_kingdom.update(delta_time)
        self.colony.update(self.plant_kingdom.leafies, delta_time)
