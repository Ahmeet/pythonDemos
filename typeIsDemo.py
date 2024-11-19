from typing import TypeIs, TypeGuard, assert_type

def isString(obj: object) -> TypeIs[str]:
    return isinstance(obj, str)

def check(obj: str | int) -> None:
    if isString(obj):
        assert_type(obj, str)
    else:
        assert_type(obj, int)