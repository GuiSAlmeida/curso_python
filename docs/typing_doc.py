"""
Typing - https://docs.python.org/3/library/typing.html
"""
from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


def fn(p1: float, p2: int) -> Union[int, float]:
    return p1 * p2


def greeting(name: str) -> str:
    return 'Hello ' + name


print(fn(2.2, 3))
