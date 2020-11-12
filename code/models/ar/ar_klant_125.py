# Import packages
import pandas as pd
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
import sklearn.model_selection as splitter
import numpy as np
from statsmodels.tsa.ar_model import AR
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20201014_300_klanten.csv', parse_dates=[0])

# Manipulate data
custfilter = df['cust_id'] == 'klant_125'
yearfilter = df['procesdag'].dt.year >= 2017
weekendfilter = df['procesdag'].dt.dayofweek < 5
df = df.where(custfilter & yearfilter & weekendfilter).dropna().reset_index(drop=True)

# Analyse data
#lag_plot(df['aantal_pakketten']) # Lag plot
autocorrelation_plot(df['aantal_pakketten']) # Auto correlation plot
plt.show()

# Define train, test and validation sets
train = df.where(df['validation_column'] == 'train')
test = df.where(df['validation_column'] == 'test')
validation = df.where(df['validation_column'] == 'validation')

# Configure model
model = AR(train['aantal_pakketten'])
result = model.fit()

# make prediction
y_pred = result.predict(test['procesdag'], test['aantal_pakketten'])
print('coeffcients: ' + result.params)


