import numpy as np


def dist_sq(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

# x1 = float(input())
# y1 = float(input())
# r1 = float(input())
# x2 = float(input())
# y2 = float(input())
# r2 = float(input())

x1, y1, r1, x2, y2, r2 = [0, 0, 4, 0, 3, 1]

dist = np.sqrt(dist_sq(x1, y1, x2, y2))


if dist < abs(r2 - r1):
    print(False)
elif dist <= (r1 + r2):
    print(True)
else:
    print(False)


