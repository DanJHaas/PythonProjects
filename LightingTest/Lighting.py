from math import ceil, floor
import tkinter as tk
from tkinter import *
top = tk.Tk()

L = []

x1,y1,x2,y2=0,0,0,0

def Lclick(event):
    # print("x: {0}, y: {1}".format(event.x,event.y))
    # print("box-x: {0}, box-y: {1}".format(1+event.x//16,1+event.y//16))
    global x1,y1,x2,y2
    x1=event.x//16*16
    y1=event.y//16*16
    x2=x1+16
    y2=y1+16
    Draw()
    

def Rclick(event):
    print("right clic")



C = tk.Canvas(top, bg="green", height=512, width=512)

def Setup():
    for i in range(32):
        L.append([])
        for j in range(32):
            L[i].append([])
    
    

def Draw():
    C.delete("all")
    Light(int(y1/16),int(x1/16),9)
    Select(x1,y1,x2,y2)
    for i in range(32):
        C.create_line(i*16,0,i*16,512)
        C.create_line(0,i*16,512,i*16)
        for j in range(32):
            if L[i][j] == []:
                L[i][j] = 0
            C.create_text(8+i*16,8+j*16,text=str(L[i][j]),font="Times 12")

    
def Select(x1,y1,x2,y2):
    C.create_rectangle(x1,y1,x2,y2,fill="blue")


def Light(lx,ly,r):
    for y in range(r):
        for x in range(r):
            gx = lx-floor(r/2)+x
            gy = ly-floor(r/2)+y
            dist = abs(gx-lx) + abs(gy-ly)
            dist = (dist-r+floor(r/2))*-1
            if dist < 0:
                dist=0
            try:    
                L[gy][gx] = dist
            except:
                None
            


Setup()
Draw()
C.bind("<Button-1>", Lclick)
C.bind("<Button-3>", Rclick)
C.pack()
top.resizable(False,False)
tk.mainloop()