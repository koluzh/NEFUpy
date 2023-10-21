import random


class MyClass:
    def __init__(self, d: dict):
        for name, arg in d.items():
            self.__setattr__(name, arg)

def factory():
    class A(MyClass):
        pass
    return A


def kek(l: list, s: str):
    A = factory()
    A.__qualname__ = s
    A.__name__ = s
    d = dict()
    for i in l:
        if isinstance(i, str):
            d[i] = random.randint(0, 100)
    o = A(d)
    return o

o = kek([1, '1', 'kek', [], 1.2], 'refoerkfo')
print(type(o))
print(o.__dict__)