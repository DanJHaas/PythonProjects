import tkinter as tk
from tkinter import *
top = tk.Tk()

x1,y1,x2,y2=0,0,0,0

def Lclick(event):
    print("x: {0}, y: {1}".format(event.x,event.y))
    print("box-x: {0}, box-y: {1}".format(1+event.x//16,1+event.y//16))
    global x1,y1,x2,y2
    x1=event.x//16*16
    y1=event.y//16*16
    x2=x1+16
    y2=y1+16
    Draw()
    

def Rclick(event):
    print("right clic")



C = tk.Canvas(top, bg="green", height=512, width=512)


def Draw():
    C.delete("all")
    Select(x1,y1,x2,y2)
    for i in range(32):
        for j in range(32):
            C.create_line(i*16,0,i*16,512)
            C.create_line(0,i*16,512,i*16)
            C.create_text(8+i*16,8+j*16,text="0",font="20")
    

def Select(x1,y1,x2,y2):
    C.create_rectangle(x1,y1,x2,y2,fill="blue")



Draw()
C.bind("<Button-1>", Lclick)
C.bind("<Button-3>", Rclick)
C.pack()
top.resizable(False,False)
tk.mainloop()