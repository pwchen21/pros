import tkinter as tk

tko=tk.Tk()
tko.title('Radio Button')
tko.geometry('300x300')


def pt_fruit():	
	#print('TEST')
	#print(var.get())
	l.config(text='I love ' + var.get() + '!!!')

#Create Label
var=tk.StringVar()
var.set(0) # set value to uncheck
l=tk.Label(tko, bg='royal blue', text='empty', width=20)
l.pack()	
	
#Create Radio button
r1=tk.Radiobutton(tko, text="LEMON", value='LEMON', variable=var, command=pt_fruit)
r1.pack()
r2=tk.Radiobutton(tko, text="Water Melon", value='Water Melon', variable=var, command=pt_fruit)
r2.pack()
r3=tk.Radiobutton(tko, text="Orange", value='Orange', variable=var, command=pt_fruit)
r3.pack()


tko.mainloop()