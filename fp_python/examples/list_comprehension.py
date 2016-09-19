# list comprehension in python
[v.attr for v in source if condition(v)]

# function chain in python
list(reversed(list(islice(count(), 5))))

# slightly modified version in python
fchain(list, reversed, list, islice, (count(), 5))
