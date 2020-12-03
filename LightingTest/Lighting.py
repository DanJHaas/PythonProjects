from math import ceil, floor
import tkinter as tk
from tkinter import *
top = tk.Tk()

L = []

x1,y1,x2,y2,lx,ly=0,0,0,0,16,16

def Lclick(event):
    # print("x: {0}, y: {1}".format(event.x,event.y))
    # print("box-x: {0}, box-y: {1}".format(1+event.x//16,1+event.y//16))
    global x1,y1,x2,y2,lx,ly
    x1=event.x//16*16
    y1=event.y//16*16
    x2=x1+16
    y2=y1+16
    lx = x1/16
    ly = y1/16
    
    Draw()
    

def Rclick(event):
    print("right clic")



C = tk.Canvas(top, bg="black", height=512, width=512)

def Setup():
    for i in range(32):
        L.append([])
        for j in range(32):
            L[i].append([])
    
    

def Draw():
    C.delete("all")
    Light(int(ly),int(lx),16)
    Select(x1,y1,x2,y2)
    for i in range(32):
        C.create_line(i*16,0,i*16,512)
        C.create_line(0,i*16,512,i*16)
        for j in range(32):
            if L[i][j] == []:
                L[i][j] = 0
            if not L[i][j] == 0:
                C.create_text(8+i*16,8+j*16,text=str(L[i][j]),font="Times 12")

    
def Select(x1,y1,x2,y2):
    C.create_rectangle(x1,y1,x2,y2,fill="#ffff00")


def Light(lightX,lightY,radius):
    radius=radius*2
    for y in range(radius):
        for x in range(radius):
            gridX = abs(lightX-floor(radius/2)+x)
            gridY = abs(lightY-floor(radius/2)+y)
            dist = abs(gridX-lightX) + abs(gridY-lightY)
            dist = (dist-radius+floor(radius/2))*-1
            if dist <= 0:
                dist=0
            C.create_rectangle(gridY*16,gridX*16,(gridY*16)+16,(gridX*16)+16,fill="#{:02x}{:02x}00".format(dist*10,dist*10))
            try:    
                L[gridY][gridX] = dist
            except:
                None
            


Setup()
Draw()
C.bind("<Button-1>", Lclick)
C.bind("<Button-3>", Rclick)
C.pack()
top.resizable(False,False)
tk.mainloop()