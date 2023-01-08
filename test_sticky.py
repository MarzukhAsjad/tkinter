from tkinter import *
from tkinter import ttk

root = Tk()

root.rowconfigure(0,weight = 1)
root.columnconfigure(0,weight = 1)

frame = ttk.Frame(root)
frame.grid(row = 0,column =0)

ttk.Label(frame,text = 'Label_1',background='red').grid(row=0,column=0,sticky='nwes') # remove sticky='news' to see the difference
ttk.Button(frame,text = 'Button').grid(row=0,column=1,sticky='nwse')
ttk.Label(frame,text = 'Label``_2').grid(row=0,column=2,sticky='nwes')
ttk.Label(frame,text = 'LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG').grid(row=1,column=0)
root.mainloop()