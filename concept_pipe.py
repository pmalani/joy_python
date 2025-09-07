t1 = (1, 2, 3)
t2 = (*t1, 4, 5)
print(t2)

l1 = [1, 2, 3]
l2 = [*l1, 4, 5]
print(l2)

l3 = [*t1, 4, 5]
print(l3)

s1 = {*t1, 1, 5}
print(s1)

d1 = { 'homer': 40, 'marge': 37 }
d2 = { 'homer': 47, 'bart': 11 }
d3 = {**d1, **d2, 'lisa': 8}
print(d3)

def add_3(a, b, c):
    return a + b + c

print('tuple', add_3(*t1))
print('list', add_3(*l1))

d4 = {'a': 1, 'b': 2, 'c': 3}
print('dict', add_3(**d4))
