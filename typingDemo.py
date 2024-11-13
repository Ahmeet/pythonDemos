import typing as t
import collections.abc as c

def sayHello(names: t.Iterable) -> None:
    for name in names:
        print(name)

#sayHello(["Bob", "Luigi"])

#This is deprecated

def sayHelloCurrent(names: c.Iterable) -> None:
    for name in names:
        print(name)

#sayHelloCurrent(["Bob", "Luigi"])

#This is using currently.

#They are exactly the same but typing has been deprecated.


def repeat(func: c.Callable, times: int) -> None:
    for i in range(times):
        func()

def hello() -> None:
    print("Hello")

repeat(hello, times=3)