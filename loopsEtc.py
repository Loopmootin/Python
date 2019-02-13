# Add numbers

sum = 0
count = 0
done = False

while not done:
    mynumber = int(input("Enter a positive integer or 0 or negative to calculate sum: "))
    if mynumber <= 0:
        done = True
    else:
        sum = sum + mynumber
        count = count + 1
if count == 0:
    average = 0
else:
    average = sum / count

print("Sum of the", count, "numbers =", sum)
print("Average of the", count, "numbers =", average)
print()


# String with while

name = "Hugo"
i = 0

while i < len(name):
    letter = name[i]
    print(letter)
    i = i + 1
print()


# String with for

for myletter in name:
    print(myletter)
print()


# Range

for i in range(1, 11, 2):
    print(i, end='...')
print()
print()


# Nested for

XMAX = 10
NMAX = 4

for n in range(1, NMAX + 1):
    print("%10d" % n, end="")
print()

for n in range(1, NMAX + 1):
    print("%10s" % "x", end="")
print()
print("\n", "      ", "-" * 33)

for x in range(1, XMAX + 1):
    for n in range(1, NMAX + 1):
        print("%10d" % x**n, end="")
    print()
print()

