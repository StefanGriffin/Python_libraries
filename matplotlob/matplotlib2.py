import numpy as np
import matplotlib.pyplot as plt

x = [2, 4, 6, 7, 8, 10]
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()



