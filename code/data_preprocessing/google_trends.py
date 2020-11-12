# Source: https://predictivehacks.com/get-google-trends-using-python/

# Import packages
import matplotlib.pyplot as plt
import pandas as pd
from pytrends.request import TrendReq

# Create pytrends obj
pytrend = TrendReq()

# Create list with keywords
kw_list = ['kerst', 'black friday', 'sinterklaas']

# Create payload
pytrend.build_payload(kw_list, timeframe='2015-01-02 2019-06-29', geo='NL')

# Get interest over time, in a dataframe and reset it's index
interest = pytrend.interest_over_time().reset_index()

# Select every row, where the date falls in Q4 and drop all rows with NaN values
q4_interest = interest.where(interest['date'].dt.month  >= 10).dropna()

# Define X and Y
x = q4_interest['date'].where(q4_interest['date'].dt.year == 2018)
y1 = q4_interest['black friday']
y2 = q4_interest['sinterklaas']
y3 = q4_interest['kerst']

# Plot graphs
fig, ax = plt.subplots(figsize=(10,7))

ax.plot(x, y1, label='black friday', linestyle='-', marker='o')
ax.plot(x, y2, label='sinterklaas', linestyle='-', marker='o')
ax.plot(x, y3, label='kerst', linestyle='-', marker='o')
ax.set(
    xlabel='Q4 in 2018',
    ylabel='Aantal zoekresultaten',
    title='Aantal zoekresultaten, per sleutelwoord, over Q4 in 2018')
ax.grid()
plt.legend()
plt.show()

# Print DataFrame: interest (this is without the Q4 filtering)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(interest)
