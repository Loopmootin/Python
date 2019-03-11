import time
import sys
import math
import random


# time

print(time.asctime())
print()


# sys

def hello():
    print("Yout name: ")
    # name = sys.stdin.readline().strip('\n')
    # print("Hello", name)

hello()
print()


# math

print("sin(30 deg)", math.sin(math.radians(30)))
print("Pythagoras: sides 3 and 4:", math.hypot(3,4))
print("Greatest common devisor for", 7*9*17, "and", 2*17*31, "is", math.gcd(1071, 1054))
print()

# random

print("Random number between 1 and 6:", random.randint(1,6))

numbers = [1, 2, 3, 4, 5, 6]
print("Random number from list:", random.choices(numbers)[0])
print(numbers)
random.shuffle(numbers)
print(numbers)
print()


