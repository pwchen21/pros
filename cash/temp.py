"""
Version:x.x.x
Histroy: 
This file is for Debug / Try & Error

"""

import pickle
import sqlite3
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from temp2 import teeemp

TK=tk.Tk()
TK.title("Teset File")
TK.geometry('250x350')

def TC():
	print("12345")
	teeemp.fun1()
	#temp2.ppt()

nbtb=tk.Button(TK, text='testing', command=TC)
nbtb.pack()

TK.mainloop()


#prfecct example
"""
def conn_db(sqlc, *w):		
		print(*w)
		conn=sqlite3.connect(r'db/test.db')
		c=conn.cursor()
		r=c.execute(sqlc, *w)
		data=r.fetchall()
		conn.commit()
		conn.close()
		return data
		
"""
"""		
def rg(x):
	print(x)

	
CDTS=tk.StringVar()
option=['Master', 'Visa', 'JCB']
tk.Label(TK, text="卡別：").pack()
rg(option[0])
CDTOM=ttk.OptionMenu(TK, CDTS, option[0], *option, command=rg)
CDTOM.pack()
"""


"""		
#t='abcde'
#c1=123
#ac=323921232343
#cd=400
#fd=1000
n='test'

sql='DELETE FROM INIT_BANK WHERE TITLE=?'
conn_db(sql, (n,))

#Perfect example for variable
#sql='INSERT INTO INIT_BANK (TITLE, CODE, ACCOUNT, CUR_DEP, FIX_DEP) VALUES (?,?,?,?,?)'
#conn_db(sql, (t,c1,ac,cd,fd))

#
print(conn_db('select * from INIT_BANK'))
#print(INSERT INTO INIT_BANK (TITLE, CODE, ACCOUNT, CUR_DEP, FIX_DEP) VALUES (?,?,?,?,?)', (t,c,ac,cd,fd))

# Below command is OK -----
# conn=sqlite3.connect(r'db/test.db')
# c=conn.cursor()
# c.execute('INSERT INTO INIT_BANK (TITLE, CODE, ACCOUNT, CUR_DEP, FIX_DEP) VALUES (?,?,?,?,?)', (t,c1,ac,cd,fd))
# conn.commit()
# -----
"""


