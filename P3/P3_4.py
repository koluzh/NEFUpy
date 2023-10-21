def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def fits(n: int):
    for d in range(2, 11):
        if n % d != 0:
            return False
    return True


d = 1
for i in range(2, 21):
    d = lcm(d, i)


if fits(d):
    print(d)
