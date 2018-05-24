#!/usr/bin/python
from Tkinter import *

root = Tk()
root.geometry('600x300')

c = Canvas(root, height = 440, width = 640, bg='white')

sun = c.create_oval(20, 100, 100, 180, fill='yellow')
sun_1 = c.create_text(60, 185, fill="black",text="sun")

mer = c.create_oval(110, 120, 145, 160, fill='orange')
mer_1 = c.create_text(130, 170, fill = 'black', text = 'Mercury')
                      
ven = c.create_oval(150, 120, 200, 175, fill = 'SkyBlue1')
ven_1 = c.create_text(175, 180, fill = 'black', text = 'Venus')

earth = c.create_oval(205, 120, 240, 160, fill = 'blue')
earth_1 = c.create_text(222, 165, fill = 'black', text = 'Earth')

mars = c.create_oval(245, 150, 265, 130, fill = 'red')
mars_1 = c.create_text(255, 155, fill = 'black', text = 'Mars')

jup = c.create_oval(270, 110, 330, 175, fill = 'brown4')
jup_1 = c.create_text(300, 183, text = 'Jupiter')

sat = c.create_oval(335, 110, 400, 175, fill = 'antique white')
sa_1 = c.create_text(365, 183, text = 'Saturn')
    
ura = c.create_oval(405, 120, 450, 165, fill = 'deep sky blue')
ura_1 = c.create_text(425,170, text = 'Uranus')
                      
nep = c.create_oval(455, 125, 490, 160, fill = 'light slate gray')
nep_1 = c.create_text(475, 165, text = 'Neptune')

plu = c.create_oval(500, 155, 518, 137, fill = 'SpringGreen4')
plu_1 = c.create_text(509, 158, text = 'Pluto')

c.pack()
root.mainloop()
