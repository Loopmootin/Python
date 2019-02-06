# unlucky floor

floor = int(input("Elevator button pressed : "))

if floor > 13:
    actualfloor = floor - 1
else:
    actualfloor = floor

if floor == 13:
    print("Elevator will explode and you will die")
else:
    print("Elevator moves to actual floor: ", actualfloor)

# earthquake

richter = float(input("Magnitude on Richter scale: "))

if richter >= 8:
    print("Most structures will be destroyed")
elif richter >= 7:
    print("Many buildings will be destroyed")
elif richter >= 6:
    print("Many buildings will be considerably damaged")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")
