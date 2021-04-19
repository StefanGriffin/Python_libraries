import math as mt
import numpy as np

# x = 2
# y = 2

# f = 3*mt.pow(x,2) + mt.sqrt(mt.pow(x, 2) + mt.pow(y, 2)) + mt.exp(mt.log(x))

# print(f)


def func_ex(x, y):
    f = 3*mt.pow(x,2) + mt.sqrt(mt.pow(x, 2) + mt.pow(y, 2)) + mt.exp(mt.log(x))
    return f

x = 3
y = 7

f = func_ex(x, y)
print(f)



