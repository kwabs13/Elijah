#!/usr/bin/python
from Tkinter import *

root = Tk()
root.geometry('600x300')

c = Canvas(root, height = 440, width = 640, bg='black')

sun = c.create_oval(20, 100, 100, 180, fill='yellow')
mer = c.create_oval(110, 120, 145, 160, fill='orange')
ven = c.create_oval(150, 120, 200, 175, fill = 'blue')
earth = c.create_oval(205, 120, 240, 160, fill = 'blue')
mars = c.create_oval(245, 120, 260, 140, fill = 'red')

c.pack()
root.mainloop()
