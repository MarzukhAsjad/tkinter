# '''
# This is a simple tkinter implementation 
# of a simple calculator which supports adding, 
# multiplying, subtracting and dividing numbers
# '''

from tkinter import *

# creating the root window and naming it
root = Tk()
root.title("Simple Calculator")

# global variable
tracker = 0
current_val_1 = 0
current_val_2 = 0
operator = 0

# creating the input field
input = Entry(root, width=50, borderwidth=5)
input.grid(row=0, column=0, columnspan=3, pady=7)


# this will put the number into the input field
def button_click(number):
    global tracker
    if (tracker == 0):
        input.delete(0, END)
    input.insert(tracker, str(number)) 
    tracker += 1

def clear_input():
    global tracker
    input.delete(0, END)
    tracker = 0

def store_number(number):
    global tracker, current_val_1, operator
    current_val_1 = int(input.get())
    input.delete(0, END)
    operator = number
    tracker = 0
    
def equal_operation(event):
    global tracker, current_val_1, current_val_2, operator
    current_val_2 = int(input.get())
    input.delete(0, END)
    if (operator == 1):
        input.insert(0, str(current_val_1 + current_val_2))
    elif (operator == 2):
        input.insert(0, str(current_val_1 * current_val_2))
    elif (operator == 3):
        input.insert(0, str(current_val_1 - current_val_2))
    elif (operator == 4):
        input.insert(0, str(int(float(current_val_1) / float(current_val_2))))
    tracker = 0
    operator = 0

button0 = Button(root, text="0", padx=40, pady=20, borderwidth=5, command=lambda: button_click(0))
button1 = Button(root, text="1", padx=40, pady=20, borderwidth=5, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, borderwidth=5, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, borderwidth=5, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, borderwidth=5, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, borderwidth=5, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, borderwidth=5, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, borderwidth=5, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, borderwidth=5, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, borderwidth=5, command=lambda: button_click(9))
button_clear = Button(root, text="Clear", padx=80, pady=20, borderwidth=5, command= clear_input)
button_plus = Button(root, text="+", padx=40, pady=20, borderwidth=5, command=lambda: store_number(1))
button_minus = Button(root, text="-", padx=40, pady=20, borderwidth=5, command=lambda: store_number(3))
button_multiply = Button(root, text="x", padx=40, pady=20, borderwidth=5, command=lambda: store_number(2))
button_divide = Button(root, text="/", padx=40, pady=20, borderwidth=5, command=lambda: store_number(4))
button_equal = Button(root, text="   =   ", padx=81, pady=20, borderwidth=5, command=lambda: equal_operation('<Button-1>'))

# binding keys to the buttons
root.bind("<Return>", equal_operation)

button9.grid(row=1, column=2)
button8.grid(row=1, column=1)
button7.grid(row=1, column=0)
button6.grid(row=2, column=2)
button5.grid(row=2, column=1)
button4.grid(row=2, column=0)
button3.grid(row=3, column=2)
button2.grid(row=3, column=1)
button1.grid(row=3, column=0)
button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_minus.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)




root.mainloop()