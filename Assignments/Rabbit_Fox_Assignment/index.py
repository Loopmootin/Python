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

steadyRabbit = []
steadyFox = []

for x in range(400):
    resultRabbit = rabbit * (1.0 + a - b * rabbit - c * fox)
    resultFox = fox * (1 - d + e * rabbit - f * fox)

    # print("Rabbit", int(resultRabbit))
    # print("Fox", int(resultFox))

    rabbit = resultRabbit
    fox = resultFox

    xyRabbit.append(50 + int(x))
    xyRabbit.append(-95 + int(resultRabbit))

    steadyRabbit.append(int(resultRabbit))

    xyFox.append(50 + int(x))
    xyFox.append(90 + int(resultFox))

    steadyFox.append(int(resultFox))

print()

print("Rabbit list", xyRabbit)
print("Fox list", xyFox)

avgRabbit = sum(steadyRabbit)/len(steadyRabbit)
avgFox = sum(steadyFox)/len(steadyFox)

c = Canvas(width=600, height=800, background='white')
c.pack()

c.create_text(150, 335, font=("Arial", 12), text="Blue graph is rabbit", fill='blue')
c.create_text(150, 35, font=("Arial", 12), text="Red graph is fox", fill='red')

c.create_text(150, 650, font=("Arial", 12), text="Average foxes : " + str(avgFox), fill='red')
c.create_text(150, 700, font=("Arial", 12), text="Average rabbits : " + str(avgRabbit), fill='blue')

axes1 = c.create_line(50, 400, 500, 400, fill='green')
axes2 = c.create_line(50, 100, 500, 100, fill='green')

rabbitCurve = c.create_line(xyRabbit, fill='blue')
foxCurve = c.create_line(xyFox, fill='red')

root.mainloop()