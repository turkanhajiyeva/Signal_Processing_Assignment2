import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-50,50,0.01)

Ts = 0.01

x1 = 5 * np.cos(0.3 * t) + np.sin(0.1 * t)

x2 = 3 * np.cos(0.2 * t) - 2 * np.sin(0.4 * t)

x1m = x1 * np.cos(10 * t)

x2m = x2 * np.cos(20 * t)

x = x1m + x2m

w = 1

x1m_extracted = Ts * np.convolve(x, 2 * np.cos(10 * t) * (w / np.pi) * np.sinc((w/np.pi) * t), 'same')

x1_reconstructed = Ts * np.convolve(x1m_extracted * np.cos(10 * t), 2 * (w / np.pi) * np.sinc((w/np.pi) * t), 'same')

x2m_extracted = Ts * np.convolve(x, 2 * np.cos(20 * t) * (w / np.pi) * np.sinc((w/np.pi) * t), 'same')

x2_reconstructed = Ts * np.convolve(x2m_extracted * np.cos(20 * t), 2 * (w / np.pi) * np.sinc((w/np.pi) * t), 'same')

plt.plot(t, x1_reconstructed, label = 'x1 reconstructed')
plt.plot(t, x1, label = 'x1')
plt.legend()

plt.figure()

plt.plot(t, x2_reconstructed , label = 'x2 reconstructed')
plt.plot(t, x2, label = 'x2')
plt.legend()

plt.show()