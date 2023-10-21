from p1_3 import get_dig

n = 9999


def get_keke(x: int):
    i_l = 0
    v = 0
    i_r = 0
    if x == 4 or x == 9:
        i_l = 1
    if 9 > x > 3:
        v = 1
    i_r = x % 5
    i_r = i_r % 4
    x_r = 0
    if x >= 9:
        x_r = 1
    return i_l, v, i_r, x_r

n_digs = get_dig(n)

I_S = ('I', 'X', 'C', 'M', 'X')
V_S = ('V', 'L', 'D', 'V')

res = ''

for i in range(len(n_digs)):
    i_l, v, i_r, x = get_keke(n_digs[i])
    t_s = i_l * I_S[i] + v * V_S[i] + i_r * I_S[i] + x * I_S[i+1]
    res = t_s + res
print(res)
