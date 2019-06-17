from tkinter import *


# draw flag 
def flag(flagcanvas):
    flagcanvas.create_rectangle(40, 40, 100, 100, fill="red", outline="red")
    flagcanvas.create_rectangle(100, 40, 120, 100, fill="white", outline="white")
    flagcanvas.create_rectangle(120, 40, 210, 100, fill="red", outline="red")
    flagcanvas.create_rectangle(40, 100, 210, 120, fill="white", outline="white")
    flagcanvas.create_rectangle(40, 120, 100, 180, fill="red", outline="red")
    flagcanvas.create_rectangle(100, 120, 120, 180, fill="white", outline="white")
    flagcanvas.create_rectangle(120, 120, 210, 180, fill="red", outline="red")


# draw a chessboard
def chess(chesscanvas):
    x = 40
    y = 200
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 1:
                chesscanvas.create_rectangle(x+j*21.2, y+i*21.2, 21.2+x+j*21.2, 21.2+y+i*21.2, fill="black", outline="black")
            else:
                chesscanvas.create_rectangle(x+j*21.2, y+i*21.2, 21.2+x+j*21.2, 21.2+y+i*21.2, fill="white", outline="white")


def closeclick(event):
    tk.destroy()


def mouseclick(self, param):
    mycanvas.delete(param)
    chess(mycanvas)
    mycanvas.create_text(125, 380, font=("Arial", 12), text="Click in the window to close it")
    mycanvas.bind('<Button-1>', closeclick)


tk = Tk()  # Object

tk.title("Mouse experiments")

mycanvas = Canvas(tk, width=340, height=420, background="lightblue")
mycanvas.bind('<Button-1>', lambda event: mouseclick(event, param=temporarytext))

mycanvas.pack()

temporarytext = mycanvas.create_text(170, 200, font=("Arial", 12), text="Click in the window to make a chessboard")

flag(mycanvas)


tk.mainloop()