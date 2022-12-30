# '''
# This is a tutorial on creating buttons and
# implementing the commands on click
# '''

from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="#ffffff", bg="black")
e.pack()
e.insert(0, "Enter your Name: ") # this puts a default placeholder

def myClick():
    myLabel = Label(root, text= "Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="white", bg="#000000")
myButton.pack()

root.mainloop()