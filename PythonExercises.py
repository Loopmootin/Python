import math

# exercise 1.1

userinput = input("Enter first number : ")
firstnumber = int(userinput)

userinput = input("Enter second number : ")
secondnumber = int(userinput)

sum = firstnumber + secondnumber
print("The sum is: ", sum)

difference = secondnumber - firstnumber
print("The difference is: ", difference)

product = firstnumber * secondnumber
print("The product is: ", product)

average = (firstnumber + secondnumber) / 2
print("The average is: ", average)

distance = abs(firstnumber - secondnumber)
print("The distance is: ", distance)

maximum = max(firstnumber, secondnumber)
print("The maximum is: ", maximum)

minimum = min(firstnumber, secondnumber)
print("The minimum is: ", minimum)


# exercise 1.2

print("%-15s %5d" % ("The sum is: ", sum))

print("%-15s %5d" % ("The difference is: ", difference))

print("%-15s %5d" % ("The product is: ", product))

print("%-15s %5d" % ("The average is: ", average))

print("%-15s %5d" % ("The distance is: ", distance))

print("%-15s %5d" % ("The maximum is: ", maximum))

print("%-15s %5d" % ("The minimum is: ", minimum))

# exercise 1.3

userinput = input("Write a distance in meters: ")

meters = int(userinput)

miles = meters * 0.000621371192
print("The distance in miles: ", miles)

yards = meters * 1.0936133
print("The distance in yards: ", yards)

feet = meters * 3.2808399
print("The distance in feet: ", feet)

inches = meters * 39.3700787
print("The distance in inches: ", inches)

# exercise 1.4

userinput = input("Write an amount: ")
amount = userinput

userinput = input("Write a yearly interest: ")
interest = userinput

for x in range(0, 10):
    fortune = float(amount) * (1 + float(interest)) ** x
    print("Your fortune after ", x, " year(s) is: ", "%.2f" % (fortune))
