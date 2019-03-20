from tkinter import *
import math

root = Tk()
root.title("Population curve")

c = Canvas(width=500, height=300, background='white')
c.pack()

axes = c.create_line(50, 150, 450, 150, fill='green')

rabbit = 500.0
fox = 10.0

time = 0.0
endTime = 400.0

a = 0.1
b = 0.00002
c = 0.01
d = 0.01
e = 0.00002
f = 0.0001

resultRabbit = rabbit * time * (1.0 + a - b * rabbit * time - c * fox * time)
resultFox = fox * time * (1 - d + e * rabbit * time - f * fox * time)

xyRabbit = []
xyFox = []

while time < endTime:
    resultRabbit = rabbit * time * (1.0 + a - b * rabbit * time - c * fox * time)
    resultFox = fox * time * (1 - d + e * rabbit * time - f * fox * time)

    print("Regn mig ud kanin", resultRabbit)
    print("Regn mig ud røv", resultFox)

    xyRabbit.append(50 + time)
    xyRabbit.append(150 - math.sin(time/40) * 100)

    xyFox.append(50 + time)
    xyFox.append(150 - math.sin(time/40) * 100)

    time = time + 1
print()

# rabbitCurve = c.create_line(xyRabbit, fill='blue')
# foxCurve = c.create_line(xyFox, fill='red')

root.mainloop()