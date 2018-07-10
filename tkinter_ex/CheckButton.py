import tkinter as tk

tko=tk.Tk()
tko.title('CheckButton')
tko.geometry('300x300')

def hungry():	
	if ((var1.get()==0) and (var2.get()==0)):
		lb.config(text='肚子餓!')
	elif (var1.get()==1 and var2.get()==0):
		lb.config(text='我愛雞腿飯!!!')
	elif (var1.get()==0 and var2.get()==1):
		lb.config(text='我愛排骨飯!!!')
	else:
		lb.config(text='我愛吃便當!')

		
var1=tk.IntVar()
var2=tk.IntVar()

lb=tk.Label(tko, text='餓', backgroun='light pink')
lb.pack()

#Set Uncheck Box
var1.set(0)
var2.set(0)

ckb1=tk.Checkbutton(tko, text='雞腿飯', onvalue=1, offvalue=0, variable=var1, command=hungry)
ckb2=tk.Checkbutton(tko, text='排骨飯', onvalue=1, offvalue=0, variable=var2, command=hungry)
ckb1.pack()
ckb2.pack()



tko.mainloop()