import random


class Mee:
    def __init__(self, n: int):
        self.num = n


def func(n: int):
    res = []
    for i in range(n):
        temp = Mee(random.randint(0, n) * 2 + 1)
        res.append(temp)
    return res


l = func(5)
for i in l:
    print(i.num)