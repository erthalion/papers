from pymonad.Maybe import Just, Nothing
from pymonad.List import List

def add(x, y):
    return x + y

add << Just(7) & Just(8)                    # returns Just(15)
add << Nothing & Just(8)                    # returns Nothing
add << Just(7) & Nothing                    # returns Nothing
add << List(1, 2, 3) & List(4, 5, 6)        # returns List(5, 6, 7, 6, 7, 8, 7, 8, 9)
