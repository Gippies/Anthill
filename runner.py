import pyglet

from anthill.simulation import Simulation
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
simulation = Simulation()


@window.event
def on_draw():
    window.clear()
    simulation.draw()


pyglet.clock.schedule_interval(simulation.update, FRAME_RATE)
pyglet.app.run()
