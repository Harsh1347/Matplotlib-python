import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from matplotlib import dates as mlt_dates

plt.style.use('seaborn')

dates = [
    datetime(2020,5,20),
    datetime(2020,5,21),
    datetime(2020,5,22),
    datetime(2020,5,23),
    datetime(2020,5,24),
    datetime(2020,5,25),
    datetime(2020,5,26),
    datetime(2020,5,27)
]

# y = [0,1,6,3,4,5,4,7]

data=pd.read_csv("data//time_data.csv")

data['Date'] = pd.to_datetime(data["Date"])
data.sort_values('Date',inplace = True)
price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date,price_close,linestyle = 'solid')

plt.gcf().autofmt_xdate()

plt.show()