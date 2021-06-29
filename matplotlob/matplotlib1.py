# graphic of numbers representation in (x, y)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [4, 8, 2, 6, 9, 1, 7, 3, 7]

plt.plot(x, y)
plt.xlabel('Time (s)')
plt.ylabel('TEmperature (degC)')
plt.show()

