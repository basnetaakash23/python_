from tkinter import *
master=Tk()
var1=IntVar()
Checkbutton(master,text="male").grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master, text="female").grid(row=1,sticky=W)
mainloop()
