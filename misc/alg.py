from sympy import *

x, y, z = symbols('x,y,z')

# f = [-1, -1, -2, -1, 1]
# g = [0, -1, -3, 3]

f = x ** 4 - x ** 3 + 2 * x ** 2 - x - 1
g = x ** 4 - 2 * x ** 2 + 1
l = (x + 1) ** 2 * (x - 1)

d = gcd(f,g)
d = poly(l)

print(d)
