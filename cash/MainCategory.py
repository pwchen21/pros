"""
Version:0.0.01
Histroy: 
2018/7/20 - Initial Version

Waiting Imporve / Fix:
I001-Unselect for edit delete
I002-Add Exit

Modify Date: 2018/7/20
"""

import pickle
import sqlite3
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox


class MainCategory:

	def __init__(self):
		# Create main category editor
		self.MC=tk.Tk()
		self.MC.title("Main Category Editor")
		self.MC.geometry('250x350')	
		
		# Create title for main category
		MCLB=ttk.Label(self.MC, text="Main Category")
		MCLB.pack()
		
		# Create Frame
		self.MCF=ttk.Frame(self.MC)
		self.MCF.pack(fill='both', expand='false')
		
		# Create Treeview
		self.tree=ttk.Treeview(self.MCF, columns=['MCID', 'MC_NAME'],show='headings')
		self.tree.column('MCID', width=80, anchor='center')
		self.tree.heading('MCID', text="ID")
		self.tree.column('MC_NAME', width=150, anchor='center')
		self.tree.heading('MC_NAME', text="Name")
		
		self.gr=self.conn_db('SELECT * FROM MAIN_CAT')
		self.tree_data(self.gr)
		
		# Create Label for New / Edit
		self.MCL=tk.Label(self.MC, text='Category Name:')
		self.MCL.place(x=20, y=260)
		self.MCE=tk.Entry(self.MC, show=None, width=10)
		self.MCE.place(x=130, y=260)
		
		
		# Create button for New & Edit & Delete
		self.MCADD=tk.Button(self.MC, text="ADD", width=7, bg='gray94', bd=2, command=lambda:self.add_main(self.MCE.get()))
		self.MCADD.place(x=20, y=300)
		
		MCEDIT=tk.Button(self.MC, text="CHANGE", width=7, bg='gray94', bd=2, command=self.edit_main)
		MCEDIT.place(x=90, y=300)
		
		self.MCDEL=tk.Button(self.MC, text="DEL", width=7, bg='gray94', bd=2, comman=lambda:self.del_main(self.MCE.get()))
		self.MCDEL.place(x=160, y=300)
				
		self.MC.mainloop()
	
	# Connect to DB and create cursor
	def conn_db(self, sqlc):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc)
			data=r.fetchall()
			conn.commit()
			conn.close()
			return data

	
	def tree_data(self,gr):
		#Improve Needed: Trying to find a goodway to destroy tree??
		#self.tree.delete(self.tree.get_children())		
		for i in self.tree.get_children():
				self.tree.delete(i)
		for main_cat in gr:
			self.tree.insert('','end', values=main_cat)		
		self.tree.pack()
	
	def rebuild_tree(self):
		gr=self.conn_db('SELECT * FROM MAIN_CAT')
		self.gr=gr
		self.tree_data(gr)
	
	#Function Add Main Category
	def add_main(self,mce):
		ad="INSERT INTO MAIN_CAT (MC_NAME) VALUES ('"+ mce + "')"
		self.conn_db(ad)
		
		self.rebuild_tree()
	
	#Function Edit Main Category
	def edit_main(self):
		#Focus on selection
		ms=self.tree.selection()
		#Get value for selection item
		if len(ms)!=0:		
			select=self.tree.item(ms)['values'][1]	
			sqlc="UPDATE MAIN_CAT SET MC_NAME='"+self.MCE.get()+"' WHERE MC_NAME='"+select+"'"
			self.conn_db(sqlc)
		else:
			tk.messagebox.showerror(title='Error', message='Please select record!!')
		self.rebuild_tree()

	#Function Delete Main Category
	def del_main(self,mce):
		#Focus on selection
		ms=self.tree.selection()		
		#Get value for selection item & Check selection
		if len(ms) != 0:
			select=self.tree.item(ms)['values'][1]
			ad="DELETE FROM MAIN_CAT WHERE MC_NAME ='"+ select + "'"
			self.conn_db(ad)
		else:
			tk.messagebox.showerror(title='Error', message='Please correct record!!')
		self.rebuild_tree()

MainCategory()