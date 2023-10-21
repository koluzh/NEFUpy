import numpy as np
import matplotlib.pyplot as plt

def detail():
    return np.random.normal(23, 1.6)

detail_list = []
count = 0
n = 10000

for i in range(n):
    d = detail()
    detail_list.append(d)
    if d <= 24.2 and d >= 22:
        count += 1

print(count / n)
plt.hist(detail_list, bins=20)
plt.show()