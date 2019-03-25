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

    xyRabbit.append(50 + x)
    xyRabbit.append(-95 + resultRabbit)

    xyFox.append(50 + x)
    xyFox.append(90 + resultFox * 35)

print()

print("Rabbit list", xyRabbit)
print("Fox list", xyFox)

steadyRabbit = str(int(xyRabbit[-1]))
steadyFox = str(int(xyFox[-1] / 35))

print(steadyRabbit)
print(steadyFox)


c = Canvas(width=600, height=800, background='white')
c.pack()

c.create_text(150, 280, font=("Arial", 12), text="Blue graph is rabbit", fill='blue')
c.create_text(150, 300, font=("Arial", 12), text="Red graph is fox", fill='red')

c.create_text(150, 35, font=("Arial", 12), text="Rabbit steady value : " + steadyRabbit, fill='blue')
c.create_text(150, 55, font=("Arial", 12), text="Fox steady value : " + steadyFox, fill='red')

axes1 = c.create_line(50, 400, 500, 400, fill='green')

rabbitCurve = c.create_line(xyRabbit, fill='blue')
foxCurve = c.create_line(xyFox, fill='red')

root.mainloop()