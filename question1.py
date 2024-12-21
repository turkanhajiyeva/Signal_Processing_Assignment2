import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

Ts = 0.01

t = np.arange(-50,50,0.01)

x1 = 5 * np.cos(0.3 * t) + np.sin(0.1 * t)

x2 = 3 * np.cos(0.2 * t) - 2 * np.sin(0.4 * t)

plt.plot(t, x1, label = f'x1')

plt.plot(t, x2, label = f'x2')

plt.legend()

plt.show()