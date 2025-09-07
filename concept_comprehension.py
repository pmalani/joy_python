# list
import itertools

list1 = [x for x in range(10)]
print(list1)

# or
list3 = list(range(10))
print(list3)

# conditional
list2 = [x for x in range(10) if x % 2 == 0]
print(list2)

# set
set1 = {x for x in range(10)}
print(set1)

# dictionary
dict1 = { x : x*x for x in range(10)}
print(dict1)

word_count = {key: len(list(values)) for key, values in itertools.groupby(sorted("a b c a".split(' ')))}
print(word_count)

# tuple
tuple1 = tuple(range(10))
print(tuple1)
