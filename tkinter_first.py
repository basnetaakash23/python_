#from Tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
from tkinter import *

root = Tk()

w = Label(root, text="Hello Tkinter!",bg="green").pack(side="left")

new_box=PhotoImage(file="C:/Users/Aakash Basnet/Downloads/image.gif")
explanation="""Sumit is a very horny guy."""
w2=Label(root, image=new_box, text=explanation,compound=LEFT,padx=40, fg="red").pack(side="top")

w1=Label(root, text=explanation,bg="green",fg="blue").pack(side="bottom")


root.mainloop()
