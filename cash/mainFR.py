import pickle
import sqlite3
import tkinter as tk
from tkinter import messagebox

def main():

	tko=tk.Tk()
	tko.title("Main Menu")
	tko.geometry('300x300')	
	
	def balanced():
		print("b_working")
		balf=tk.Toplevel(tko)
		balf.geometry('300*500')
		
		target=tk.Button(balf, text='Exit', command=Exit)
		target.place(x=60, y=100)
		
	def daily():
		print("d_working")
		
	def target():
		print("t_working")	
	
	bal=tk.Button(tko, text='Balanced', command=balanced)
	bal.place(x=60, y=20)

	daily=tk.Button(tko, text='Daily', command=daily)
	daily.place(x=60, y=60)
	
	target=tk.Button(tko, text='Target', command=target)
	target.place(x=60, y=100)
		
	tko.mainloop()