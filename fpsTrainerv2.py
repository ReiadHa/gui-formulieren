import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *

check = True

def Time():
    global tijd,pts,label,check
    timer = tk.Label(text=f'Time Remaining {tijd}',fg='white',bg='black',width=30)   
    timer.place(relx=0.20, rely=0, anchor='n')  
    if tijd != 0:
        tijd -= 1 
    elif tijd == 0:
        msgBox = messagebox.askyesno('',f"congrats u have scored {pts} points,\ndo u want to play again? ")
        if msgBox == True: 
            tijd = 20
            pts   = 0
            check = False
            clear_frame()
            entry()
            start()  
        else: 
            window.destroy()
    if check == True:
        window.after(1000,Time)

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

def ptsScore():
    global pts
    score = tk.Label(text =f'{pts} Points', bg='black',fg='white',width=20)
    score.place(relx=0.95, rely=0, anchor='ne')
   
def keuze():
    global plek, press,clicks,mouse,label,randList,mouse
    randPlek = random.choice(plek)
    mouse = random.choice(list(clicks))
    randList = random.choice(press)
    if randList != '<Button-1>' and randList != '<Triple-Button-1>' and randList != '<Double-Button-1>':
        window.bind(f'{randList}',keyboard)
        label = tk.Label(frame,text = f'press {randList}')
        label.config(width=15,bg='black',fg='white')
        label.place(rely = randPlek, relx= randPlek,anchor='center')
    else : 
        label = tk.Label(frame,text = f'{clicks[mouse]}')
        label.place(rely = randPlek, relx= randPlek,anchor='center')
        label.config(bg='black',fg='white')
        label.bind(f'{mouse}',keyboard)

def keyboard(event):
    global label,pts,check 
    if check == True:
        window.unbind(f'{randList}') 
        label.unbind(f'{mouse}') 
        label.destroy()
        pts +=1
        keuze()
        ptsScore()

def butClicked():
    global check,but
    check = True
    but.destroy()  
    sub_btn.destroy()
    entLabel.destroy()
    sec_entry.destroy()
    Time() 
    keuze()
    
def submit():
    global seconds,tijd,sub_btn,entLabel,secVar
    seconds = secVar.get()
    seconds = int(secVar.get())
    print("amount of seconds : " , seconds)
    tijd = seconds
 
def entry():
    global sub_btn,entLabel,secVar,sec_entry
    entLabel = tk.Label(frame, text = 'Fill in the time duration of the game', font=('calibre',10, 'bold'))
    entLabel.place(rely=0.2,relx=0.5,anchor='center')
    entLabel.config(bg='black',fg='white')
    secVar = tk.StringVar()
    sec = secVar.get()
    sec_entry = tk.Entry(frame,textvariable = secVar, font=('calibre',10,'normal'))
    sec_entry.place(rely=0.3,relx=0.5,anchor='center')
    sub_btn=tk.Button(frame,text = 'Submit befor u start the game!', command = submit)
    sub_btn.place(rely=0.4,relx=0.5,anchor='center')
    sub_btn.config(bg='black',fg='white')

def start():
    global but,score,timer,check
    score = tk.Label(frame, text =f'{pts} Points', bg='black',fg='white',width=20)
    score.place(relx=1.0, rely=0, anchor='ne')
    timer = tk.Label(frame,text=f'Time Remaining {tijd}',fg='white',bg='black',width=30)   
    timer.place(relx=0.20, rely=0, anchor='n')  
    but = tk.Button(frame)
    but.config(text='press Hier to start',bg='black',fg='white',command=butClicked)
    but.place(rely=0.5,relx=0.5,anchor='center')

window = tk.Tk()
window.geometry('300x300')
window.resizable(False,False)

frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")

tijd = 20
pts   = 0

press = ['a', 's','w','d','<space>','<Button-1>','<Double-Button-1>','<Triple-Button-1>']
clicks = {
    '<Button-1>'        : 'one click',
    '<Double-Button-1>' : 'Doubble Click',
    '<Triple-Button-1>' : 'Tripple Click',
}
plek  = [0.45,0.25,0.50,0.35,0.60]

start()
entry()

window.mainloop()