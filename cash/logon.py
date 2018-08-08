"""
Version:0.0.05
Histroy: 
2017/07/20 - Change Title/Frame Size
2081/07/10 - Clarify Folder, Change the path
2018/07/06 - reg_user function completed
2018/07/05 - Copy from pickleT.py & check_id_pw function completed
2018/08/08 - Improve function for conn_db()

Waiting Imporve / Fix:
I001-Add Logo

Modify Date: 2018/7/20

"""
import pickle
import sqlite3
import mainFR
import tkinter as tk
from tkinter import messagebox


# Connect to DB and create cursor
def conn_db(sqlc, *v):		
		conn=sqlite3.connect(r'db/test.db')
		c=conn.cursor()
		r=c.execute(sqlc, *v)
		data=r.fetchall()
		conn.commit()
		conn.close()
		return data

		
def check_id_pw():
		conn=sqlite3.connect(r'db/test.db')
		c=conn.cursor()
		
		# Get User's Password
		sql='SELECT PW from USER WHERE NAME=?'
		rs=conn_db(sql, (id.get(),))
		#print('here', rs)
		
		# If user does not exist, fetch will return none
		if len(rs)==0:
			tk.messagebox.showerror(title='Error', message='Incorrect Account!!')
		else:	
			# Transfer user data from tuple to string
			#print(rs[0][0])
			rst=str(rs[0][0])
			#print("rst:", rst, " ", "pwget:", pw.get())
			# Check password
			if rst== pw.get():
				tk.messagebox.showinfo(title='Info', message='Log on successfully!!')
				sql='SELECT ID FROM USER WHERE NAME=?'
				lgid=conn_db(sql, (id.get(),))
				tko.destroy()
				#print('logon:', lgid[0][0])
				mainFR.main(lgid[0][0])
				
			else:
				tk.messagebox.showerror(title='Error', message='Log on failed!')			

def reg_user():	

	#Clear all Input Data
	def clear_all():
		idr.delete(0, 'end')
		nic.delete(0, 'end')
		mailr.delete(0, 'end')
		pwr.delete(0, 'end')
		
		user_reg.destroy()
	
	def to_reg():
		#print(idr.get(), nic.get(), mailr.get(), pwr.get())
		sql='SELECT PW from USER WHERE NAME=?'
		print("id.get", id.get())
		rs=conn_db(sql, (id.get(),))
		print('p1:', len(rs))
		
		
		if len(rs)==0:
			sql='INSERT INTO USER (NAME, NICK, PW, MAIL) VALUES (?,?,?,?)'
			conn_db(sql,(idr.get(), nic.get(), pwr.get(), mailr.get(),))

		else:
			tk.messagebox.showwarning(title='Warning', message='User Exists!!')
		
		user_reg.destroy()
		
	#Create Registration Windows
	user_reg=tk.Toplevel(tko)
	user_reg.title("Registration Windows")
	user_reg.geometry('300x150')
	
	
	#Registration information Name(id)/Mail/Password
	tk.Label(user_reg, text='User Name: ').place(x=10, y=10)
	idr=tk.Entry(user_reg, show=None)
	idr.place(x=120, y=10)
	
	tk.Label(user_reg, text='Nickname: ').place(x=10, y=30)
	nic=tk.Entry(user_reg, show=None)
	nic.place(x=120, y=30)
	
	tk.Label(user_reg, text='Mail: ').place(x=10, y=50)
	mailr=tk.Entry(user_reg, show=None)
	mailr.place(x=120, y=50)
	
	tk.Label(user_reg, text='Password: ').place(x=10, y=70)
	pwr=tk.Entry(user_reg, show='*')
	pwr.place(x=120, y=70)
	
		
	regc=tk.Button(user_reg, text='Cancel', command=clear_all)
	regc.place(x=120, y=100)
	regok=tk.Button(user_reg, text='OK', command=to_reg)
	regok.place(x=80, y=100)
	
def exit_pro():
	tko.destroy()

#Create Logon Windows
tko=tk.Tk()
tko.title("Money Life")
tko.geometry('300x100')	

#User ID Label / Input
tk.Label(tko, text='User Name: ').place(x=10, y=10)
id=tk.Entry(tko, show=None)
id.place(x=120, y=10)

#User Password / Input
tk.Label(tko, text='Password: ').place(x=10, y=30)
pw=tk.Entry(tko, show='*')
pw.place(x=120, y=30)

#Registration Button
regb=tk.Button(tko, text='Registration', command=reg_user)
regb.place(x=60, y=60)

#Log on Button
logb=tk.Button(tko, text="Log on", command=check_id_pw)
logb.place(x=150, y=60)

#Exit Button
logb=tk.Button(tko, text="Exit", command=exit_pro)
logb.place(x=250, y=60)

tko.mainloop()