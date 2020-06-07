import pandas as pd 
import matplotlib.pyplot as plt 

plt.style.use("seaborn")

data = pd.read_csv("data//data.csv")
ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']

fig,(ax1,ax2) =plt.subplots(nrows=2,ncols=1,sharex=True)

ax1.plot(ages,dev_sal,label = 'All Developer')
ax2.plot(ages,py_sal,label = 'Python')
ax2.plot(ages,js_sal,label = 'Java Script')

# ax1.set_xlabel('Ages')
ax1.set_ylabel('Salary')
ax1.set_title('Median Salary by Age')

ax1.legend()

ax2.set_xlabel('Ages')
ax2.set_ylabel('Salary')
# ax2.set_title('Median Salary by Age')

ax2.legend()

plt.show()