import functools

numbers = [1, 2, 3, 4]
dogs = ["Fido", "Pluto", "Lady"]


# Non functional (how to do)
total = 0
for number in numbers:
    total += number
print(total)

# Functional (what you want)
print(sum(numbers))

# Functional without the readymade sum
print(functools.reduce(lambda mysum, x: mysum + x, numbers))
print()


# Non functional
def showfirstnon():
    global numbers
    return numbers[0]


print(showfirstnon())


# Functional
def showfirst(list):
    return list[0]


print(showfirst(numbers))
print()


# (Non functional) with local variable that are changed
def mysumnon(list):
    total = 0
    for number in list:
        total += number
    return total


print(mysumnon(numbers))


# Functional, no variable - recursion
def mysum(list):
    if not list:
        return 0
    else:
        return list[0] + mysum(list[1:])


print(mysum(numbers))
print()


# Non functional, multiply nubers by 2 in new list
def doublenon(list):
    newnumbers = []
    for number in list:
        newnumbers.append(number * 2)
    return newnumbers


print(doublenon(numbers))


# Functional
def double1(number):
    return number * 2


print(list(map(double1, numbers)))


doublelambda = lambda number: number * 2
print(list(map(doublelambda, numbers)))

print(list(map(lambda number: number * 2, numbers)))
print()


# Non functional fibonacci
def fibonaccinon(n, first=1, second=1):
    mylist = []
    for i in range(n):
        mylist.append(first)
        first, second = second, first + second
    return mylist


print(fibonaccinon(10))


# Non functional with generator (one time list)
def fibonaccigen(n, first=1, second=1):
    for i in range(n):
        yield(first)
        first, second = second, first + second


print(list(fibonaccigen(10)))


# Non functional, bad recursive
def fibonaccirec(n):
    if n <= 2:
        return 1
    else:
        return fibonaccirec(n-1) + fibonaccirec(n-2)


mylist = []

for i in range(1, 11):
    mylist.append(fibonaccirec(i))
print(mylist)

# Functional, good recursive
fibonacci = (lambda n, first=1, second=1:
             [] if n == 0 else
             [first] + fibonacci(n-1, second, first + second))

print(fibonacci(10))
print()


# Non functional list iteration
bigdognon = []

for dog in dogs:
    bigdognon.append("Big {}".format(dog))
print(bigdognon)


# Functional using coprehension ("understanding" - create a list from iterable)
print(["Big {}".format(dog) for dog in dogs])
print()


# Fist class function (delegate in C#) - function as a parameter (or return, variable)
def myname(name):
    print(name)


mynewname = myname
myname("Hugo")
mynewname("Hugo")
print()


# Higher order function (close connected to first class functions (and delegates i C#)
def myconvert(to, number):
    return to(number)


print("Number = " + myconvert(str, 10.123))
print("Number = " + myconvert(str, myconvert(int, 10.123)))
print()


# Filter dog with an o
print(list(filter(lambda x: 'o' in x, dogs)))
print()
