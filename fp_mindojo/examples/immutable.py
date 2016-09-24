from collections import namedtuple

Record = namedtuple("Record", "id name value")
r = Record(1, "first record", "record value")
r.name = "second record"    # error

fset = frozenset([1, 2, 1, 3])
fset.add(1)     # no such function
