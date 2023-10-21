coords = list()
angles = list()

with open('p3.in', 'r') as f:
    s = f.readline()
    x, y = s.split(' ')
    x = float(x)
    y = float(y)
    coords.append([x, y])

for c in coords:
    x = c[0]
    y = c[1]
    k = y/x
    angles.append(k)

n = len(angles)
k = n

for i in range(n - 1):
    for j in range(i + 1, n):
        if angles[i] == angles[j]:
            k -= 1

print(k)
