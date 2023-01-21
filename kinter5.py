# This tutorial covers radio buttons implementation

from tkinter import *

root = Tk()
root.title("Radio Button")
root.iconbitmap('pictures/coding.ico')

r = IntVar() #this can be StrVar() if the values were strings like value = "1"
r.set(2) # setting this value initially will keep an optin selected by default

def clicked(value):
    global myLabel
    myLabel.config(text= str(value))

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack(padx=50, pady=10)
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(text=r.get())
myLabel.pack()
mainloop()