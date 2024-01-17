# basic fibonacci function
from sys import argv
count = int(argv[1])


# compute the x-th Fibonnacci number
def fib_iter(x):
    assert (x >= 0)  # check for a bad input
    if x == 0:
        return 0
    elif x == 1:
        return 1

    fib_minus_1 = 1
    fib_minus_2 = 0

    for i in range(2, x):
        temp = fib_minus_1
        fib_minus_1 = fib_minus_1 + fib_minus_2
        fib_minus_2 = temp

    return fib_minus_1+fib_minus_2


retval = fib_iter(count)
print(f"fib % 2 is {retval % 2}")
