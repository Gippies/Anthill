import pyglet
from pyglet.window import mouse

from anthill.simulation import Simulation
from anthill.utils.graphics import GraphicView
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
simulation = Simulation()


@window.event
def on_draw():
    window.clear()
    simulation.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        simulation.view = GraphicView.UNDERGROUND
    elif button == mouse.RIGHT:
        simulation.view = GraphicView.OUTSIDE


pyglet.clock.schedule_interval(simulation.update, 1.0 / FRAME_RATE)
pyglet.app.run()
