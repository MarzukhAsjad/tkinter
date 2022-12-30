# '''
# This is a introductory tutorial on inserting labels and 
# using the grid system to position widgets
# '''

from tkinter import *

# root widget (window)
root = Tk()

# initialisinig a widget (text label)
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Mizookie")

# shoving the label into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# main loop of GUI
root.mainloop()