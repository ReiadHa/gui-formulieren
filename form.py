import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from string import ascii_letters
import re   

 
#======================= main ===========================
RowColG= 0
val = []
#============ check E-mail function/ check of de E-mail klopt en heeft 1 "@" en 1 ".com ... etc" ==================
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'    
def check(email): 
    global val  
    if(re.search(regex,email)):
        mail = True   
        print("Valid Email")  
        val.append("Valid Email")
    else:   
        mail= False
        print("Invalid Email") 
        val.append("Invalid Email")
    return mail

#================== checkt of voor en achter naam of er alleen letters in zit ========================
let = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def strCheck(st,Var):
    global val
    for i in st:
        if i in let:
            vulnaam = True
        else:
            vulnaam = False
            break
    if vulnaam == True :
        nameVal = f'valid {Var}'
        val.append(nameVal)
    else:
        nameVal = f'invalid {Var}'
        val.append(nameVal)
    return vulnaam

#=================== checkt  of de nummer valid is def ======================  
def intCheck(nt,Var):
    global val
    Nummer = nt.isnumeric() and len(nt) == 10
    if Nummer == True:
        numVal = f'valid {Var}'
        val.append(numVal)
    else:
        numVal = f'invalid {Var}'
        val.append(numVal)
    return Nummer
#================controleerd of alles True is om de codes te runnen/ gebruik maken van de vorige functies.========
def controleren():
    global gebruiker,ges,RadioGeslacht,selected,val,RowColG
    gebruiker = {
    'Naam            ' : f' {str(entryList[0].get())}',
    'Achternaam  ' : f' {str(entryList[1].get())}',
    'Telefoon Nr  ' : f' {entryList[2].get()}',
    'E-mail Adress' : f' {str(entryList[3].get())}',
    'Geslacht        ' : f' {selected.get()}'
    }
    emailVar =check(entryList[3].get())
    voorVar  = strCheck(entryList[0].get(),'voornaam      ')
    achterVar = strCheck(entryList[1].get(),'achternaam    ')
    NummerVar = intCheck(entryList[2].get(),'Telefoon Nummer')
    if voorVar == True and emailVar == True and achterVar == True and NummerVar == True:
        RowColG = RowColG + 1
        x = [(f'{i}          : {gebruiker[i]}') for i in gebruiker]
        showinfo(title='result',message='\n'.join(x))
        val.clear()
    else:   
        v = [i for i in val]
        showinfo(title='invalid',message='\n'.join(v))
        print('check je informatie A.U.B.!')
        val.clear()

#==================== Setup van de scherm ==================   
window = tk.Tk()
window.geometry('350x300')

#================== voornaam entry en label ===============
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
#================== radioButton ====================
relX = 0.28
relY = 0.4

label5 = tk.Label(text='Geslacht : ')
label5.place(relx=0.01,rely=0.4,anchor='nw')


ges = ['man','vrouw']
selected = tk.StringVar()
for i in range(2):
    RadioGeslacht = ttk.Radiobutton(window,text=ges[i], value=ges[i] ,variable=selected)
    RadioGeslacht.place(relx=relX,rely=relY,anchor='nw')
    relX += 0.2
#====================== regels label =======================
reg = ['Notitie: ','Geen spatie tussen, voor of achter de voor/achter naam.','Telefoon nummer moet 10 getalen zijn.','geldig E-mail adres invullen.']
regY = 0.5
for i in reg:
    regels = tk.Label(text=f'{i}')
    regels.place(relx=0.01,rely=regY,anchor='nw')
    regY += 0.06
#=============== CheckButton setup/command =================

CheckBut = tk.Button(text='Controleren')
CheckBut.place(relx=0.5,rely=0.9,anchor='center')
CheckBut.config(command=controleren)



window.mainloop()