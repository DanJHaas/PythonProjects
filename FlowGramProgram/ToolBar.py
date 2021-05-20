"""
Tool GUI steps:
1) rectangle box with some basic icons


"""

from pyglet import shapes
from pyglet.window import mouse

tools = {
    "LineTool":[1],
    "ShapeTool":[2]
}

boxBack = shapes.Rectangle(20,20,30,100,color=(0,255,0))
boxFore = shapes.Rectangle(22,22,26,96,color=(0,0,0))


def drawBox():
    boxBack.draw()
    boxFore.draw()