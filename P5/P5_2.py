import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm


def monte_carlo_markov_chain(f, proposal, n_samples, initial_state):
    chain = [initial_state]
    for i in range(n_samples - 1):
        proposed_state = np.array([proposal[0](chain[-1][1]), proposal[1](chain[-1][0])])
        acceptance_ratio = f(*proposed_state) / f(*chain[-1])
        acceptance_ratio *= norm.pdf(chain[-1][0], proposed_state[1], 0.2)
        acceptance_ratio /= norm.pdf(proposed_state[0], chain[-1][1], 0.2)
        if acceptance_ratio > np.random.rand():
            chain.append(proposed_state)
        else:
            chain.append(chain[-1])
    plt.plot(chain)
    return np.array(chain)


def target_function(x, y):
    return np.exp(-10 * (x ** 2 - y) ** 2 - (y - 1. / 4.) ** 4)


def proposal_x(y):
    return np.random.normal(y, 0.2)


def proposal_y(x):
    return np.random.normal(x, 0.2)


# Находим максимум функции с помощью Монте-Карло на цепях Маркова.
n_samples = 100000
initial_state = np.array([0., 0.])
chain = monte_carlo_markov_chain(target_function, [proposal_x, proposal_y], n_samples, initial_state)
samples = chain

# Выводим среднее значение.
mean = np.mean(samples, axis=0)
print("Среднее значение: ", mean)

# Находим значение в которой функция достигает своего максимального значения.
max_index = np.argmax(target_function(samples[:, 0], samples[:, 1]))
max_value = target_function(samples[max_index, 0], samples[max_index, 1])
print("Значение в которой функция достигает своего максимума: ", max_value)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = target_function(X, Y)
ax.plot_surface(X, Y, Z, )

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('График функции f(x,y) = e^(-x^2-y^2)sin(5x)')
plt.show()
