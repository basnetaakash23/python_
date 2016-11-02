import tkinter as tk

counter=0
def counter_label(label):
    counter=0
    def count():
        global counter
        counter+=1
        label.config(text=str(counter))
        label.after(100,count)
    count()
    

root=tk.Tk()
root.title("Counting Seconds")
label=tk.Label(root,fg="dark green")
label.pack()
counter_label(label)
button=tk.Button(root,text="Stop",width=60, height=60, command=root.destroy)
button.pack()
root.mainloop()
