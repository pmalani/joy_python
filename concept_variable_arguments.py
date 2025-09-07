from dataclasses import dataclass
from typing import Dict

@dataclass
class Position:
    security_id : int
    quantity : float

@dataclass
class Universe:
    security_id_to_position : Dict[int, Position]

    @classmethod
    def from_positions(cls, *positions):
        return cls({p.security_id: p for p in positions})

p1 = Position(1, 100)
p2 = Position(2, 200)
p3 = Position(3, 300)

u1 = Universe.from_positions(p1, p2, p3)
print(u1)

u2 = Universe.from_positions(*[Position(x, x * 100) for x in range(2, 5)])
print(u2)

