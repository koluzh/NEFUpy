from sympy import *

x = symbols('x')

f = sqrt((1 + 3*(sin(x)) ** 2)/cos(x))
print(f)

I = integrate(f)

print(I)