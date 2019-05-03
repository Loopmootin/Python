import random

# 11.1
# sqrt by binary search


def findsqrt(x):
    max = x + 1
    min = 0
    while max - min > 0.000001:
        mid = (max + min) / 2
        if mid * mid > x:
            max = mid
        else:
            min = mid
    return mid


print("sqrt of 0.81 = %.5f" % findsqrt(0.81))
print("sqrt of 2 = %.5f" % findsqrt(2))
print("sqrt of 3 = %.5f" % findsqrt(3))
print("sqrt of 4 = %.5f" % findsqrt(4))
print("sqrt of 5 = %.5f" % findsqrt(5))
print("sqrt of 2.25 = %.5f" % findsqrt(2.25))
print()


# 11.2
# Dutch national flag
# n buckets inline sorted with n peeks with color and n swaps

def colour(x):
    global buckets
    return buckets[x]


def swap(x, y):
    global buckets
    swap = buckets[x]
    buckets[x] = buckets[y]
    buckets[y] = swap


buckets = []
n = 10
for i in range(0, n):
    r = random.randint(1, 3)
    if r == 1:
        buckets.append("red")
    elif r == 2:
        buckets.append("white")
    else:
        buckets.append("blue")
print("Unsorted " + str(len(buckets)) + " buckets : ")
print(buckets)
print()

firstwhite = -1
beforeblue = n - 1
pointer = 0
while pointer <= beforeblue:
    if colour(pointer) == "blue":
        swap(pointer, beforeblue)
        beforeblue -= 1
    elif colour(pointer) == "white":
        if firstwhite == -1:
            firstwhite = pointer
        pointer += 1
    else:
        if firstwhite != -1:
            swap(pointer, firstwhite)
            firstwhite += 1
        pointer += 1

print("Sorted " + str(len(buckets)) + " buckets : ")
print(buckets)
print()
