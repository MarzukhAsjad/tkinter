# '''
# This will cover a further implementation of 
# numerous Radiobuttons with a loop and using
# StringVar instead of IntVar for values
# '''

from tkinter import *

root = Tk()
root.title("Radio Button (2)")
root.iconbitmap('pictures/coding.ico')

pizza = StringVar() #this can be StrVar() if the values were strings like value = "1"

# list of pizza toppings used for the radiobutton options
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza.set('None') # setting this value initially will keep an optin selected by default

def clicked(value):
    global myLabel
    myLabel.config(text=str(value))

for text, value in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=value, command=lambda: clicked(pizza.get())).pack(padx=10, pady=10, anchor=W)


myLabel = Label(text=pizza.get())
myLabel.pack()
mainloop()