import numpy as np
import matplotlib.pyplot as plt

def monte(n: int):
    count = 0
    exact = np.pi
    data = []

    for i in range(n):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
        accuracy = abs(((count / n * 4) - exact)/exact)
        data.append(accuracy)

    plt.plot(data)
    plt.show()
    return count

m_res = monte(1000) / 1000 * 4

print(m_res)
