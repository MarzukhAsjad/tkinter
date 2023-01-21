# this is a tutorial to cover frame implementation

from tkinter import *

root = Tk()
root.title('Frame Implementation')
root.iconbitmap('pictures/coding.ico')

frame = LabelFrame(root, text="GUGU BERRY", padx=10, pady=20)
frame.pack(padx=30, pady=40)

b1 = Button(frame, text="Touch me")
b2 = Button(frame, text="... or NOT")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()