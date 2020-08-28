import pyglet
from pyglet.gl import gl
import ratcave as rc

test = ["hello","goodbye"]

for i,j in enumerate(test):
    print(j)

window = pyglet.window.Window()



@window.event
def on_draw():
    window.clear()


def update(dt):
    pass
pyglet.clock.schedule(update)

pyglet.app.run()