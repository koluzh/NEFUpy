from sympy import *
import matplotlib
init_printing()

x = symbols('x')
f = x / ln(1 + x)
a = 0
b = 1
n = 6
h = (b - a) / n

nums = []
for i in range(n + 1):
    nums.append(a + (b - a) / n * i)
pprint(nums)


'''simpson'''
sum = 0
sum1 = 0
sum2 = 0

for i in range(1, n):
    if i % 2 == 0:
        temp = f.subs(x, nums[i])
        sum1 += temp
        pprint(temp)
        temp *= 2
    else:
        temp = f.subs(x, nums[i])
        pprint(temp)
        sum2 += temp
        temp *= 4
    sum += temp

sum += 0 + f.subs(x, nums[n])
pprint(f.subs(x, nums[n]))
sum *= h / 3
pprint('final expression: ')
print('2: ')
pprint(sum1)
print('4: ')
pprint(sum2)
pprint(sum)
pprint('value: ')
pprint(sum.evalf())

I = integrate(f, (x, a, b))
print('Integral: ')
pprint(I.evalf())

'''delta'''
der4 = f
for i in range(4):
    der4 = diff(der4)
print('4th derivative: ')
print(der4)
try:
    maxi = maximum(der4, x)
    print('sup: ')
    print(maxi.evalf())
    delta = (a - b) / 180 * (h ** 4) * maxi
    print('delta: ')
    print(delta.evalf())
except:
    a = 0.01
    pprint(der4.subs(x, a))
    pprint(der4.subs(x, a).evalf())
    print('keke')
    pprint(der4.subs(x, b))
    pprint(der4.subs(x, b).evalf())