import math
import random

# Math examples
print("Sin(30) =", math.sin(math.radians(30)))
print("Pythagoras : with sides 3 and 4 : ", math.hypot(3, 4))
print("Greatest common divisor for ", 7 * 9 * 17, "and", 2 * 17 * 31, "is", math.gcd(1071, 1054))

print("A random number between 1 and 6:", random.randint(1, 6))
print()

numbers = [1, 2, 3, 4, 5, 6]
print("A random number between 1 and 6:", random.choices(numbers)[0])
print()

print(numbers)
random.shuffle(numbers)
print(numbers)
print()