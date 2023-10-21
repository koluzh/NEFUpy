import numpy as np
import matplotlib.pyplot as plt

x = []
for i in range(10):
    x.append(i % 2)

plt.plot(x)

plt.show()