"""
Version:x.x.x
Histroy: 
This file is for Debug / Try & Error

Modify Date: 2018/7/23
"""

import pickle
import sqlite3
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

TK=tk.Tk()
TK.title("Sub Category Editor")
TK.geometry('250x350')

def action1(x):
	print(x)


def test(x):
	print(x)

val=tk.StringVar()
list=['aaa', 'bbb', 'ccc']
val.set(list[0])
op=tk.OptionMenu(TK, val, *list, command=action1)
#op=tk.OptionMenu(TK, val, 'a', 'b' ,'c', command=test(val))
op.pack()



TK.mainloop()
