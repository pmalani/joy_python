tuple1 = ('Homer', 40)
name, age = tuple1
print(name, age)

name, _ = tuple1
print(name)

list1 = [40, 37]
age1, age2 = list1
print(age1, age2)

list2 = [1, 8, 11, 37, 40]
first, *middle, last = list2
print(first, middle, last)
middle.append(100)
print(middle, list2)

for i, e in enumerate(middle):
    print(i, e)

dict1 = {'name': 'Homer', 'age': 41}
name, age = dict1.values()
print(name, age)

class Person(object):
    def __init__(self, name3, age3):
        self.name = name3
        self.age = age3

    # treats like a list for deconstruction
    def __iter__(self):
        yield self.name
        yield self.age

homer = Person('Homer', 42)
name, age = homer
print(name, age)

match homer:
    case Person(name=n, age=a):
        print(f'{n} is {a} years old')
    case _:
        print('not a person')