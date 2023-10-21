import numpy as np
from P9_1 import func, get_eps

def get_max(f: callable, a: float, b: float, dx: float):
    x = a
    maxi = f(x)
    while x < b:
        x += dx
        if f(x) > maxi:
            maxi = f(x)
    return maxi

def monte(f: callable, a: float, b: float, n: int):
    dx = (b - a) / n
    h = get_max(f, a, b, dx)
    x_r = np.random.uniform(a, b, n)
    y_r = np.random.uniform(0, h, n)
    count = 0
    for x, y in zip(x_r, y_r):
        if y <= f(x):
            print(x, y)
            count += 1
    s_box = h * (b - a)
    s = s_box * count / n
    eps = get_eps(f, a, b, s)
    return s, eps


print(monte(func, 0, 4, 1000000))

