from tkinter import *
import math

root = Tk()
root.title("Population curve")

rabbit = 500.0
fox = 10.0

a = 0.1
b = 0.00002
c = 0.01
d = 0.01
e = 0.00002
f = 0.0001

xyRabbit = []
xyFox = []

for x in range(400):
    resultRabbit = rabbit * (1.0 + a - b * rabbit - c * fox)
    resultFox = fox * (1 - d + e * rabbit - f * fox)

    # print("Rabbit", int(resultRabbit))
    # print("Fox", int(resultFox))

    rabbit = resultRabbit
    fox = resultFox

    xyRabbit.append(50 + int(x))
    xyRabbit.append(55 + int(resultRabbit))

    xyFox.append(50 + int(x))
    xyFox.append(540 + int(resultFox))

    # time = time + 1
print()

print("Rabbit list", xyRabbit)
print("Fox list", xyFox)

c = Canvas(width=600, height=1000, background='white')
c.pack()

xaxes = c.create_line(50, 550, 500, 550, fill='green')
# yaxes = c.create_line(50, 50, 50, 600, fill='green')

rabbitCurve = c.create_line(xyRabbit, fill='blue')
foxCurve = c.create_line(xyFox, fill='red')

root.mainloop()