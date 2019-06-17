from tkinter import *

# function
def echo():
    mylabel['text'] = textentry.get()
    button1.config(state=DISABLED)
    button2.config(state=NORMAL)


def getReady():
    button1.config(state=NORMAL)
    button2.config(state=DISABLED)


tk = Tk()  # Object

tk.title("Canvas with buttons")

mycanvas = Canvas(tk, width=240, height=100, background="lightblue")

# input field
textentry = Entry(mycanvas)
mycanvas.create_window(20, 60, anchor=NW, window=textentry, height=20, width=80)

# button
button1 = Button(mycanvas, text="Echo input", command=echo)
mycanvas.create_window(20, 20, anchor=NW, window=button1)

button2 = Button(mycanvas, text="Enable echo button", command=getReady)
button2.config(state=DISABLED)
mycanvas.create_window(120, 20, anchor=NW, window=button2)

# label
mylabel = Label(mycanvas, text="Echo", anchor='w')
mycanvas.create_window(120, 60, anchor=NW, window=mylabel, height=20, width=80)

mycanvas.pack()
tk.mainloop()
