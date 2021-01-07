from tkinter import *

root = Tk()

canvas = Canvas(root, width=1000, height=800)
canvas.pack()
#What does canvas.pack or any.pack really do/how does it get interpreted?

black = canvas.create_line(0, 100, 0, 100)

root.mainloop()
#Without .mainloop, your program won't run,
