import mailbox
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
import re   
from string import ascii_lowercase
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
alpha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
print(alpha)
nums = [0,1,2,3,4,5,6,7,8,9]
def check(email):   
    global mail
    if(re.search(regex,email)):
        mail = True   
        print("Valid Email")  
    else:   
        mail= False
        print("Invalid Email") 
def strCheck(st):
    global vulnaam
    if list(st) not in alpha:
        vulnaam = False
    else:
        vulnaam = True
        print('vul graag alleen letters in, voor je voor en achternaam')


    
radioList = []
def controleren():
    global gebruiker,radioList,ges,RadioGeslacht,selected,mail

    gebruiker = {
    'Naam:         ' : str(entryList[0].get()),
    'Achternaam:   ' : str(entryList[1].get()),
    'Telefoon Nr:  ' : int(entryList[2].get()),
    'E-mail Adress:' : str(entryList[3].get()),
    'Geslacht:     ' : selected.get()
    }
    check(entryList[3].get())
    strCheck(entryList[1].get())
    strCheck(entryList[0].get())
    if vulnaam == True and mail == True :
        for i in gebruiker:
            print(i,gebruiker[i])
    else:   
        print('check je informatie A.U.B.!')

    
window = tk.Tk()
window.geometry('250x300')

# #=============== voornaam entry en label============
entryList = []
lebRelX = 0.01
lebRelY = 0.02
lst = ['voornaam','achternaam','TelefoonNr','E-mail']
for i in lst:

    label = tk.Label(text=f'{i}')
    label.place(relx=lebRelX,rely=lebRelY,anchor='nw')
    entry = tk.Entry()
    entry.place(relx=0.3,rely=lebRelY,anchor='nw')
    entryList.append(entry) 
    lebRelY += 0.09
#============= radioButton ================
relX = 0.28
relY = 0.5

label5 = tk.Label(text='Geslacht : ')
label5.place(relx=0.01,rely=0.5,anchor='nw')


ges = ['man','vrouw']

selected = tk.StringVar()
for i in range(2):
    RadioGeslacht = ttk.Radiobutton(window,text=ges[i], value=ges[i] ,variable=selected)
    RadioGeslacht.place(relx=relX,rely=relY,anchor='nw')
    relX += 0.2
    # radioList.append(RadioGeslacht)
    
#=============== Check Button =================
CheckBut = tk.Button(text='Controleren')
CheckBut.place(relx=0.5,rely=0.9,anchor='center')
CheckBut.config(command=controleren)



window.mainloop()