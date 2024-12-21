import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(-50,50,0.01)

x1 = 5 * np.cos(0.3 * t) + np.sin(0.1 * t)

x2 = 3 * np.cos(0.2 * t) - 2 * np.sin(0.4 * t)

x1m = x1 * np.cos(10 * t)

x2m = x2 * np.cos(20 * t)

plt.plot(t, x1m, label = 'x1m')
plt.legend()
plt.figure()

plt.plot(t, x2m, label = 'x2m')
plt.legend()

x = x1m + x2m

plt.figure()

plt.plot(t, x, label = 'x1m + x2m')
plt.legend()

plt.show()