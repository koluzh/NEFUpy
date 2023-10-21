import numpy as np


def solve_quadric(a: float, b: float, c: float):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    d_r = np.sqrt(d)
    x1 = (-b + d_r) / 2 / a
    x2 = (-b - d_r) / 2 / a
    return x1, x2


if __name__ == '__main__':
    x = int(input())

    x1, x2 = solve_quadric(1, 1, -2 * x)

    n = max(x1, x2)
    n = int(n)
    res = x - int(n * (n + 1) / 2)
    print(res)
