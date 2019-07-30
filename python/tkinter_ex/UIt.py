import tkinter as tui

"""
def __init__(self, master=None):
	tk.Frame.__init__(self, master)
	self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
	self.createWidgets()

def createWidgets(self):
	top=self.winfo_toplevel()
	top.rowconfigure(0, weight=1)
	top.columnconfigure(0, weight=1)
	self.rowconfigure(0, weight=1)
	self.columnconfigure(0, weight=1)
	self.quit = Button(self, text='Quit', command=self.quit)
	self.quit.grid(row=0, column=0,
	sticky=tk.N+tk.S+tk.E+tk.W)

createWidgets()
"""


hit = False
def btn_hit():  # For Button / Lable Example
	#print('test')
	global hit
	if hit == False:
		print('1')
		hit = True
		bs.set('肥宅不出門')
	else:
		print('2')
		hit = False
		bs.set('Let\'s GO')
		

def ins_p(): #b1 插入至選取的最前端
	#help(e)
	bs=e.get()
	tx.insert('insert', bs)
	#tx.insert(2.2, bs2) #插入至指定位置，如果沒有等同於insert

def ins_e(): #b2 插入至選取的尾端
	bs=e.get()
	tx.insert('end', bs)


tko=tui.Tk() #宣告TK物件
tko.title("Input Items") #設定視窗title
tko.geometry('300x500')  #設定視窗大小

                   
bs = tui.StringVar()
#bs.set('NOT HIT!')
#bs.set('aa')

#Text example 
tx = tui.Text(tko, height=3, bg='pink')  #宣告text，放置多次輸入資訊
tx.pack()


#Label example
l = tui.Label(tko, textvariable=bs, bg='blue',  font=('Calibri', 12), width=15, height=2)
l.pack(pady=10, padx=10, side="top")

#Button example 
b = tui.Button(tko, text='b-呼叫肥宅', bg='navy', activebackground='yellow', width=15, height=2, command=btn_hit) # Change Lable by btn_hit
b.pack(pady=10, padx=10, side="top")

#Entry & Button
e= tui.Entry(tko, show=None, bg='green')
e.pack()
#show = '*' 不要顯示鍵入的值

b1 = tui.Button(tko, text='b1-想和肥宅說說話', bg='navy', width=15, height=2, command=ins_p).pack()
b2 = tui.Button(tko, text='b2-不要說話', bg='navy', width=15, height=2, command=ins_e).pack()


#frame=tui.Frame(tko, borderwidth=100)
#button=tui.Button(frame, activebackground='#000000')
#tko.grid_bbox(column=None, row=None, col2=None, row2=None)
#button=tui.Button(frame, text="EXIT", command=tko.destroy)
#button.pack(side="bottom")
tko.mainloop()

