# This tutorial will cover messsage boxes

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message box tutorial')
root.iconbitmap('pictures/coding.ico')

'''
Different modes for messagebox:
showinfo, showwarning, showerror, askquestion, askokcancel, askyesno 
'''

Label1 = Label(root, text="response here")

def popup():
    global response, Label1
    response = messagebox.showinfo("Titlebar", "This is the message")
    if response == "ok":
        Label1.config(text=response)

button1 = Button(root, text="Popup", command=popup)

button1.pack()
Label1.pack()

root.mainloop()