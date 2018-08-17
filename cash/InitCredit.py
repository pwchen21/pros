"""
Version:0.0.02
Histroy: 
2018/08/03 - Initial Version with User Authority
2018/08/08 - Improve user authority by logon (But Cannot get list by setting)


Waiting Imporve / Fix:
I001- Should EDIT/DELETE by ID
F001- Shows select record when using Tab(or multiple value selected) to change column 
F002- Cannot get list by setting

Modify Date: 2018/08/08
"""

import pickle
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class InitCredit:

	def __init__(self,uid):
		# Temp user, this will be replace by variable 
		self.usr=uid
		print('IC:', self.usr)
		# Create InitCredit
		self.IC=tk.Tk()
		self.IC.title("Init/Edit Credit")
		self.IC.geometry('310x335')
		
		# Create Credit Card List
		self.cdstr=tk.StringVar()
		self.getcd='select TYPE from INIT_CREDIT WHERE AUTH=?'
		print('data', self.conn_db(self.getcd, (self.usr,)))
		self.cdstr.set(self.conn_db(self.getcd, (self.usr,)))
		tk.Label(self.IC, text="信用卡列表：").place(x=33, y=10)
		#print('cdstr:', self.cdstr)
		self.cdlb=tk.Listbox(self.IC, listvariable=self.cdstr, width=15, height=16)
		self.cdlb.place(x=10, y=30)
		self.cdlb.bind('<<ListboxSelect>>', self.selected)
			
		# Create Bank Name
		self.CBS=tk.StringVar()
		tk.Label(self.IC, text="銀行名稱：").place(x=130, y=10)
		self.CBE=tk.Entry(self.IC, width=13, textvariable=self.CBS)
		self.CBE.place(x=200, y=10)
			
		# Create credit card name
		self.CDNS=tk.StringVar()
		tk.Label(self.IC, text="卡種：").place(x=130, y=40)
		self.CDNE=tk.Entry(self.IC, width=8, textvariable=self.CDNS)
		self.CDNE.place(x=200, y=40)
			
		# Create Credit card type	
		self.CDTS=tk.StringVar()
		option=['Master', 'VISA', 'JCB']
		self.get_card_type(option[0])
		tk.Label(self.IC, text="卡別：").place(x=130, y=70)
		self.CDTOM=ttk.OptionMenu(self.IC, self.CDTS, option[0], *option, command=self.get_card_type)
		self.CDTOM.place(x=200, y=70)
		
		# Create Credit card number
		self.CDCS=tk.StringVar()
		tk.Label(self.IC, text="信用卡號：").place(x=180, y=100)
		self.CDCE=tk.Entry(self.IC, width=23, textvariable=self.CDCS)
		self.CDCE.place(x=130, y=130)
		
		# Create CRC
		self.CDCRCS=tk.StringVar()
		tk.Label(self.IC, text="檢查碼").place(x=130, y=170)
		self.CDCRCE=tk.Entry(self.IC, width=13, textvariable=self.CDCRCS)
		self.CDCRCE.place(x=200, y=170)
		
		# Create Close Date
		self.CDCLS=tk.StringVar()
		tk.Label(self.IC, text="結帳日").place(x=130, y=200)
		self.CDCLE=tk.Entry(self.IC, width=13, textvariable=self.CDCLS)
		self.CDCLE.place(x=200, y=200)
		
		# Create PAY Date
		self.CDPDS=tk.StringVar()
		tk.Label(self.IC, text="付款日").place(x=130, y=230)
		self.CDPDE=tk.Entry(self.IC, width=13, textvariable=self.CDPDS)
		self.CDPDE.place(x=200, y=230)
		
		# Create STATUS 
		self.CDSTS=tk.StringVar()
		self.CDSTS.set('N')
		tk.Label(self.IC, text="啟用").place(x=130, y=260)
		self.CDSTCB=tk.Checkbutton(self.IC, offvalue='N', onvalue='Y', variable=self.CDSTS)
		self.CDSTCB.place(x=200, y=260)

		
		# Create Button for New / Save / Cancel
		NBBT=tk.Button(self.IC, text="Add", bg='gray94', bd=2, command=self.new_credit)
		NBBT.place(x=140, y=290)
		SBBT=tk.Button(self.IC, text="Save", bg='gray94', bd=2, command=self.save_credit)
		SBBT.place(x=190, y=290)
		CBBT=tk.Button(self.IC, text="Del", bg='gray94', bd=2, command=self.del_credit)
		CBBT.place(x=240, y=290)		
		
		
		self.IC.mainloop()
	
	def conn_db(self, sqlc, *v):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc, *v)
			data=r.fetchall()
			conn.commit()
			conn.close()
			return data
	
	
	def get_card_type(self, cardt):
		#print('test:', cardt)
		return cardt
	
	# Clear all entry
	def clear_all(self):
		self.CBE.delete(0, 'end')    # Bank Name
		self.CDNE.delete(0, 'end')   # Credit card name
		self.CDCE.delete(0, 'end')   # Credit card number
		self.CDCRCE.delete(0, 'end') # Credit card CRC
		self.CDCLE.delete(0,'end')   # Credit card Cycle date
		self.CDPDE.delete(0, 'end')	 # Credit card Pay date
	
	
	def selected(self, *w):
		try:
			value=self.cdlb.get(self.cdlb.curselection())[0]
			sql="SELECT * FROM INIT_CREDIT WHERE TYPE=? AND AUTH=?"
			get_record=self.conn_db(sql, (value, self.usr,))
			#print(get_record)
			
			self.CBS.set(get_record[0][2])
			self.CDNS.set(get_record[0][3])
			self.CDTS.set(get_record[0][4])
			self.CDCS.set(get_record[0][5])
			self.CDCRCS.set(get_record[0][6])
			self.CDCLS.set(get_record[0][7])
			self.CDPDS.set(get_record[0][8])
			self.CDSTS.set(get_record[0][9])
			
		except:
			tk.messagebox.showerror(title='Error', message='Please select record!!')
	
		
	def new_credit(self):	
		sql='INSERT INTO INIT_CREDIT (AUTH, BANK, TYPE, MVF, NUM, IDENTIFY, CYCLE, PAYDAY, STATUS) VALUES (?, ?,?,?,?,?,?,?,?)'
		self.conn_db(sql, (self.usr, self.CBE.get(), self.CDNE.get(), self.CDTS.get(), self.CDCE.get(), self.CDCRCE.get(), self.CDCLE.get(), self.CDPDE.get(), self.CDSTS.get()))
		#Rebuild list
		self.cdstr.set(self.conn_db(self.getcd, (self.usr,)))		
		self.clear_all()

		
	def save_credit(self):
		value=self.cdlb.get(self.cdlb.curselection())[0]
		sql='UPDATE INIT_CREDIT SET BANK=?, TYPE=?, MVF=?, NUM=?, IDENTIFY=?, CYCLE=?, PAYDAY=?, STATUS=? WHERE TYPE=? AND AUTH=?'
		self.conn_db(sql, (self.CBE.get(), self.CDNE.get(), self.CDTS.get(), self.CDCE.get(), self.CDCRCE.get(), self.CDCLE.get(), self.CDPDE.get(), self.CDSTS.get(), value, self.usr))
		#Rebuild & clear get entry
		self.cdstr.set(self.conn_db(self.getcd, (self.usr,)))	
		self.clear_all()
		
	def del_credit(self):
		try:
			value=self.cdlb.get(self.cdlb.curselection())[0]
			sql='DELETE FROM INIT_CREDIT WHERE TYPE=? AND AUTH=?'
			self.conn_db(sql, (value, self.usr))
			#Rebuild list
			self.cdstr.set(self.conn_db(self.getcd, (self.usr,)))
			
			self.clear_all()
		except:
			tk.messagebox.showerror(title='Error', message='Please select record!!')

			
#InitCredit(1)			