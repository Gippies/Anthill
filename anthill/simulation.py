from anthill.groups import Colony, PlantKingdom
from anthill.utils.graphics import GraphicView


class Simulation:
    def __init__(self):
        self.colony = Colony()
        self.plant_kingdom = PlantKingdom()
        self.view = GraphicView.OUTSIDE

        graphic_components = [self.colony.hill]
        graphic_components.extend(self.colony.ants)
        graphic_components.extend(self.plant_kingdom.leafies)
        self.all_view = GraphicView(graphic_components)

    def draw(self):
        self.all_view.draw(self.view)

    def update(self, delta_time):
        self.colony.update(self.plant_kingdom.leafies, delta_time)
        self.plant_kingdom.update(delta_time)
