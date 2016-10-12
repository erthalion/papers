from fn import recur, F
from fn.curried import curried
from operator import add, mul

# function composition
f = F(add, 1) << F(mul, 100)

# decorator for currying functions
@curried
def sum5(a, b, c, d, e):
    return a + b + c + d + e

# trampoline for tail recursion
@recur.tco
def fact(n, acc=1):
    if n == 0: return False, acc
    return True, (n-1, acc*n)
