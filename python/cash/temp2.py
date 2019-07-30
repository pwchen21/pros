"""
Version:x.x.x
Histroy: 
This file is for Debug / Try & Error
"""


import pickle
import sqlite3
import tkinter as tk2

from tkinter import messagebox

class teeemp:

	def __init__(self):
		self.TK2=tk2.Tk()
		self.TK2.title("Teset File")
		self.TK2.geometry('250x350')
		print('class teeemp')
	
	def fun1(self):	
		tk2.Label(self.TK2, text="Temp2：").pack()
		self.ls=[1,2,3,4]
		self.a=tk2.StringVar()
		self.a.set(self.ls)
		print('t:',self.a.get())
		#print('a', a)
		#A=tk.Listbox(TK2, width=15, height=16)
		self.A=tk2.Listbox(self.TK2, listvariable=self.a, width=15, height=16)
		self.A.pack()
						
		
		"""
		for x in ls:
			print('x',x)
			A.insert(x)
			print(A)
		"""
		
		self.TK2.mainloop()
		
	#def fun3(self):
	#	self.fun1(self)
		
class ppt:
	def fun2():
		print('print by tmp2')

		
#A=teeemp()
#A.fun1()