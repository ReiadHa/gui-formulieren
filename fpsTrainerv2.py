import random
import tkinter as tk
from tkinter import messagebox


def Time():
    global tijd,pts,label
    timer = tk.Label(text=f'Time Remaining {tijd}',fg='white',bg='black',width=30)   
    timer.place(relx=0.20, rely=0, anchor='n')  
    if tijd != 0:
        tijd -= 1 
    elif tijd == 0:
        msgBox = messagebox.askyesno('',f"congrats u have scored {pts} points,\ndo u want to play again? ")
        if msgBox == True: 
            tijd = 20
            pts   = 0
            label.destroy()
            keuze()
        else: 
            window.destroy()
    window.after(1000,Time)

def ptsScore():
    global pts
    score = tk.Label( text =f'{pts} Points', bg='black',fg='white',width=20)
    score.place(relx=0.95, rely=0, anchor='ne')
   

def keuze():
    global plek, press,clicks,mouse,label,randList,mouse
    randPlek = random.choice(plek)
    mouse = random.choice(list(clicks))
    randList = random.choice(press)
    if randList != '<Button-1>' and randList != '<Triple-Button-1>' and randList != '<Double-Button-1>':
        window.bind(f'{randList}',keyboard)
        label = tk.Label(text = f'press {randList}')
        label.config(width=15,bg='black',fg='white')
        label.place(rely = randPlek, relx= randPlek,anchor='center')
    else : 
        label = tk.Label(text = f'{clicks[mouse]}')
        label.place(rely = randPlek, relx= randPlek,anchor='center')
        label.config(bg='black',fg='white')
        label.bind(f'{mouse}',keyboard)

def keyboard(event):
    global label,pts  
    window.unbind(f'{randList}') 
    label.unbind(f'{mouse}') 
    label.destroy()
    pts +=1
    keuze()
    ptsScore()

def butClicked():
    but.destroy()  
    Time() 
    keuze()


window = tk.Tk()
window.geometry('300x300')
window.config(bg='grey')


tijd = 20
pts   = 0

press = ['a', 's','w','d','<space>','<Button-1>','<Double-Button-1>','<Triple-Button-1>']
clicks = {
    '<Button-1>'        : 'one click',
    '<Double-Button-1>' : 'Doubble Click',
    '<Triple-Button-1>' : 'Tripple Click',
}
plek  = [0.45,0.25,0.50,0.35,0.60]

score = tk.Label( text =f'{pts} Points', bg='black',fg='white',width=20)
score.place(relx=1.0, rely=0, anchor='ne')

but = tk.Button()
but.config(text='press Hier to start',bg='black',fg='white',command=butClicked)
but.place(rely=0.5,relx=0.5,anchor='center')

timer = tk.Label(text=f'Time Remaining {tijd}',fg='white',bg='black',width=30)   
timer.place(relx=0.20, rely=0, anchor='n')  







window.mainloop()