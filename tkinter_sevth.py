from tkinter import*

root=Tk()

v=IntVar()
v.set(0) #initializing the choice, i.e Python

languages=[
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
    ]

def ShowChoice():
    print(v.get())

Label(root, text="""Choose your fovorite programming language:""",justify=LEFT, padx=20).pack()

for (txt,val) in languages:
     Radiobutton(root, 
                text=txt,
                indicatoron = 0,
                width = 20,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

Button(root,text="ENd", width=20,padx=20, command=root.destroy).pack(anchor=W)


mainloop()
    
    
