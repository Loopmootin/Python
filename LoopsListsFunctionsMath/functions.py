import math

# Hello


def hello(name):
    n = len(name)
    print("-" * (n + 8))
    print("Hello", name, "!")
    print("-" * (n + 8))


hello("Hugo")
print()


# Function and main


def bottlevolume(height, diameter):
    volume = height * math.pi * diameter**2 / 4
    return volume


def main():
    first = bottlevolume(1, 2)
    second = bottlevolume(math.pi, 4)
    print("Volume of first bottle", first)
    print("Volume of second bottle", second)
    print()


main()
