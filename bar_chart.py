from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

x = [i for i in range(5)]

x_ind = np.arange(len(x))
width = 0.25

y1 = [i+2 for i in range(5)]
y2 = [i+4 for i in range(5)]
y3 = [i for i in range(5)]

plt.bar(x_ind,y1,width=width)
plt.bar(x_ind+width,y2,width=width)
plt.bar(x_ind-width,y3,width=width)
plt.show()