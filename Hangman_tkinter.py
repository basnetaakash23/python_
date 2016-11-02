from tkinter import*

import time
import random

root= Tk()
top = Tk()


top.title('Hangmanz') 
top.geometry('500x140')

root.geometry('200x250')
root.title('Photo')




def appear(index, letter):
    # This line would be where you insert the letter in the textbox
    guess = ('')
    guess += str(letter)
    if letter in line:
        print(char,end=''),



    # set the players guess to guesses







    w.insert(0,letter)

    # Disable the button by index
    buttons[index].config(state="disabled")







letters=["Q", "A", "Z", "W", "S", "X", "E", "D", "C", "R", "F", "V", "T", "G", "B",
         "Y", "H", "N", "U", "J", "M", "I", "K", "O", "L", "P"]

# A collection (list) to hold the references to the buttons created below
buttons = []

for index in range(26): 
    n=letters[index]

    button = Button(top, bg="White", text=n, width=5, height=1, relief=GROOVE,
                    command=lambda index=index, n=n: appear(index, n))

    # Add the button to the window
    button.grid(padx=2, pady=2, row=index%3, column=index//3)

    # Add a reference to the button to 'buttons'
    buttons.append(button)

w = Entry(root,width=22, fg="black",
bg="#f2f2f2", font="Impact")
w.pack()



#photo   
canvas = Canvas(root,width = 200, height = 200, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'Scaffold01.gif')
canvas.create_image(50, 10, image = gif1, anchor = NW)

ok=True
while ok==True:
    answer = input ("Would you like to input a new word? Enter Y or N ")

    if answer == ('Y'):
        file = open("Hangmanwords.txt", "a")
        d =input("enter new word ")
        file.write("\n"+d)
        file.close()
        c=input("would you like to add another word? Y or N")
        if c == ('y'):
            ok=True
        elif c == ('N'):
            ok=False
    elif answer == ('N'):
            ok=False
time.sleep(1)
print("Get ready to play!")



line = random.choice(open("Hangmanwords.txt","r").readlines())
print(line)

for char in line:
        print("*")





root.mainloop()
top.mainloop()
