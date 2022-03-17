import tkinter as tk
from tkinter import *
import tkinter


window= tk.Tk()
window.geometry('1920x1080')
toggle = False
for r in range(11):
    for c in range(11):
        tom = tkinter.Label()
        tom.place(x= r*75 ,y = c*75)
        if toggle :
            tom.config(bg='white',width=50,height=50)
        else:
            tom.config(bg='black',width=50,height=50)
        toggle = not toggle
    toggle = not toggle




window.mainloop()
