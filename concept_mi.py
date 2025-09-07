
class Person(object):
    def __init__(self, name):
        self.name = name

class Buyer(Person):
    def __init__(self, name):
        super().__init__(name)

    def buy(self):
        print(f'{self.name} is buying...')

class Seller(Person):
    def __init__(self, name):
        super().__init__(name)

    def sell(self):
        print(f'{self.name} is selling...')

class Broker(Buyer, Seller):
    def __init__(self, name):
        super().__init__(name)

bart = Broker("Bart")
print(bart.name)
# mro = method resolution order
print(Broker.__mro__)
bart.buy()
bart.sell()

class Component(object):
    def __init__(self, x_coordinate):
        self.x_coordinate = x_coordinate

class Border(Component):
    def __init__(self, x_coordinate):
        super().__init__(x_coordinate)

class Button(Component):
    def __init__(self, x_coordinate):
        super().__init__(x_coordinate)

# non-virtual, not possible
# e.g. BorderedButton(Border, Button)

class House(object):
    def address(self):
        print("getting house address")
        return 1

class Boat(object):
    def address(self):
        print("getting boat address")
        return 2

class HouseBoat(House, Boat):
    pass

class BoatHouse(Boat, House):
    pass

hb = HouseBoat()
print("house boat", hb.address())

bh = BoatHouse()
print("boat house", bh.address())

class HouseBoat2(House, Boat):
    def address(self):
        return Boat.address(self)

hb2 = HouseBoat2()
print("house boat 2", hb2.address())
