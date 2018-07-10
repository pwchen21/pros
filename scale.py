import tkinter as tk

tko=tk.Tk()
tko.title("Scale Test")
tko.geometry("300x300")


def print_sel(v):
	l.config(text='You selected:' + v)

l=tk.Label(tko, bg='yellow',text='N/A')
l.pack()

s=tk.Scale(tko, bg='pink', orient=tk.HORIZONTAL, resolution=5, length=200, from_=50, to=200, relief=tk.SOLID, troughcolor='light sky blue', cursor='coffee_mug', command=print_sel)
#resoultion:一格跳多少
#from_, to:起始值即結束值
#Bar的長度



s.pack()

tko.mainloop()