# Постройте графики функций f = x**3 и g = x**4 на интервале [0, 1] на
# разных графиках, так чтобы у них отличались цвета, тип линий и точек.
# Не забудьте также подписать оси и названия графиков.
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 1, 100)
Y1 = X ** 3
Y2 = X ** 4

fig, axs = plt.subplots(2, 1)
# making plot color red
axs[0].plot(X, Y1, color='red', linestyle='dashed', marker='o')
axs[0].set_title('f = x**3')
axs[1].plot(X, Y2)
axs[1].set_title('g = x**4')

plt.show()
