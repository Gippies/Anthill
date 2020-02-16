import pyglet

from settings import SCREEN_WIDTH, SCREEN_HEIGHT

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)


@window.event
def on_draw():
    window.clear()


pyglet.app.run()
