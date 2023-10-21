import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(1, 2, 100)
y = np.linspace(0, 1, 100)
x,y = np.meshgrid(x, y)
z = np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y)
ax.plot_surface(x, y, z)
plt.show()