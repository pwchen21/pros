import tkinter as tk

class temp4c(tk.Frame):
	def __init__(self, *args, **kwargs):
		testc=tk.StringVar()
		testc.set('ABC')
		test=tk.Entry(self, width=13, textvariable=testc)
		test.pack()
		
if __name__ == '__main__':
		print('Init...')
		TK4=tk.Tk()
		test1=temp4c(TK4)
		test1.pack()
		#TK4.title("Teset File")
		#TK4.geometry('250x350')
		#TK4.mainloop()