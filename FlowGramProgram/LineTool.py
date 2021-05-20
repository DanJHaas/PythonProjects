"""
Line Tool steps:
1) are you active :check:

"""
from pyglet import shapes
from pyglet.window import mouse

active = False
linex,liney = 0,0
lines = {}
fakeline = shapes.Line(0,0,0,0,color=(0,255,0),width=2)

def newLines():
    if active == True:
        fakeline.draw()
        for i in lines:
            shapes.Line(lines[i][0],lines[i][1],lines[i][2],lines[i][3],color=(0,255,0),width=2).draw()


def onClick(x,y,button, cursor,window):
    if active == True:
        match mouse.buttons_string(button):
            case "LEFT":
                window.set_mouse_cursor(cursor)
                global linex,liney
                linex = x
                liney = y
                fakeline.x = x
                fakeline.y = y
                fakeline.x2 = x
                fakeline.y2 = y
            case _:
                pass

def onRelease(x,y,button, cursor,window):
    if active == True:
        match mouse.buttons_string(button):
            case "LEFT":
                window.set_mouse_cursor(cursor)
                lines["line{0}".format(len(lines))] = [linex,liney,x,y,"blank"]
            case _:
                pass

def onDrag(x,y,button):
    if active == True:
        match mouse.buttons_string(button):
            case "LEFT":
                fakeline.x2 = x
                fakeline.y2 = y
            case _:
                pass