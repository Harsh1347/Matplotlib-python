from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

x = [x for x in range(-3,4)]
y = [x**2 for x in range(-3,4)]
y2 = [x**3 for x in range(-3,4)]

plt.style.use('fivethirtyeight')
plt.plot(x,y,label = 'square')
plt.plot(x,y2,label = 'cube')
plt.legend()
plt.show()
