# '''
# This is a tutorial on importing images and 
# placing them in the window
# '''

from tkinter import *
from PIL import Image, ImageTk

# root details
root = Tk()
root.title("Mizookie is learning tkinter")
root.iconbitmap("pictures/coding.ico")

# image details
img = ImageTk.PhotoImage(Image.open("pictures/programmer.png"))
label_img = Label(image=img)
label_img.pack()

# exit button details
button_exit = Button(root, text="Click to quit", command=root.quit)
button_exit.pack()

root.mainloop()