import matplotlib.pyplot as plt
import random

n = 1000
count = 0
probs = []

for i in range(1, n + 1):
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    c = random.randint(0, 1)
    if all([a, b, c]):
        count += 1
    probs.append(count/i)

plt.plot(probs)
plt.show()
