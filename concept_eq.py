from dataclasses import dataclass

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return TypeError
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(0, 0)

print(f"p1 is p2: {p1 is p2}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")

@dataclass
class AnotherPoint:
    x: int
    y: int

p1 = AnotherPoint(1, 2)
p2 = AnotherPoint(1, 2)
p3 = AnotherPoint(0, 0)

print(f"p1 is p2: {p1 is p2}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
