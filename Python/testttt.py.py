from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog

timmy = Tk()
timmy.title("Calculator")
timmy.configure(background="black")

#layout
frame = Frame(timmy)
theLabel = Label(text="This is a calculator")
theLabel.pack()
'''
.mainloop helps display the text
But what is theLabel? Purpose?
'''
#interface
button1 = Button(text="Calculate")
'''
adding "frame" as the first parameter makes "Calculate" button disappear.
'''
button1.pack()

operator=""
#enables user to type inside input
text_Input = StringVar()

def register():
    name = simpledialog.askstring("doo doo poo poo", "woo?")
'''
    Label(timmy, text="First Name").grid(row=0)
    Label(timmy, text="Last Name").grid(row=1)
    
    firstName = Entry(timmy)
    lastName = Entry(timmy)
    
    firstName.grid(row=0, column=1)
    lastName.grid(row=1, column=1)
'''

button2 = Button(timmy, text="Register", command=register)

button2.pack()

typeUr = Button(timmy, text="")

timmy.mainloop()
