from tkinter import *
import math


root = Tk()
root.title("Sine curve")

c = Canvas(width=500, height=300, background='white')
c.pack()

axes = c.create_line(50, 150, 450, 150, fill='green')

xy = []
for x in range(400):
    xy.append(50 + x)
    xy.append(150 - math.sin(x/40) * 100)

sinecurve = c.create_line(xy, fill='red')

root.mainloop()