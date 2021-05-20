"""
pyglet program:
1) get a window running :check:
2) draw lines :check:
3) mouse input :check:
"""
import pyglet
from pyglet.graphics import draw
from pyglet.window import mouse
from pyglet import shapes,gui
import LineTool
import ToolBar
import ButtonHandler


window = pyglet.window.Window()
linecur = window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
defcur = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)

# test = shapes.Circle(200,200,5,color=(0,255,0))
# test.opacity = 128


def printhi():
    print("hi")
    pass

def printlow():
    print("low")
    pass


ButtonHandler.CreateButton(30,40,"toggle",True,False)
ButtonHandler.CreateButton(200,220,"toggle","cock","penis")

# LineTool.active = True

@window.event
def on_mouse_press(x,y,button,mods):
    # LineTool.active = ButtonHandler.ToggleButton(x,y)
    # print(LineTool.active)
    LineTool.onClick(x,y,button,linecur,window)
       

@window.event   
def on_mouse_release(x, y, button, mods):
    LineTool.onRelease(x,y,button,defcur,window)


@window.event
def on_mouse_drag(x,y,dx,dy,button,mods):
    LineTool.onDrag(x,y,button)

@window.event
def on_draw():
    window.clear()
    LineTool.newLines()
    ToolBar.drawBox()
    ButtonHandler.DrawButtons()

pyglet.app.run()

