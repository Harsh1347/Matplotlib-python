from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

minutes = [x for x in range(1,10)]

player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,3,1,4,2,5,4,5]
player3 = [1,1,1,1,2,5,3,4,5]

labels =['player1','player2','player3']

plt.stackplot(minutes,player1,player2,player3,labels=labels)

plt.legend(loc='upper left')    

plt.show()