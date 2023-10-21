from math import *


def is_triplet(a, b):
    c = a ** 2 + b ** 2
    c = int(sqrt(c))
    if c * c == b * b + a * a:
        return [True, c]
    return [False]


for i in range(1, 1000):
    for j in range(1, 1000):
        if is_triplet(i, j)[0]:
            c = is_triplet(i, j)[1]
            if i + j + c == 1000:
                print(i, j, c)