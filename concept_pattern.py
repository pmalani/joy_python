from dataclasses import dataclass
from enum import Enum

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

color = Color.RED

match color:
    case Color.RED:
        print("go red")
    case _:
        print("go other")

colorStr = "BLUE"

match colorStr:
    case "red" | "RED":
        print("go red")
    case "blue" | "BLUE":
        print("go blue")
    case _:
        print("go other")

@dataclass
class Point:
    x: int
    y: int

def match_point(a_point: Point):
    match a_point:
        case Point(0, 0):
            print("at origin")
        case Point(a, b) if a == b:
            print("x and y are the same")
        case Point(a, b):
            print(f"x: {a}, y: {b}")

r = Point(0, 0)
match_point(r)

p = Point(3, 3)
match_point(p)

q = Point(1, 2)
match_point(q)

def match_points(ps):
    match ps:
        case []:
            print("no points")
        case [Point(0, 0)]:
            print("only origin")
        case [Point(x1, 0), Point(x2, 0)]:
            print(f"two points on x-axis: {x1}, {x2}")
        case _:
            print("other points")

points1 = []
match_points(points1)
points2 = [Point(5, 0), Point(10, 0)]
match_points(points2)

tuple1 = ("Homer", 47)

match tuple1:
    case (_, age) if age >= 18:
        print("can vote")

dict1 = {"name": "Homer", "age": 50}

match dict1:
    case {"name" : _, "age" : a} if a >= 21:
        print("can drink 🍻")