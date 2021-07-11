from matplotlib import numpy as np

from matplotlib import pyplot as plt

x = np.arange(0, 20, 0.1)
k1 = 1
k2 = 2
plt.plot(x, np.cos(k1*x))
plt.plot(x, np.cos(k2*x))
plt.show()
