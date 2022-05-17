import tkinter as tk

root = tk.Tk()
root.geometry("750x750")
root.title("Het Dambord")
color = True

for r in range(10):
	for c in range(10):
		label1 = tk.Label()
		label1.place(x= c*75 ,y = r*75)
		if color == True: 
			label1.config(bg='black')
		if color == False:
			label1.config(bg='grey')
		color = not color
		label1.config(width=10,height=5)
	color = not color
root.resizable(False,False)
root.mainloop()