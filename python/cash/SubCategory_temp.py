"""
Version:0.0.01
Histroy: 
2018/7/23 - Initial Version

Waiting Imporve / Fix:
I001- conn_db function cannot input with variables

Modify Date: 2018/7/23
"""

import pickle
import sqlite3
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

class SubCategory:
	def __init__(self):
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
		gr=self.conn_db('SELECT MC_NAME FROM MAIN_CAT')
		self.val=tk.StringVar()
		self.SCMB=ttk.OptionMenu(self.SC, self.val, gr[0],*gr, command=self.getSC)
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
	def conn_db(self, sqlc):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc)
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
		for main_cat in gr:
			self.SCtree.insert('','end', values=main_cat)		
		self.SCtree.pack()
		
	def getSC(self, SCName):
		#print(SCName)
		self.MC=SCName
		sql='SELECT SBCID, SUBC_NAME FROM SUB_CAT WHERE MCID=(SELECT MCID FROM MAIN_CAT WHERE MC_NAME="'+SCName[0]+'")'
		#print(sql)
		self.gr=self.conn_db(sql)
		#print(self.gr)
		self.tree_data(self.gr)
		
	def add_sub(self, sce):
		print('add sub')
		print(self.MC[0])
		
		"""
		conn1=sqlite3.connect(r'db/test.db')
		c1=conn1.cursor()
		print('11:', self.MC[0])
		sql="SELECT MCID FROM MAIN_CAT WHERE MC_NAME=?"
		sql2="self.MC[0],"
		r1=c1.execute(sql,sql2)
		#r1=c1.execute("SELECT MCID FROM MAIN_CAT WHERE MC_NAME=?", (self.MC[0],))
		print(r1)
		"""
		#Trying: Method1
		sql="SELECT MCID FROM MAIN_CAT WHERE MC_NAME='"+self.MC[0]+"'"  #OK
		
		#sql="'SELECT MCID FROM MAIN_CAT WHERE MC_NAME=?', (self.MC[0],)" #NG
		#print('sql:',sql)
		sqlr=self.conn_db(sql)[0][0]
		#print('sql result', sqlr)		
		
		
		
		#sql=SELECT MCID FROM MAIN_CAT WHERE MC_NAME=?, (self.MC)
		#print(sql)
		#gmid=self.conn_db(sql)
		#sql=(self.conn_db('SELECT MCID FROM MAIN_CAT WHERE MC_NAME=?;', (self.MC)))
		#print('==sql==', sql)
		#test=self.conn_db(sql)
		#print(test)
		#sql='INSERT INTO SUB_CAT(MCID, SUBC_NAME) VALUES (?, ?)', (gmid,sce)
		#print(sql)
		#mid=self.conn_db(gmid)[0]
		#print('type:', type(mid))
		#print('mid', mid)
		#gr=self.conn_db('INSERT INTO SUB_CAT(MCID, SUBC_NAME) VALUES (?, ?)', (gmid,sce))
		#INSERT INTO SUB_CAT(MCID, SUBC_NAME) VALUES ("1", "TEST")
		#ad="INSERT INTO SUB_CAT(MCID, SUBC_NAME) VALUES (""+1+"", "TEST")"
	
	def edit_sub():
		print('edit sub')
	
	def del_sub():
		print('del_sub')
		
		
SubCategory()