from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 

plt.style.use('fivethirtyeight')

ages = [19,28,20,21,25,26,29,31,35,39,45,55,60]

median_age = 29

data = pd.read_csv('data//ages.csv')
ids = data['Responder_id']
ages = data['Age']
plt.hist(ages,bins=[10,20,30,40,50,60,70,80,90,100],edgecolor = 'black',log=True)

plt.axvline(median_age,color ="red",label = 'Age Median')

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.show()