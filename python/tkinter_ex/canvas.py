import tkinter as tk

def moveit():
	c.move(ret, 20,0)

def moveit1():
	c.move(ret, -20,0)	
	
tko=tk.Tk()
tko.title("Canvas")
tko.geometry('300x700')


#MENU Sample---------------------------
#新增MENU
men=tk.Menu(tko)
#再新增MENU下的file
file=tk.Menu(men, tearoff=0)
#把file增加到MENU上
men.add_cascade(label='File', menu=file, underline=0)

#增加file的選項
file.add_command(label='New')
file.add_command(label='Open')
file.add_command(label='Save')

#增加分隔線
file.add_separator() 

# File再加Submenu
files=tk.Menu(file, tearoff=0)
file.add_cascade(label='Other', menu=files)
files.add_command(label='Load old')

file.add_command(label='Exit')

edit=tk.Menu(men, tearoff=0)
men.add_cascade(label="Edit", menu=edit)
edit.add_command(label='CUT')
edit.add_command(label='COPY')
edit.add_command(label='PASTE')


#Config Menu Bar
tko.config(menu=men)

#新增圖片/各種圖型-----------------------
c=tk.Canvas(tko, bg='pink', width=300, height=600).pack(ipady=130)
imgf=tk.PhotoImage(file='D:\se\py\lion.png')
img=c.create_image(150, 150, image=imgf)
#放圖片
#從什麼位置放，150/150，Default 是中間， 可用anchor來控制 NW/N/NE/E/SE/S/SW/W

li=c.create_line(75,280,75,550, width=5)
#畫線

ov=c.create_oval(125,280,175,320, fill='sky blue')
#產生橢圓形

poly=c.create_polygon(125, 350, 175, 350, 200, 400, 175, 450, 125, 450, 100, 400, fill='light yellow')
#多邊形

ret=c.create_rectangle(125,500,175,550, fill='green')
#長方形

but=tk.Button(text='Change Left', command=moveit, cursor='man')
but.pack(anchor='ne', side='left')
but1=tk.Button(text='Change Right', command=moveit1, cursor='man')
but1.pack(anchor='nw', side='right')


tko.mainloop()

