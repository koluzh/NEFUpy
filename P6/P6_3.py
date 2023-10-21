def get_ascii_sum(w: str):
    return sum([ord(c) for c in w])

res = []

with open('kek.txt', 'r') as f:
    s = f.read()
    words = s.split(' ')
    for w, i in zip(words, range(len(words))):
        if get_ascii_sum(w) % 2 == 1:
            res.append(w)

with open('lol.txt', 'w') as f:
    f.write(' '.join(res))


