import tkinter as tk
from temp3 import temp3c

TK=tk.Tk()
TK.title("Teset File")
TK.geometry('250x350')

def TC():
    B=temp3c
    B.fun1()

nbtb=tk.Button(TK, text='testing', command=TC)
nbtb.pack()

TK.mainloop()