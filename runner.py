import pyglet

from anthill.groups import Colony
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
my_colony = Colony()


@window.event
def on_draw():
    window.clear()
    my_colony.draw()


pyglet.clock.schedule_interval(my_colony.update, .016)
pyglet.app.run()
