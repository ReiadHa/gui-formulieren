import tkinter as tk


radioList = []
def controleren():
    global gebruiker,entry1,entry2,entry3,entry4,radioList,ges,RadioGeslacht
    if RadioGeslacht== True:
        gender = ges[0]

    gebruiker = {
    'Naam:         ' : entryList[0].get(),
    'Achternaam:   ' : entryList[1].get(),
    'Telefoon Nr:  ' : entryList[2].get(),
    'E-mail Adress:' : entryList[3].get(),
    # 'Geslacht:     ' : gender
    }
    for i in gebruiker:
        print(i, gebruiker[i])

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
for i in range(2):
    RadioGeslacht = tk.Radiobutton(text=ges[i],value = i)
    RadioGeslacht.place(relx=relX,rely=relY,anchor='nw')
    relX += 0.2
    radioList.append(RadioGeslacht)
    
#=============== Check Button =================
CheckBut = tk.Button(text='Controleren')
CheckBut.place(relx=0.5,rely=0.9,anchor='center')
CheckBut.config(command=controleren)



window.mainloop()