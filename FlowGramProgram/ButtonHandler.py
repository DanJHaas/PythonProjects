"""
button handling for toggles and push buttons
"""

import pyglet
from pyglet import shapes
import LineTool


# x,y,type,state
buttons = {

}

def DrawButtons():
    for i in buttons:
        match buttons[i][2]:
            case "tb":
                tb = shapes.Rectangle(buttons[i][0],buttons[i][1],16,16,color=(0,0,0))
                match buttons[i][3]:
                    case 1:
                        tb.color = (0,255,0)
                        tb.draw()
                    case 0:
                        tb.color = (255,0,0)
                        tb.draw()
            case "pb":
                shapes.Rectangle(buttons[i][0],buttons[i][1],16,16,color=(0,255,0)).draw()



def CreateButton(x,y,type,TrueState,FalseState):
    match type:
        case "toggle":
            buttons["button{0}".format(len(buttons))] = [x,y,"tb",0,TrueState,FalseState]
        case "push":
            buttons["button{0}".format(len(buttons))] = [x,y,"pb",0,TrueState,FalseState]

def ToggleButton(x,y):
    for i in buttons:
        match buttons[i][2]:
            case "tb":
                if (buttons[i][0]+16 > x > buttons[i][0]) and (buttons[i][1]+16 > y > buttons[i][1]):
                    match buttons[i][3]:
                        case 0:
                            buttons[i][3] = 1
                            try:
                                return buttons[i][4]()
                            except Exception:
                                return buttons[i][4]
                                break
                            
                        case 1:
                            buttons[i][3] = 0
                            try:
                                return buttons[i][5]()
                            except Exception:
                                return buttons[i][5]
                                break

def PushButton(x,y,func):
    
    pass