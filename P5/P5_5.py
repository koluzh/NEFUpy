import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-1, 1, 100)
fig, axs = plt.subplots(4, 1)
for i in range(4):
    temp_y = X ** (i + 1)
    axs[i] .plot(X, temp_y)

plt.show()

# making plot color red