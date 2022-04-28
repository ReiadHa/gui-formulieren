import tkinter as tk 
#=================== funtions hier onder=================================
def up():
    global number,keer,soort,check1
    number += 1
    soort = 1
    check1 = True
    print(number)
    keer = True
    autocheck()
    clicker()
def down():
    global number, keer,soort,var1,check1
    number -= 1
    check1 = True
    autocheck()
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
def autocheck():
    global var1
    c1.config(state='active')

def Dclick(event):
    global number,soort,check1
    print('clicked')
    if keer == True :
        number = number * 3
        soort = 3
        check1 = True
        autocheck()

    elif keer == False :
        print('test')
        number = number / 3
        soort = 4
        check1 = True
        autocheck()
    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr)
def autoClicker():
    global c1,keer,number,lab,var1
    print('test')
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
    win.after(200,autoClicker)



    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr) 
            

        
    
#==================== window/labels/buttons setup hieronder====================
soort = 0
check1 = False
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

c1.config(state='disabled')

autoClicker()
button1.pack(side=tk.TOP)
button2.pack(side=tk.BOTTOM)
button1.config(command=up)
button2.config(command=down)
lab.bind("<Double-Button-1>",Dclick)
clicker()

#=====window mainloop========
win.mainloop()