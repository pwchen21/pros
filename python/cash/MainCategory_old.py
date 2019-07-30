import pickle
import sqlite3
import tkinter as tk
from tkinter import ttk

#import os
#from tkinter import messagebox


# Connect to DB and create cursor
def conn_db(sqlc):		
		conn=sqlite3.connect(r'db/test.db')
		c=conn.cursor()
		r=c.execute(sqlc)
		data=r.fetchall()
		conn.commit()
		conn.close()
		return data


def show_cat_now():
	
	# Create main category editor
	MC=tk.Tk()
	MC.title("Main Category Editor")
	MC.geometry('250x350')	
	
	#get all main category
	gr=conn_db('SELECT * FROM MAIN_CAT')
	
	# Create title for main category
	MCLB=ttk.Label(MC, text="Main Category")
	MCLB.pack()
	
	# Create frame for category table
	MCF=ttk.Frame(MC)	
	MCF.pack(fill='both', expand='false')
	
	def treev():
		tree=ttk.Treeview(MCF, columns=['MCID', 'MC_NAME'],show='headings')
		tree.column('MCID', width=80, anchor='center')
		tree.heading('MCID', text="ID")
		tree.column('MC_NAME', width=150, anchor='center')
		tree.heading('MC_NAME', text="Name")
		
		for main_cat in gr:
			tree.insert('','end', values=main_cat)
		
		tree.pack()

	treev()
	
	# Create Label for New / Edit
	MCL=tk.Label(MC, text='Category Name:').place(x=20, y=260)
	MCE=tk.Entry(MC, show=None, width=10)
	MCE.place(x=130, y=260)
	
	
	# Create button for New & Edit & Delete
	MCADD=tk.Button(MC, text="ADD", width=5, bg='gray94', bd=2, command=lambda:add_main(MCE.get()))
	MCADD.place(x=50, y=300)

	
	
	MCEDIT=tk.Button(MC, text="EDIT", width=5, bg='gray94', bd=2, command=edit_main)
	MCEDIT.place(x=100, y=300)
	
	MCDEL=tk.Button(MC, text="DEL", width=5, bg='gray94', bd=2, comman=lambda:del_main(MCE.get()))
	MCDEL.place(x=150, y=300)
	
	MC.mainloop()

def add_main(mce):
	print('===add main===')
	print(mce)
	ad="INSERT INTO MAIN_CAT (MC_NAME) VALUES ('"+ mce + "')"
	conn_db(ad)
	A=show_cat_now()
	A.treev()

	"""
	add_main=tk.Toplevel(MC)
	add_main_title("Add Category")
	add_main.geometry(150*150)
	"""
def edit_main():
	print('edit main')

def del_main(mce):
	print('===delete main===')
	print(mce)
	ad="DELETE FROM MAIN_CAT WHERE MC_NAME ='"+ mce + "'"
	print(ad)
	conn_db(ad)

show_cat_now()