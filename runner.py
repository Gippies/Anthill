import pyglet

from ant import Ant
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
my_ant = Ant(200, 200)


@window.event
def on_draw():
    window.clear()
    my_ant.draw()


pyglet.clock.schedule_interval(my_ant.update, .016)
pyglet.app.run()
