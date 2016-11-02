from tkinter import *
root=Tk()

v=IntVar()

Label(root,text="""Choose a language:""",justify=LEFT,padx=20).pack()
Radiobutton(root,text="Python",padx=10,value=1).pack(anchor=W)
Radiobutton(root,text="Perl",padx=20,value=3).pack(anchor=E)
mainloop()
