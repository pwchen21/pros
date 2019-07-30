"""
Version:0.0.01
Histroy: 
2018/8/08 - Initial Version

Waiting Imporve / Fix:
F001 - Cannot get bank & credit card list


Modify Date: 2018/08/08
"""

import pickle
import sqlite3
import mainFR
import tkinter as tk
from tkinter import messagebox
#Internal Module
import MainCategory
import SubCategory
import InitBank
import InitCredit
import DateTime

class SettingPage():
	
	def __init__(self, uid):
		self.SP=tk.Tk()
		self.SP.title("Settings")
		self.SP.geometry('280x280')	

		# Temp user, this will be replace by variable 
		self.usr=uid	
		print('setting page',uid)
		tk.Label(self.SP, text='Setting').place(x=110, y=10)

		self.mainC=tk.Button(self.SP, text="Category", command=self.MC)
		self.mainC.place(x=30, y=50, width=90)

		self.subC=tk.Button(self.SP, text="Sub Category", command=self.SC)
		self.subC.place(x=30, y=90, width=90)
		
		self.subC=tk.Button(self.SP, text="Init Credit", command=self.IC)
		self.subC.place(x=150, y=50, width=90)
		
		self.subC=tk.Button(self.SP, text="Init Bank", command=self.IB)
		self.subC.place(x=150, y=90, width=90)

		self.subC=tk.Button(self.SP, text="Date/Time", command=self.DT)
		self.subC.place(x=30, y=130, width=90)
		
		
		self.SP.mainloop()
		
	def MC(self):
		MainCategory.MainCategory(self.usr)
		
	def SC(self):
		SubCategory.SubCategory(self.usr)
		
	def IC(self):		
		InitCredit.InitCredit(self.usr)
		
	def IB(self):
		InitBank.InitBank(self.usr)
		
	def DT(self):
		DateTime.DateTime(self.usr)
		