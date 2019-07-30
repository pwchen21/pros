import tkinter as tk

tko=tk.Tk()
tko.title('Frame')
tko.geometry('300x300')

tk.Label(tko, text='On the up frame').pack()


fr=tk.Frame(tko)
fr.pack()
"""
fr1=tk.Frame(fr, cursor='man')
fr2=tk.Frame(fr)
fr1.pack(side='left')
fr2.pack(side='right')
"""

fr1=tk.Frame(fr, bg='green', cursor='man', width=150, height=300)
fr2=tk.Frame(fr, bg='blue', width=150, height=300)
fr1.pack(side='left')
fr2.pack(side='right')


tk.Label(fr1, text='Content Fr1').pack(ipadx=10,ipady=30)
tk.Label(fr2, text='Content Fr2').pack(ipadx=10,ipady=30)

tk.Button(fr1, text='Button Fr1').pack()

fr1.pack(side='left')
fr2.pack(side='right')

tko.mainloop()