import numpy as np
import matplotlib.pyplot as plt

xstart = 0
xstop = 2*np.pi
increment = 0.1

x = np.arange(xstart, xstop, increment)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, x, y2)
plt.legend(['sin(x)', 'cos(x)'])
plt.show()

