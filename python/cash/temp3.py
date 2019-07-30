"""
Version:x.x.x
Histroy: 
This file is for Debug / Try & Error
"""


import tkinter as tk    

class temp3c():
    def fun1():
        TK3=tk.Tk()
        TK3.title("Teset File")
        TK3.geometry('200x300')
        tk.Label(TK3, text="Temp3：").pack()
        ls=['aa','bb','cc','dd']
        a=tk.StringVar(TK3)
        a.set(ls)
        print('t:',a.get())
        A=tk.Listbox(TK3, listvariable=a)
        A.pack()                        
        TK3.mainloop()
		
#A1=temp3c
#A1.fun1()