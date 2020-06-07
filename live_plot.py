import random
from itertools import count 
import pandas as pd
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x = []
y = []

index = count()

def animante(i):
    x.append(next(index))
    y.append(random.randint(0,10))    
    if len(x) <20:  
        plt.cla()
        plt.plot(x,y)
    else:
        plt.cla()
        plt.plot(x[-20:],y[-20:]) 


ani = FuncAnimation(plt.gcf(),animante,interval = 500)




plt.show()