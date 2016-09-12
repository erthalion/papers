from pyrsistent import m, pmap, v

# No mutation of maps once created, instead they are
# "evolved" leaving the original untouched
m1 = m(a=1, b=2)
m2 = m1.set('c', 3)
m3 = m2.set('a', 5)
