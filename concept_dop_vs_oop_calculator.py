import math
from dataclasses import dataclass
from functools import singledispatch

@dataclass
class Circle:
    radius: float

@dataclass
class Square:
    side: float

# traditional with isinstance checks
def perimeter2(shape_obj):
    if isinstance(shape_obj, Circle):
        return 2 * math.pi * shape_obj.radius
    elif isinstance(shape_obj, Square):
        return 4 * shape_obj.side
    else:
        raise ValueError("Unknown shape")

shapes = [Circle(5), Square(10)]
for shape in shapes:
    print(perimeter2(shape))

# with pattern matching and destructuring
def perimeter1(shape_obj):
    match shape_obj:
        case Circle(radius=r):
            return 2 * math.pi * r
        case Square(side=s):
            return 4 * s
        case _:
            raise ValueError("Unknown shape")

for shape in shapes:
    print(perimeter1(shape))

# with single dispatch
@singledispatch
def perimeter3(shape_obj):
    raise ValueError("Unknown shape")
@perimeter3.register
def _(shape_obj: Circle):
    return 2 * math.pi * shape_obj.radius
@perimeter3.register
def _(shape_obj: Square):
    return 4 * shape_obj.side

for shape in shapes:
    print(perimeter3(shape))
