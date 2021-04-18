import numpy as np


data = [-1.0, 2.5, 3.25, 5.75]

m = str(np.mean(data))
print('The mean or average is:   ' + m)

st_dev = str(np.std(data))
print('Standard deviation is:   ' + st_dev)

med = str(np.median(data))
print('The Median is:   ' + med)

minv = str(np.min(data))
print('The minimul value is:   ' + minv)

maxv = str(np.max(data))
print('The maximum value is:   ' + maxv)


