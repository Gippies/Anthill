from anthill.groups import Colony, PlantKingdom
from anthill.utils.graphics import GraphicView


class Simulation:
    def __init__(self):
        self.colony = Colony()
        self.plant_kingdom = PlantKingdom()

        graphic_components = [self.colony.hill]
        graphic_components.extend(self.colony.ants)
        graphic_components.extend(self.plant_kingdom.leafies)
        self.outside_view = GraphicView(graphic_components)

    def draw(self):
        self.outside_view.draw()

    def update(self, delta_time):
        self.colony.update(self.plant_kingdom.leafies, delta_time)
        self.plant_kingdom.update(delta_time)
