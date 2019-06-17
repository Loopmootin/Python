from random import random


# Imperative, non functional : Statements change the programs state
print("New race - imperative\n")
time = 0
carpositions = [1, 1, 1]

while time < 5:
    print("Time = ", time)
    for i in range(len(carpositions)):
        # draw car
        print('#' * carpositions[i])
        # move car
        if random() > 0.3:
            carpositions[i] += 1
    time += 1
    print()

print()


# Declarative : Logic without control flow
# Functional : Declarative style that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data

def movecars(carpositions):
    return list(map(lambda x: x + 1 if random() > 0.3 else x, carpositions))


def outputcar(position):
    return '¤' * position


def runstepofrace(state):
    return {'time': state['time'] + 1, 'carpositions': movecars(state['carpositions'])}


def draw(state):
    print("Time = ", str(state['time']))
    print('\n'.join(map(outputcar, state['carpositions'])))
    print()


def race(state):
    draw(state)
    if state['time'] < 4:
        race(runstepofrace(state))


print("New race - functional\n")
# state is a dictionary, time is an int, car_positions is a list (of ints)
race({'time': 0, 'carpositions': [1, 1, 1]})
