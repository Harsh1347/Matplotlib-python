from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 

plt.style.use('seaborn')

data = pd.read_csv('data//yt_data.csv')

view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# x = [1,9,4,1,2,6,6,7,8,9,2,3,5,1,8,4,2,6,4,7,8,4,5,8]
# y = [4,5,6,8,1,3,4,5,6,7,8,9,3,2,6,7,8,2,1,4,6,9,4,2]
# colors = [9,7,3,8,7,3,4,5,6,7,9,6,3,2,4,4,8,2,5,4,6,9,4,10]
# size = [201,309,404,211,322,556,236,337,128,629,322,433,325,111,238,234,312,216,214,127,128,224,325,118]
plt.scatter(view_count,likes,c= ratio,cmap='summer',
            edgecolor = 'black',linewidths=1,
            alpha=0.5) 

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.title("Scatter Plot")
plt.show()