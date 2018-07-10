import tkinter as tk

#New Tk object
tko=tk.Tk()
tko.title("ListBox Test")
tko.geometry("200x300")


#Function print select for btn
def print_con():
	#print('print select')
	value=lb.get(lb.curselection()) #lb.cuselection will get the index selected, lb.get will get the value
	#print(value)
	bs.set(value)
	#print('bs:', bs)
	
#Function add item for pbtn
def add_item():
	print('add_item')
	es=e.get()
	lb.insert('end', es)
	
#Function to delete select item
def del_item():
	lb.delete(lb.curselection())

#Create List Box
lbsv=tk.StringVar()
lbsv.set(('肥宅', '胖子', '喵喵'))
lb=tk.Listbox(tko, listvariable=lbsv, bg='pink')
lb.pack()

#Create Label
bs=tk.StringVar()
l=tk.Label(tko,bg='royal blue', width=10, textvariable=bs)
l.pack()

#Create button to print
btn=tk.Button(tko, text="Print Select", command=print_con).pack()

#Create Entry
es=tk.StringVar()
e= tk.Entry(tko, show=None, bg='green')
e.pack()

#Create button to add items
pbtn=tk.Button(tko, text="Add Items", command=add_item).pack()

#Create button to delete items
dbtn=tk.Button(tko, text="Del Item", command=del_item).pack()

tko.mainloop()