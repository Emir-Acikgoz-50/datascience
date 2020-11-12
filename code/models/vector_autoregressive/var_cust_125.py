# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as splitter
from statsmodels.tsa.api import VAR
import numpy as np

# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20201014_300_klanten.csv', parse_dates=[0])

# Manipulate data
custfilter = df['cust_id'] == 'klant_125'
yearfilter = df['procesdag'].dt.year >= 2017
df = df.where(custfilter & yearfilter).dropna().reset_index(drop=True)
mdata = df[['aantal_pakketten']]
mdata.index = pd.DatetimeIndex(df['procesdag'])
data = np.log(mdata)

# Configure model
model = VAR(data)
results = model.fit()
print(results.summary())

# Plot
fig, ax = plt.subplots()
ax.bar(df['procesdag'], df['aantal_pakketten'])
plt.show()

