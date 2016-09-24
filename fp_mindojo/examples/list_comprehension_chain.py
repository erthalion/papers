def apply(v, f):
    return f(v)

def fchain( *args):
    first = args[0]
    args = (lambda v: first(*v), ) + args[1:]
    return reduce(apply, args[:-1], args[-1])
