import random

# Bubble sort in place.

# Define bubblesort function, that takes a list 'numbers' as argument.


def bubblesort(numbers):
    for i in range(0, len(numbers) - 1):  # Goes through the whole list.
        for j in range(0, len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                swop = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = swop


# Try bubblesort.
# First, print the list that also shows the length of the list (numbers in list).
numbers = [2, 6, 3, 9, 4, 4, 2, 1, 10, 67, 10, 7, 8, 4]
print(str(len(numbers)) + " numbers : ", numbers)
print()

# Second, use the bubblesort function, to sort the list correctly.
bubblesort(numbers)
print(str(len(numbers)) + " numbers : ", numbers)
print()


# Binary search in sorted array


def binarysearch(number, numbers):
    minindex = 0
    maxindex = len(numbers) - 1
    found = False

    while not found and minindex <= maxindex:
        midindex = (minindex + maxindex) // 2
        if numbers[midindex] == number:
            found = True
            answer = midindex
        elif numbers[midindex] > number:
            maxindex = midindex - 1
        else:
            minindex = minindex + 1
    if not found:
        answer = -1
    return answer


# Try binary search
print("Sorted numbers", numbers)

for i in[0, 1, 2, 4, 5, 9, 67, 68]:
    result = binarysearch(i, numbers)
    if result == -1:
        print(str(i) + " not found")
    else:
        print(str(i) + " found at position " + str(result))

print()

# Roll two dice
singlestatistic = [0, 0, 0, 0, 0, 0]
doublestatistic = 0
numberofthrows = 90

for i in range(0, numberofthrows):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    singlestatistic[die1 - 1] += 1
    singlestatistic[die2 - 1] += 1
    if die1 == die2:
        doublestatistic += 1

sumofsingles = 0
for i in range(0, len(singlestatistic)):
    sumofsingles += singlestatistic[i]

print(singlestatistic, "number of rolls", str(sumofsingles))
print(str(doublestatistic), "doubles out of", numberofthrows, "throws")
print()


# Tower of Hanoi recursion; move a pile of n discs from stick i to stick j

def tower(n, i, j):
    global count
    if n == 1:
        count += 1
        print("Move a disc from stick " + str(i) + " to stick " + str(j) + " (move number " + str(count) + ")")
    else:
        tower(n - 1, i, 6 - i - j)
        tower(1, i, j)
        tower(n - 1, 6 - i - j, j)


# Try Tower of Hanoi
count = 0
n = 15
print("Moove Tower of Hanoi with " + str(n) + " discs from stick 1 to stick 3")

tower(n, 1, 3)
print("Finished after " + str(count) + " moves")
