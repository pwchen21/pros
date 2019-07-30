import pickle
import tkinter as tk
from tkinter import messagebox

class id_check:
	def __init__(self, i, p):
		self.id=i
		self.pwd=p
				
	def showinfo(self):
		print('Logon by: ' + self.id)	
		print('Password: ' + self.pwd)

			
			
def get_id_pw():

	nic=id_check(id.get(), pw.get())
	nic.showinfo()

def check_id_pw():
	try:
		with open(r'D:\se\py\user_info.pickle','rb') as usr_f:
			usr_info = pickle.load(usr_f)
	except FileNotFoundError:
			tk.messagebox.showerror(title='Error', message='Account Does NOT Exist')
	
	#print('idget: ' , id.get())
	#print('user_info: ' , usr_info)
	
	#print('1: ' , usr_info[id.get()][0])
	#print('2: ' , pw.get())
	
	# User in User File
	if id.get() in usr_info:
		# Check Password
		if usr_info[id.get()][0] == pw.get():			
			tk.messagebox.showinfo(title='Info', message='Log on correctly')
		# Incorrect password
		else:
			tk.messagebox.showerror(title='Error', message='Log on failed!')
	# User Not in User File
	else:
		tk.messagebox.showerror(title='Error', message='Incorrect Account')
def reg_user():	
	#Clear all Input Data

	def clear_all():
		idr.delete(0, 'end')
		mailr.delete(0, 'end')
		pwr.delete(0, 'end')
		user_reg.destroy()
	
	def to_reg():
		#Check file exist
		user=[]
		try:
			# Load original user file and append new register data
			with open(r'D:\se\py\user_info.pickle','rb') as usr_f:
				user = pickle.load(usr_f)
				print(user)
				print(idr.get())
				if  user.get(idr.get()):
					user_reg.destroy()
					tk.messagebox.showerror(title='Error', message='User Exist!')					
				else:
					user[idr.get()]=[pwr.get(),mailr.get()]				
			# Dump new data to file
			with open(r'D:\se\py\user_info.pickle','wb') as usr_f:
				pickle.dump(user, usr_f)
			user_reg.destroy()
		#If file does not exist create on and dump user info
		except FileNotFoundError:
			with open(r'D:\se\py\user_info.pickle','wb') as usr_f:
				user_info = {idr.get():[pwr.get(),mailr.get()]}
				pickle.dump(user_info, usr_f)
				user_reg.destroy()

		
	#Create Registration Windows
	user_reg=tk.Toplevel(tko)
	user_reg.title("Registration Windows")
	user_reg.geometry('300x150')
	
	
	#Registration information Name(id)/Mail/Password
	tk.Label(user_reg, text='User Name: ').place(x=10, y=10)
	idr=tk.Entry(user_reg, show=None)
	idr.place(x=120, y=10)
		
	
	tk.Label(user_reg, text='Mail: ').place(x=10, y=30)
	mailr=tk.Entry(user_reg, show=None)
	mailr.place(x=120, y=30)
	
	tk.Label(user_reg, text='Password: ').place(x=10, y=50)
	pwr=tk.Entry(user_reg, show='*')
	pwr.place(x=120, y=50)
	
		
	regc=tk.Button(user_reg, text='Cancel', command=clear_all)
	regc.place(x=120, y=80)
	regok=tk.Button(user_reg, text='OK', command=to_reg)
	regok.place(x=80, y=80)
	

#Create Logon Windows
tko=tk.Tk()
tko.title("Welcome to read!")
tko.geometry('300x300')	

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

tko.mainloop()