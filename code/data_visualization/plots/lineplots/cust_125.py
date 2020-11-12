# Import packages
import pandas as pd
from pandas.plotting import lag_plot
import matplotlib.pyplot as plt
import sklearn.model_selection as splitter
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_pacf
from matplotlib.dates import DateFormatter
import matplotlib.dates as dates
# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20201014_300_klanten.csv', parse_dates=[0])

# Manipulate data
custfilter = df['cust_id'] == 'klant_125'
yearfilter = df['procesdag'].dt.year >= 2017
weekendfilter = df['procesdag'].dt.dayofweek < 5
data = df.where(custfilter & yearfilter& weekendfilter).dropna().reset_index(drop=True)

print(data.tail(20))

# Define sublots
fig, (full, year_2018) = plt.subplots(2)

# Plot whole timeline
x = data['procesdag']
y = data['aantal_pakketten']
full.plot(x, y)
full.xaxis.set_major_formatter(DateFormatter('%Y'))
full.xaxis.set_major_locator(dates.YearLocator())

# Plot 2018
plt_2018_filter = data['procesdag'].dt.year == 2018
data = data.where(plt_2018_filter).dropna()
x2 = data['procesdag']
y2 = data['aantal_pakketten']
print(data.info())
year_2018.plot(x2, y2)
year_2018.xaxis.set_major_formatter(DateFormatter('%m'))
year_2018.xaxis.set_major_locator(dates.MonthLocator())

#Show graphs
fig.tight_layout()
plt.show()
