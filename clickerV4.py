import tkinter as tk 
#=================== funtions hier onder=================================
def up():
    global number,keer,soort
    number += 1
    soort = 1
    print(number)
    keer = True
    clicker()
def down():
    global number, keer,soort
    number -= 1
    print(number)
    keer = False
    soort = 2
    clicker()
def clicker():
    global number,lab
    if number < 0:
        win.config(bg='red')
    elif number > 0 :
        win.config(bg='green')
    elif number == 0:
        win.config(bg='grey')
    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr)

def Dclick(event):
    global number,soort
    print('clicked')
    if keer == True :
        number = number * 3
        soort = 3
    elif keer == False :
        print('test')
        number = number / 3
        soort = 4
    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr)
def autoClicker():
    global c1,keer,number,lab,var1
    if var1.get() == 1: 
        if soort == 1 :
            print('test1')
            number += 1
        elif soort == 2 :
            print('test2')
            number -= 1    
        elif soort == 3:
            print('test 3')
            number = number * 3        
        elif soort == 4:
            print('test 4')
            number = number / 3
    win.after(5000,autoClicker)



    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr) 
            

        
    
#==================== window/labels/buttons setup hieronder====================
soort = 0
keer = False
number = 0
win = tk.Tk()
win.geometry('300x150')

lab = tk.Label( text= f'{number:.0f}',width=20)
lab.config(bg='white')
lab.place(anchor='center',relx=0.5,rely = 0.5)

button1 = tk.Button(text='Up',width=20)
button2 = tk.Button(text='Down',width=20)

var1 = tk.IntVar() 
c1 = tk.Checkbutton(win, text='AutoClicker',variable=var1, onvalue=1, offvalue=0)
c1.pack()
autoClicker()

button1.pack(side=tk.TOP)
button2.pack(side=tk.BOTTOM)
button1.config(command=up)
button2.config(command=down)
lab.bind("<Double-Button-1>",Dclick)
clicker()

#=====window mainloop========
win.mainloop()