# from : https://www.python-course.eu/recursive_functions.php


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def factorialdetailed(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorialdetailed(n-1)
        print("intermediate result for ", n, " * factorial(", n-1, "): ", res)
        return res	


print()
print(factorial(5))
print()
print(factorialdetailed(5))
