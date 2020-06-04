from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.05,0]

colors = ['#008fd5','#fc4f30','#e5ae37']

plt.pie(slices,labels=labels,explode=explode,
        shadow=True,startangle=90,
        wedgeprops={'edgecolor':'black'},
        autopct='%1.1f%%'
        )
plt.show()

