def get_dig(x: int):
    digs = list()
    while x > 0:
        temp_dig = x % 10
        digs.append(temp_dig)
        x = x // 10
    return digs


def get_num(x: list[int]):
    num = 0
    for i in range(len(x)):
        num = num + x[i] * pow(10, i)

    return num


def do_funny(x: list[int]):
    x.sort()
    a = x.copy()
    x.sort(reverse=True)
    b = x.copy()
    a_num = get_num(a)
    b_num = get_num(b)
    if a_num > b_num:
        b_num, a_num = a_num, b_num
    res = b_num - a_num
    return res


if __name__ == '__main__':
    n = int(input())
    k = 0

    while True:
        dig_list = get_dig(n)
        new_n = do_funny(dig_list)
        if new_n == n:
            break
        n = new_n
        k = k + 1

    print(n, k)
