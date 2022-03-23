from cgitb import text
import tkinter as tk
from typing import Container

window = tk.Tk()
window.geometry('300x600')

#=============== voornaam entry en label============
label1 = tk.Label(text='voornaam: ')
label1.place(relx=0.01,rely=0.01,anchor='nw')

entry1 = tk.Entry()
entry1.place(relx=0.3,rely=0.01,anchor='nw')
#============= achternaam entry en label=============
label2 = tk.Label(text='achternaam: ')
label2.place(relx=0.01,rely=0.05,anchor='nw')

entry2 = tk.Entry()
entry2.place(relx=0.3,rely=0.05,anchor='nw')

#============= radioButton ================
label3 = tk.Label(text='Geslacht : ')
label3.place(relx=0.01,rely=0.09,anchor='nw')

radioGelsacht = tk.Radiobutton(text='Man')
radioGelsacht.place(relx=0.28,rely=0.09,anchor='nw')
radioGelsacht.place(relx=0.28,rely=0.09,anchor='nw')




window.mainloop()