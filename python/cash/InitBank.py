"""
Version:0.0.04
Histroy: 
2018/08/01 - Initial Version
2018/08/03 - Fix delete without item selected will not popup error message
		   Add User authority
2018/08/08 - Improve user authority by logon (But Cannot get list by setting)
2018/08/14 - Trying to FIX F002		   
2018/08/22 - Fixed F002.
		   
Waiting Imporve / Fix:
I001- Should EDIT/DELETE by ID
F001- Shows select record when using Tab(or multiple value selected) to change column 
[Fixed-20180822]F002- Cannot get list by setting

Modify Date: 2018/08/08/22
"""

import pickle
import sqlite3
import tkinter as tk
from tkinter import messagebox

class InitBank:

	def __init__(self, uid):
		# Temp user, this will be replace by variable 
		self.usr=uid
		
		# Create InitBank
		self.IB=tk.Tk()
		self.IB.title("Init/Edit Bank")
		self.IB.geometry('310x260')
		
		# Create Bank List
		self.bankstr=tk.StringVar()
		self.getbank='select TITLE from INIT_BANK WHERE AUTH=?'
		self.bankstr.set(self.conn_db(self.getbank,(self.usr,)))
		tk.Label(self.IB, text="銀行列表：").place(x=35, y=10)
		#print(self.bankstr.get())
		#self.bklb=tk.Listbox(self.IB, listvariable=self.bankstr, width=15, height=12)
		self.bklb=tk.Listbox(self.IB, width=15, height=12)
		self.build_bklist()
		self.bklb.place(x=10, y=30)
		self.bklb.bind('<<ListboxSelect>>', self.selected)
			
		# Create Bank Name
		self.CBS=tk.StringVar(self.IB)
		tk.Label(self.IB, text="銀行名稱：").place(x=130, y=10)
		self.CB=tk.Entry(self.IB, width=13, textvariable=self.CBS)
		self.CB.place(x=200, y=10)
		
		# Create Bank code
		self.CBBS=tk.StringVar(self.IB)
		tk.Label(self.IB, text="銀行代號：").place(x=130, y=40)
		self.CBB=tk.Entry(self.IB, width=8, textvariable=self.CBBS)
		self.CBB.place(x=200, y=40)
		
		
		# Create Bank Account number	
		self.CBAS=tk.StringVar(self.IB)
		tk.Label(self.IB, text="銀行帳號:").place(x=180, y=80)
		self.CBA=tk.Entry(self.IB, width=23, textvariable=self.CBAS)
		self.CBA.place(x=130, y=100)
		
		# Create CURRENT Deposit
		self.CCDS=tk.StringVar(self.IB)
		tk.Label(self.IB, text="活期存款：").place(x=130, y=140)
		self.CCD=tk.Entry(self.IB, width=13, textvariable=self.CCDS)
		self.CCD.place(x=200, y=140)
				
		# Create FIX Deposit
		self.CFDS=tk.StringVar(self.IB)
		tk.Label(self.IB, text="定期存款：").place(x=130, y=170)
		self.CFD=tk.Entry(self.IB, width=13, textvariable=self.CFDS)
		self.CFD.place(x=200, y=170)

		# Create Button for New / Save / Cancel
		NBBT=tk.Button(self.IB, text="Add", bg='gray94', bd=2, command=self.new_bank)
		NBBT.place(x=130, y=210)
		SBBT=tk.Button(self.IB, text="Save", bg='gray94', bd=2, command=self.save_bank)
		SBBT.place(x=180, y=210)
		CBBT=tk.Button(self.IB, text="Del", bg='gray94', bd=2, command=self.del_bank)
		CBBT.place(x=230, y=210)		
		
		self.IB.mainloop()
	
	def conn_db(self, sqlc, *v):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc, *v)
			data=r.fetchall()
			conn.commit()
			conn.close()
			return data
	
	# Clear all entry
	def clear_all(self):
		self.CB.delete(0, 'end')
		self.CBB.delete(0, 'end')
		self.CBA.delete(0, 'end')
		self.CCD.delete(0, 'end')
		self.CFD.delete(0, 'end')	
		
	def selected(self, *w):
		self.clear_all()
		try:
			value=self.bklb.get(self.bklb.curselection())
			sql="SELECT * FROM INIT_BANK WHERE TITLE=? AND AUTH=?"			
			get_record=self.conn_db(sql, (value,self.usr, ))
			self.CB.insert(0, get_record[0][2])
			self.CBB.insert(0, get_record[0][3])
			self.CBA.insert(0, get_record[0][4])
			self.CCD.insert(0, get_record[0][5])
			self.CFD.insert(0, get_record[0][6])
		except:
			tk.messagebox.showerror(title='Error', message='Please select record!!')
	
	# Rebuild Bank List 
	def build_bklist(self):
		print("Function Build Bank List")
		self.bklb.delete(0,'end')
		GB=self.conn_db(self.getbank, (self.usr,))
		for x in range(len(GB)):
			self.bklb.insert(x, GB[x][0])
		
	def new_bank(self):	
		sql='INSERT INTO INIT_BANK (AUTH, TITLE, CODE, ACCOUNT, CUR_DEP, FIX_DEP) VALUES (?, ?,?,?,?,?)'
		self.conn_db(sql, (self.usr, self.CB.get(), self.CBB.get(), self.CBA.get(), self.CCD.get(), self.CFD.get(),))
		#Rebuild list
		self.build_bklist()
		self.clear_all()
		
	def save_bank(self):
		value=self.bklb.get(self.bklb.curselection())
		sql='UPDATE INIT_BANK SET TITLE=?, CODE=?, ACCOUNT=?, CUR_DEP=?, FIX_DEP=? WHERE TITLE=? AND AUTH=?'
		self.conn_db(sql, (self.CBS.get(), self.CBBS.get(), self.CBAS.get(), self.CCDS.get(), self.CFDS.get(), value, self.usr,))
		#Rebuild list
		self.build_bklist()
		
	def del_bank(self):
		try:
			value=self.bklb.get(self.bklb.curselection())
			sql='DELETE FROM INIT_BANK WHERE TITLE=? AND AUTH=?'
			self.conn_db(sql, (value, self.usr))
			#Rebuild list
			self.build_bklist()
			
			self.clear_all()
		except:
			tk.messagebox.showerror(title='Error', message='Please select record!!')
