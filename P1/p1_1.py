import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = list()

for i in range(-100, 100):
    t = a * i ** 3 + b * i ** 2 + c * i + d
    if t == 0:
        x.append(i)

print(x)
