import math as mt
import numpy as np


def func_ex(x, y):
    f = 3*np.power(x, 2) + np.sqrt(np.power(x, 2) + np.power(y, 2)) + np.exp(np.log)
    return f

start = 0
stop = 11
increment  = 1

x_data = np.arange(start, stop, increment)
y_data = np.arange(start, stop, increment)

for x in x_data:
    for y in y_data:
        f = func_ex(x, y)
        print(f'f({x},{y})={f}'
        
        )

