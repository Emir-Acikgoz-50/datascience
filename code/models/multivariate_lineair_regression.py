# Import packages
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as lm
import sklearn.model_selection as splitter
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20200904_Sample.csv',  index_col=0, parse_dates=[1])

# Manipulate data
cust_filter = df['cust_id'] == 'klant_1'
date_filter = df['procesdag'].dt.dayofweek <= 4
df = df.where(date_filter & cust_filter).dropna()

df['weekdag'] = df['procesdag'].dt.dayofweek
df['maand'] = df['procesdag'].dt.month
df['jaar'] = df['procesdag'].dt.year

pd.set_option('display.max_columns', df.shape[1])
pd.set_option('display.width', None)
print(df.head(20))

# Define x and y
x = df.loc[:, ['weekdag', 'maand', 'jaar']].to_numpy()
y = df.loc[:, ['aantal_pakketten']].to_numpy()

# Feature extraction: Weekday, Month, Year
enc = OneHotEncoder(sparse=False)
x_transform = enc.fit_transform(x)

# Define train and test datasets
x_train, x_test, y_train, y_test = splitter.train_test_split(x_transform, y, test_size=0.1, random_state=0)

# Fit model
model = lm.LinearRegression(fit_intercept=False)
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate model
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print(x_test)

# Plot the result
fig, ax = plt.subplots()
plt.scatter(x_test[:, 0], y_test, color='black')
plt.plot(x_test[:, 0], y_pred, color='blue')
plt.show()

