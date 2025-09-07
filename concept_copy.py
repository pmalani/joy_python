import copy
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
    def from_positions(cls, positions):
        return cls({p.security_id: p for p in positions})

    def __len__(self):
        return len(self.security_id_to_position)

    def __iter__(self):
        return iter(self.security_id_to_position.values())

    def __add__(self, other):
        self_copy = copy.deepcopy(self.security_id_to_position)
        for o in other:
            if o.security_id in self_copy:
                p = self_copy[o.security_id]
                p.quantity += o.quantity
            else:
                self_copy[o.security_id] = copy.copy(o)
        return Universe(self_copy)

u1 = Universe.from_positions([Position(x, x * 100) for x in range(1, 4)])
print(u1)
print(len(u1))

for pos in u1:
    print(pos)

u2 = Universe.from_positions([Position(x, x * 100) for x in range(2, 5)])
u3 = u1 + u2
print(u3)
print(u1)
