from maybe import Nothing, Just

def test_function(a, b):
    """ a & b may be None
    """
    a2 = a * a
    b2 = a2 * b

    return (a2, b2)

test_function(1, 2)         # ok
test_function(None, 2)      # exception
test_function(Nothing, 2)   # ok
