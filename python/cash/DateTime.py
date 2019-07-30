"""
Version:0.0.01

Histroy: 
2018/09/07 - Initial Version for Date/Time Page. How to Config system time should cosider more detail. Including timezone.

Waiting Imporve / Fix:


Modify Date: 2018/09/07
"""

import pickle
import sqlite3
import tkinter as tk
import datetime

from tkinter import ttk
from tkinter import messagebox


class DateTime:
	def __init__(self, uid):
		self.usr=uid
		self.IC=tk.Tk()
		self.IC.title("Edit Date / Time")
		self.IC.geometry('310x335')

		self.dt=tk.StringVar(self.IC)
		self.tm=tk.StringVar(self.IC)
		self.dt.set(str(datetime.datetime.now().date()))
		self.tm.set(datetime.datetime.now().time().strftime('%H:%M:%S'))
		
		tk.Label(self.IC, text="Date：").place(x=50, y=30)
		self.dte=tk.Entry(self.IC, width=20, textvariable=self.dt)
		self.dte.place(x=95, y=30)

		tk.Label(self.IC, text="Time：").place(x=50, y=50)
		self.tme=tk.Entry(self.IC, width=20, textvariable=self.tm)
		self.tme.place(x=95, y=50)
		
		DTSet=tk.Button(self.IC, text="SET", bg='gray94', bd=2, command=self.dtset)
		DTSet.place(x=75, y=80)
		
		GetCT=tk.Button(self.IC, text="GET CURRENT TIME", bg='gray94', bd=2, command=self.GCT)
		GetCT.place(x=110, y=80)
		
		self.IC.mainloop()
	
	def conn_db(self, sqlc, *v):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc, *v)
			data=r.fetchall()
			conn.commit()
			conn.close()
			return data	
	
	def dtset(self):
		print('Function dtset')
		CUR=datetime.datetime.now()
		sql='UPDATE TIME_SET SET DATE=?, TIME=? WHERE UID=0'
		self.conn_db(sql, (datetime.datetime.now().date(), datetime.datetime.now().time().strftime('%H:%M:%S')))
		print('C:', type(CUR))
		print('N:', type(self.dt.get()), '',  type(self.tm.get()))

	def GCT(self):
		self.dt.set(str(datetime.datetime.now().date()))
		self.tm.set(str(datetime.datetime.now().time().strftime('%H:%M:%S')))
	
		
