import string
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase
import random
a = string.ascii_lowercase
l = list(a)


def popupmsg():
    global punt
    msgBox = messagebox.askyesno('Game Over',f'Game over, jou punten zij {punt}, het word was {woord}\n wil je nog meer spelen ? ')
    if msgBox == True:
        clear_frame()
        punt = 20
        startup()
    else:
        window.destroy()

def clear_frame():
    global lijst
    for widgets in frame.winfo_children():
      widgets.destroy()
    lijst.clear()

def gok():
    global woord,box1,B,punt,count
    bol = True
    for index in range(len(woord)):
        if woord[index] == lijst[index].get():
            lijst[index].config(bg = 'green')
        elif lijst[index].get() in woord:
            lijst[index].config(bg='orange')
            punt -= 2
            bol = False
        else:
            bol = False
            punt -= 2
    if bol == True:
        if len(woord) < 6:
            punt += 15
            msg = messagebox.showinfo('Gewonnen!',f'Gefiliciteerd je hebt woord uitgeraad!\n jou punten zijn {punt}')
            count.destroy()
            clear_frame()
            startup()
        else:
            clear_frame()
            startup()
            punt += 36
    if punt <= 0: 
        print('game over')
        popupmsg()
    else:    
        print(punt)
    count.config(text=f'your points are {punt}')
def Verlaten():
    window.destroy()

def raad():
    global woord,box1,B,count,lijst
    woord = str(wordStr.get())

    if len(woord) >7 or len(woord) < 4:
        msgB = messagebox.showinfo('index out of range!','vul graag een woord van 4 tot 7 letters!')

    else:
        clear_frame()
        leave = tk.Button(text= 'Quit')
        leave.place(relx = 0.9,rely = 0.9, anchor='center')
        leave.config(command=Verlaten)

        label = tk.Label(frame,text='Raad het Woord')
        label.place(relx= 0.53, rely=0.2,anchor='s')
        label.config(font = ("Courier",20))

        rel = 0.15
        but1 = tk.Button(frame,text='Doe een gok!')
        but1.place(relx=0.5,rely=0.5,anchor='center')
        but1.config(command=gok)

        for B in range(len(woord)):
            alles =[random.choice(ascii_lowercase) for i in range(4)] 
            alles.append(woord[B])
            random.shuffle(alles)
            box1 = tk.Spinbox(frame)
            box1.config(width=3)
            box1['values'] =[i for i in alles]
            box1.place(relx= rel, rely=0.3,anchor='center')
            lijst.append(box1)
            rel += 0.15


        

def startup():
    global but,wordStr,word,count
    label = tk.Label(frame,text='vul een woord in! ')
    label.place(relx= 0.53, rely=0.2,anchor='s')
    label.config(font = ("Courier",20))

    word = tk.Entry(frame,textvariable = wordStr)
    word.place(relx=0.5,rely=0.3, anchor='center')

    label2 = tk.Label(frame,text='(4 tot 7 letters)')
    label2.place(relx=0.5,rely=0.4, anchor='center')

    but = tk.Button(frame,text = 'stel woord in')
    but.place(relx=0.5,rely=0.5, anchor='center')
    but.config(command=raad)     
    count = tk.Label(text=f'your points are {punt}')
    count.place(relx=0.01,rely=0.01, anchor='sw')
    count.pack() 

        

window = tk.Tk()
window.geometry('300x300')
wordStr = tk.StringVar()
frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")
lijst = []
punt = 20

startup()
window.mainloop()