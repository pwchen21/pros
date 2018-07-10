import tkinter as tk
from tkinter import messagebox


tko=tk.Tk()
tko.title('Pop-up')
tko.geometry('300x300')

def popup():
	"""	
	#showinfo/showwarning/showerror
	tk.messagebox.showinfo(title='Info', message='OK')
	tk.messagebox.showwarning(title='Warning', message='!!!!!!')
	tk.messagebox.showerror(title='Error', message='XXXXX')
	"""
	
	#print return value
	
	#Return Value YES/NO
	print(tk.messagebox.askquestion(title='ask YES/NO', message='Hello'))
	#Return Value True/False
	print(tk.messagebox.askokcancel(title='ask YES/Cancel', message='Hello'))
	#Return Value True/False/None
	print(tk.messagebox.askyesnocancel(title='ask Yes/NO/Cancel', message='Hello'))  
	
btn=tk.Button(text='HIT!!', command=popup)
btn.pack()


tko.mainloop()