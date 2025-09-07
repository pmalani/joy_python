from typing import Optional

from pymonad.maybe import Nothing, Just, Maybe
from pymonad.tools import curry

def div1(a, b):
    return a / b
print(div1(10, 2))
# print(div1(10, 0))

def div2(a, b, default_value = 0):
    return default_value if b == 0 else a / b
print(div2(10, 2))
print(div2(10, 0))
print(div2(10, 0, None))

@curry(2)
def div3(b, a):
    return Nothing if b == 0 else Just(a / b)
identity = lambda x: x
print(div3(2, 10).maybe(None, identity))
print(div3(0, 10).maybe(None, identity))
print(Maybe.insert(10).then(div3(2)).maybe(None, identity))
print(Maybe.insert(10).then(div3(0)).maybe(None, identity))

def div4(a: int | float, b: int | float) -> Optional[int | float]:
    return None if b == 0 else a / b
print(div4(10, 2))
print(div4(10, 0))
