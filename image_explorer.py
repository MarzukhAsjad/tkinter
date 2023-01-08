# '''
# This is a tutorial on importing images and 
# placing them in the window
# '''

from tkinter import *
from PIL import Image, ImageTk

# global variables
label_index = 0

# root details
root = Tk()
root.title("Mizookie is learning tkinter")
root.iconbitmap("pictures/coding.ico")

# image importing
img1 = ImageTk.PhotoImage(Image.open("pictures/programmer.png"))
img2 = ImageTk.PhotoImage(Image.open("pictures/man.png"))
img3 = ImageTk.PhotoImage(Image.open("pictures/woman.png"))
img4 = ImageTk.PhotoImage(Image.open("pictures/woman (1).png"))
img5 = ImageTk.PhotoImage(Image.open("pictures/woman (2).png"))
img6 = ImageTk.PhotoImage(Image.open("pictures/clown.png"))

# label creating
label_1 = Label(image=img1)
label_2 = Label(image=img2)
label_3 = Label(image=img3)
label_4 = Label(image=img4)
label_5 = Label(image=img5)
label_6 = Label(image=img6)

# dictionary of labels
Labels = [label_1, label_2, label_3, label_4, label_5, label_6]
label_placed = Labels[label_index]

# Counter label
label_count = Label(root, text="Image " + str(label_index + 1) + " out of " + str(len(Labels)), bd=1, relief=SUNKEN, anchor=E)

# functions for button implementations
def backward():
    global label_index, label_placed, label_count

    label_index -= 1

    if (label_index == 0):
        button_backward["state"] = "disabled"
    else:
        button_forward["state"] = "active"
        button_backward["state"] = "active"

    label_placed.grid_forget()  # this is necessary as otherwise the image otherwise overlaps
    label_placed = Labels[label_index]
    label_count = Label(root, text="Image " + str(label_index + 1) + " out of " + str(len(Labels)), bd=1, relief=SUNKEN, anchor=E)
    label_placed.grid(row=0, column=0, columnspan=3)
    label_count.grid(row=2, column=0, columnspan=3, sticky='ew')
    print(label_index)
    return

def forward():
    global label_index, label_placed, label_count
    
    label_index += 1

    if (label_index == len(Labels) - 1):
        button_forward["state"] = "disabled"
    else:
        button_forward["state"] = "active"
        button_backward["state"] = "active"


    label_placed.grid_forget()
    
    label_placed = Labels[label_index]
    label_count = Label(root, text="Image " + str(label_index + 1) + " out of " + str(len(Labels)), bd=1, relief=SUNKEN, anchor=E)
    label_placed.grid(row=0, column=0, columnspan=3)
    label_count.grid(row=2, column=0, columnspan=3, sticky='ew')
    print(label_index)
    return

# button details
button_backward = Button(root, text=" < ", command=backward)
button_exit = Button(root, text="Click to quit", command=root.quit)
button_forward = Button(root, text=" > ", command=forward)

print(label_index)

# initial states of the forward and backward buttons
if label_index == 0:
    button_backward["state"] = "disabled"
elif label_index == len(Labels) - 1:
    button_forward["state"] = "disabled"

# positioning the widgets
Labels[label_index].grid(row=0, column=0, columnspan=3)
button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
label_count.grid(row=2, column=0, columnspan=3, sticky='ew')

root.mainloop()