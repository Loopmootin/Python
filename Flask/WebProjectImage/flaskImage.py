# Use PIL; Python Image Library
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import os
import math

# Tk frame
root = Tk()
root.title("Sine curve")

# Canvas
c = Canvas(width=500, height=300, bg='white')
c.pack()  # .. packs the canvas to see what we are doing

# Text
mytext = "Graph of sin(x)"
c.create_text(50, 30, anchor=NW, text=mytext)

# Lines
axes = c.create_line(50, 150, 450, 150, fill='green')

# List
xy = []
for x in range(400):
    xy.append(50 + x)
    xy.append(150 - math.sin(x/40) * 100)

sinecurver = c.create_line(xy, fill='red')


# Some color constrants for PIP
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# myimage is not visible
myimage = Image.new("RGB", (500, 300), white)
# sort of handle
draw = ImageDraw.Draw(myimage)

myfont = ImageFont.truetype("arial.ttf", 15)
draw.text((50, 20), mytext, font=myfont, fill=black)
draw.line([50, 150, 450, 150], green)
draw.line(xy, red)


# save as .jpg or .gif or .bmp or .png
myfilepath = os.path.join('static', 'images', 'mydrawing.jpg')
myimage.save(myfilepath)


# like double click on the file
os.startfile(myfilepath)

root.mainloop()