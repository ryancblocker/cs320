# basic fibonacci function
from sys import argv
count = int(argv[1])
# compute the x-th Fibonnacci number
def fib(x):
    assert (x >= 0) # check for a bad input
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fib(x-1)+fib(x-2)

print(fib(count))
