ololo = 'mama'

with open('kek.txt') as f:
    s = f.read()
    words = s.split(' ')
    for w, i in zip(words, range(len(words))):
        if i > 0 and i < len(words) - 1:
            if ololo == words[i - 1] and ololo == words[i + 1]:
                print(w)
                break

