# basic fibonacci function
from sys import argv
count = int(argv[1])

def fib_help(x):
    if x == 1:
        return 1, 0
    fib_minus_1, fib_minus_2 = fib_help(x-1)
    return fib_minus_1+fib_minus_2, fib_minus_1

def fib1(x):
    assert (x >= 0)
    if x == 0:
        return 0
    elif x == 1:
        return 1
    fib_minus_1, fib_minus_2 = fib_help(x-1)
    return fib_minus_1+fib_minus_2

print(fib1(count))
