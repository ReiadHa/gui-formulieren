import tkinter as tk 
from tkinter import *
from tkinter import ttk
from calendar import month_name,day_name


def go():
    pass


window = tk.Tk()
window.geometry('200x200')

label = tk.Label(text="Please select a date:")
label.pack(fill=tk.X, padx=5, pady=5)


month = tk.StringVar()
box = ttk.Combobox(window, textvariable = month)
box['values'] = [day_name[m] for m in range(1, 13)]
box['state'] = 'readonly'
box.place(x = 75,y = 40,width = 55)

day = tk.StringVar()
box2 = ttk.Combobox(window, textvariable = day)
box2['values'] = [month_name[m][0:3] for m in range(1, 13)]
box2['state'] = 'readonly'
box2.place(x = 10,y = 40,width = 55)

year = tk.StringVar()
box3 = ttk.Combobox(window, textvariable = year)
box3['values'] = [month_name[m][0:3] for m in range(1, 13)]
box3['state'] = 'readonly'
box3.place(x = 140,y = 40,width = 55)

but = tk.Button()
but.config(text = 'Go')
but.place(relx= 0.5, rely= 0.5,anchor = 'center')
but.config(command=go)





window.mainloop()