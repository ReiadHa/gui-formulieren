# # # python program demonstrating
# # # Combobox widget using tkinter


# # import tkinter as tk
# # from tkinter import ttk

# # # Creating tkinter window
# # window = tk.Tk()
# # window.title('Combobox')
# # window.geometry('500x250')

# # # label text for title
# # ttk.Label(window, text = "GFG Combobox Widget",
# # 		background = 'green', foreground ="white",
# # 		font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# # # label
# # ttk.Label(window, text = "Select the Month :",
# # 		font = ("Times New Roman", 10)).grid(column = 0,
# # 		row = 5, padx = 10, pady = 25)

# # # Combobox creation
# # n = tk.StringVar()
# # monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# # # Adding combobox drop down list
# # monthchoosen['values'] = (' January',
# # 						' February',
# # 						' March',
# # 						' April',
# # 						' May',
# # 						' June',
# # 						' July',
# # 						' August',
# # 						' September',
# # 						' October',
# # 						' November',
# # 						' December')
# # if monthchoosen['values'] == True:
# #     window.destroy()

# # monthchoosen.grid(column = 1, row = 5)
# # monthchoosen.current()
# # window.mainloop()


# # Program to make a simple
# # login screen

# #==============================================================================================================================================================================
# import tkinter as tk

# root=tk.Tk()

# # setting the windows size
# root.geometry("600x400")

# # declaring string variable
# # for storing name and password
# name_var=tk.StringVar()
# passw_var=tk.StringVar()


# # defining a function that will
# # get the name and password and
# # print them on the screen
# def submit():
    
# 	name=name_var.get()
# 	password=passw_var.get()
# 	name = int(name)
# 	print("The name is : " , name)
# 	print("The password is : " + password)
# 	print(type(name))
# 	name_var.set("")
# 	passw_var.set("")
	
	
# # creating a label for
# # name using widget Label
# name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# # creating a entry for input
# # name using widget Entry
# name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# # creating a label for password
# passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# # creating a entry for password
# passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

# # creating a button using the widget
# # Button that will call the submit function
# sub_btn=tk.Button(root,text = 'Submit', command = submit)

# # placing the label and entry in
# # the required position using grid
# # method
# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)

# # performing an infinite loop
# # for the window to display
# root.mainloop()




# import tkinter as tk
# from tkinter import *
# import tkinter


# window= tk.Tk()
# window.geometry('755x755')
# # window.wm_minsize(1000,2)
# toggle = False
# for r in range(10):
#     for c in range(10):
#         tom = tkinter.Label()
#         tom.place(x= c*75 ,y = r*75)
#         if toggle :
#             tom.config(bg='white',width=50,height=50)
#         else:
#             tom.config(bg='black',width=50,height=50)
#         toggle = not toggle
#     toggle = not toggle

# # container.columnconfigure(index, weight)
# # container.rowconfigure(index, weight)




# window.mainloop()

import tkinter as tk
from tkinter import *
import tkinter

root = tk.Tk()
root.geometry("750x750")
color = True

for r in range(10):
	for c in range(10):
		label1 = tkinter.Label()
		label1.place(x= c*75 ,y = r*75)
		if color == True: 
			label1.config(bg='black')
		if color == False:
			label1.config(bg='grey',)
		color = not color
		label1.config(width=10,height=5)
	color = not color

 


root.mainloop()