from tkinter import *
import math

root = Tk()
root.title("Plot of tractrix")

mycanvas = Canvas(width=500, height=300, background="white")
mycanvas.create_text(150, 50, anchor=NW, font=("Arial", 24), text="Lazy dog curve")
mycanvas.pack()

xaxes = mycanvas.create_line(50, 250, 450, 250, fill='green')
yaxes = mycanvas.create_line(50, 250, 50, 50, fill='green')

xy = []
for yfor in range(100, 1, -1):
    y = yfor/100
    x = math.log((1 + math.sqrt(1 - y * y)) / y) - math.sqrt(1 - y * y)
    xy.append(50 + x * 100)
    xy.append(250 - y * 100)

dogcurve = mycanvas.create_line(xy, fill='blue')

root.mainloop()