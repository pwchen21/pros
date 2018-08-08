"""
Version:x.x.x
Histroy: 
This file is for Debug / Try & Error
"""


import pickle
import sqlite3
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

class teeemp():
	def fun1():
		TK2=tk.Tk()
		TK2.title("Teset File")
		TK2.geometry('250x350')
		print('class teeemp')
		
		
		tk.Label(TK2, text="Temp2：").pack()
		
		a=tk.StringVar()
		print('t:',a.get())
		a.set([1,2,3,4])
		print('t1: ', a.get())
		
		A=tk.Listbox(TK2, listvariable=[1,2,3,4], width=15, height=16)
		A.pack()
		TK2.mainloop()
		
class ppt():
	print('print by tmp2')

#teeemp.fun1()