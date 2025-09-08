class Person:
    def __init__(self, first_name, last_name):
        self._f_name = first_name
        self._l_name = last_name

    @property
    def full_name(self):
        return f'{self._f_name} {self._l_name}'

    @full_name.setter
    def full_name(self, name):
        [self._f_name, self._l_name] = name.split(' ')


p1 = Person("Homer", "Simpson")
print(p1.full_name)

p1.full_name = "Lisa Simpson"
print(p1.full_name)