# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as splitter
import numpy as np
from statsmodels.tsa.statespace import sarimax

# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20201014_300_klanten.csv', parse_dates=[0])
custfilter = df['cust_id'] == 'klant_125'
yearfilter = df['procesdag'].dt.year >= 2017
data = df.where(custfilter & yearfilter).dropna().reset_index(drop=True)

# Configure model
model = sarimax()

