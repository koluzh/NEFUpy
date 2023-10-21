for i in range(1000, 10000):
    s = str(i)
    b = False
    for j in range(3):
        for k in range(j + 1, 4):
            if s[j] == s[k]:
                b = True
    if not b:
        print(i)

