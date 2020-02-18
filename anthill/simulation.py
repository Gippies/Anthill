from anthill.groups import Colony, PlantKingdom
from anthill.structures import Chamber
from anthill.utils.graphics import GraphicView
from anthill.utils.vectors import Vector2


class View:
    OUTSIDE = 1
    UNDERGROUND = 2


class Simulation:
    def __init__(self):
        self.colony = Colony()
        self.plant_kingdom = PlantKingdom()
        self.view = View.OUTSIDE

        graphic_components = [self.colony.hill]
        graphic_components.extend(self.colony.ants)
        graphic_components.extend(self.plant_kingdom.leafies)
        self.outside_view = GraphicView(graphic_components)
        self.underground_view = GraphicView([Chamber(Vector2(200, 200))])

    def draw(self):
        if self.view == View.OUTSIDE:
            self.outside_view.draw()
        elif self.view == View.UNDERGROUND:
            self.underground_view.draw()

    def update(self, delta_time):
        self.colony.update(self.plant_kingdom.leafies, delta_time)
        self.plant_kingdom.update(delta_time)
