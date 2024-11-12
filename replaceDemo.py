from typing import NamedTuple
from dataclasses import dataclass
from copy import replace, copy

@dataclass(frozen=True) # This is immutable
class Item:
    name: str
    cost: float
    
cup: Item = Item("Cup", 10)
goldenCup: Item = copy(cup)
# diamondCup: Item = copy(cup, name="diamondCup") if you uncomment this line it will give you an error copy method cannot take any other arguments.

print(cup)
print(goldenCup)

print(id(cup))
print(id(goldenCup))

# Two different ID's via copy

pen: Item = Item("Pen", 10)
goldenPen: Item = replace(pen, cost=100)
diamondPen: Item = replace(pen, name="diamondPen", cost=1000)

print(pen)
print(goldenPen)
print(diamondPen)

print(id(pen))
print(id(goldenPen))
print(id(diamondPen))

# Two different ID's via replace but i can change it's properties even this class is immutable


