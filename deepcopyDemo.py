from typing import Any
from copy import deepcopy

a: list[Any] = [1, 2, ["a", "b"], 4, 5]
aCopy: list[Any] = a.copy() # Shallow Copy

aCopy[2][0] = 999

print(f"Original: {a}")
print(f"Shallow Copy: {aCopy}")

print("########################################")
print("########################################")

a: list[Any] = [1, 2, ["a", "b"], 4, 5]
aDeepCopy: list[Any] = deepcopy(a) # Deep Copy

aDeepCopy[2][0] = 999

print(f"Original: {a}")
print(f"Deep Copy: {aDeepCopy}")