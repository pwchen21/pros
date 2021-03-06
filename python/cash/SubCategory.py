"""
Version:0.0.04
Histroy: 
2018/07/26 - Initial Version
2018/08/03 - Add User authority
			Change EDIT/DELETE by ID
			FIX [F001] Change Modify/Delete According to ID
2018/08/08 - Improve user authority by logon
2018/08/22 - Fix F002
			
Waiting Imporve / Fix:
[Fixed-2018080300] F001: Delete/Modify for mobile phone will failed, because "0" will be igonored.
[Fixed-2018082200]F002: Can not shows default mail category.

Modify Date: 2018/08/22
"""

import pickle
import sqlite3
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

class SubCategory:
	def __init__(self, uid):
		# Temp user, this will be replace by variable 
		self.usr=uid
		# Create sub cateogory editor
		self.SC=tk.Tk()
		self.SC.title("Sub Category Editor")
		self.SC.geometry('250x350')
		
		# Create Frame: Top for title, Left for select maincategory, Right select Subcategory
		self.fr=tk.Frame(self.SC)
		self.FTitle=tk.Frame(self.fr, bg='green', cursor='man')
		self.FTitle.pack(side='top',expand=True)
		
		self.FMC=tk.Frame(self.fr, bg='blue')
		self.FMC.pack(side='left')
		
		self.FSC=tk.Frame(self.fr, bg='red')
		self.FSC.pack(side='right')
		
		#Variable for MC now
		self.MC=tk.StringVar()

		# Create Drop Down list for main category
		sql='SELECT MC_NAME FROM MAIN_CAT WHERE AUTH=?'
		gr=self.conn_db(sql, (self.usr, ))
		self.val=tk.StringVar(self.SC)
		print('val:', self.val)
		print('gr0', gr[0][0])
		self.SCMB=ttk.OptionMenu(self.SC, self.val, gr[0], *gr, command=self.getSC)
		self.SCMB.pack()
		
		
		# Create Sub category Treeview
		self.SCtree=ttk.Treeview(self.SC, columns=['SCID', 'SC_NAME'],show='headings')
		self.SCtree.column('SCID', width=80, anchor='center')
		self.SCtree.heading('SCID', text="ID")
		self.SCtree.column('SC_NAME', width=150, anchor='center')
		self.SCtree.heading('SC_NAME', text="Name")
		self.getSC(gr[0])
		
		# Create Label for New / Edit
		self.SCL=tk.Label(self.SC, text='Sub Category Name:')
		self.SCL.place(x=15, y=260)
		self.SCE=tk.Entry(self.SC, show=None, width=10)
		self.SCE.place(x=140, y=260)
		
		
		# Create button for New & Edit & Delete
		self.SCADD=tk.Button(self.SC, text="ADD", width=7, bg='gray94', bd=2, command=lambda:self.add_sub(self.SCE.get()))
		self.SCADD.place(x=20, y=300)
		
		self.SCEDIT=tk.Button(self.SC, text="CHANGE", width=7, bg='gray94', bd=2, command=self.edit_sub)
		self.SCEDIT.place(x=90, y=300)
		
		self.SCDEL=tk.Button(self.SC, text="DEL", width=7, bg='gray94', bd=2, comman=lambda:self.del_sub(self.SCE.get()))
		self.SCDEL.place(x=160, y=300)
		
		self.SC.mainloop()		
	
	# Connect to DB and create cursor
	def conn_db(self, sqlc, *v):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc, *v)
			data=r.fetchall()
			conn.commit()
			conn.close()
			return data	
	
	# Create tree data
	def tree_data(self,gr):
		#Improve Needed: Trying to find a goodway to destroy tree??
		#self.tree.delete(self.tree.get_children())		
		for i in self.SCtree.get_children():
				self.SCtree.delete(i)
		for sub_cat in gr:
			#print(sub_cat)
			self.SCtree.insert('','end', values=sub_cat)		
		self.SCtree.pack()
	
	def rebuildsb(self,mcid):
		#print("==Rebuild Tree Now!===")
		sql='SELECT SBCID, SUBC_NAME FROM SUB_CAT WHERE MCID=?'
		#print('qrsql', grsql)
		gr=self.conn_db(sql,(str(mcid),))
		self.gr=gr
		self.tree_data(gr)
	
	def getSC(self, SCName):
		self.MC=SCName
		
		#print("1:", self.MC)
		sql='SELECT SBCID, SUBC_NAME FROM SUB_CAT WHERE MCID=(SELECT MCID FROM MAIN_CAT WHERE MC_NAME=? AND AUTH=?)'
		self.gr=self.conn_db(sql, (SCName[0], self.usr, ))
		self.tree_data(self.gr)	
	
	def add_sub(self, sce):
		#GET MAIN ID
		sql="SELECT MCID FROM MAIN_CAT WHERE MC_NAME=? AND AUTH=?" 
		sqlr=self.conn_db(sql, (self.MC[0], self.usr))[0][0]
		
		# Insert Command
		add="INSERT INTO SUB_CAT(AUTH, MCID, SUBC_NAME) VALUES (?, ?, ?)"
		#print('1:',add)
		self.conn_db(add, (self.usr, str(sqlr),sce,))
		self.rebuildsb(sqlr)
	
	def edit_sub(self):
		#GET MAIN ID
		sql="SELECT MCID FROM MAIN_CAT WHERE MC_NAME=? AND AUTH=?" 
		sqlr=self.conn_db(sql, (self.MC[0], self.usr, ))[0][0]
		
		#Focus on selection
		scms=self.SCtree.selection()
		
		#Get value for selection item
		if len(scms)!=0:		
			select=self.SCtree.item(scms)['values'][0]
			sqlc="UPDATE SUB_CAT SET SUBC_NAME=? WHERE SBCID=?"
			self.conn_db(sqlc, (self.SCE.get(), select, ))
		else:
			tk.messagebox.showerror(title='Error', message='Please select record!!')
		
		self.rebuildsb(sqlr)
		
	
	def del_sub(self,sce):
		#GET MAIN ID
		sql="SELECT MCID FROM MAIN_CAT WHERE MC_NAME=?" 
		sqlr=self.conn_db(sql, (self.MC[0], ))[0][0]
	
		#Focus on selection
		scms=self.SCtree.selection()
		#Get value for selection item & Check selection
		if len(scms) != 0:
			# !!!self.SCtree.item(scms) for mobile phone will cut 0
			select=str(self.SCtree.item(scms)['values'][0])			
			ad="DELETE FROM SUB_CAT WHERE SBCID=?"
			self.conn_db(ad, (select, ))
		else:
			tk.messagebox.showerror(title='Error', message='Please correct record!!')
		self.rebuildsb(sqlr)
