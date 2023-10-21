import numpy as np

import scipy.integrate as si


def func(x: float) -> float:
    return 3 * x ** 2 + 4 * x + 2


def integrate(f: callable, start: float, end: float, dx: float, option: str = 'mid') -> float:
    sum = 0
    r = np.arange(start, end, dx)
    for i in r:
        if option == 'left':
            x = i
        elif option == 'right':
            x = i + dx
            if x > end:
                break
        elif option == 'mid' or option == 'trap':
            x = i + dx / 2
            if x > end:
                break
        else:
            raise Exception('invalid option')
        try:
            sum += f(x) * dx
        except:
            raise Exception('разрыв в точке ', x)
    return sum


def get_eps(func, start, end, result):
    exact = si.quad(func, start, end)[0]
    eps_abs = abs(result - exact)
    eps_rel = eps_abs / exact
    return eps_abs, eps_rel


if __name__ == '__main__':
    s = integrate(func, 0, 4, 0.1, 'mid')

    exact = si.quad(func, 0, 4)
    exact = exact[0]

    eps_abs = abs(s - exact)
    eps_rel = eps_abs / exact

    print('result: ', s)
    print('exact: ', exact)
    print('eps_abs: ', eps_abs)
    print('eps_rel: ', eps_rel)
