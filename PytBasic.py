# Small Python examples

import math

print("Hello World!")
print()

print("Hello")
print("world!")
print()

print('I say "Hello World!"')
print()

print("A lucky number: ", 3+4, " Unlucky number: ", int("13"))
print()

BOTTLEVOLUME = 0.7  # A constant
bottle = 5
totalvolume = BOTTLEVOLUME * bottle
print("Bottle volume = ", str(BOTTLEVOLUME))
print("Total volume = ", totalvolume)
print()


FIRSTNAME = "Hugo"
LASTNAME = "Smith"

name = FIRSTNAME + " " + LASTNAME

print("Name = ", name, "\nIt starts with ", name[0])
print("Length of name = ", len(name))
print()

print("7 / 4 = ", 7 / 4)
print("7 // 4 = ", 7 // 4)
print("7 % 4 = ", 7 % 4)
print("sqrt(4) = ", math.sqrt(4))
print("sqrt(2) = ", math.sqrt(2))
print("sqrt(2) = %4.2f" % math.sqrt(2))

print()
print("Hej mor")

yourname = input("きみのなまえはなにおですか ")
print("Hello " + yourname)
print()

userinput = input("Enter first number : ")
firstnumber = int(userinput)

userinput = input("Enter second number : ")
secondnumber = int(userinput)

sum = firstnumber + secondnumber
print()

print("%-15s %5d" % ("First number ", firstnumber))
print("%-15s %5d" % ("Second number ", secondnumber))
print("%-15s %5d" % ("Sum ", sum))
print()

print("-" * 30)
print()