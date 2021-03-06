# Import packages
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as lm
import sklearn.model_selection as splitter
from sklearn import metrics

# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20200904_Sample.csv', index_col=0, parse_dates=[1])

# Manipulate data
cust_filter = df['cust_id'] == 'klant_1'
date_filter = df['procesdag'].dt.dayofweek <= 4
df = df.where(date_filter & cust_filter).dropna()

# Define x and y
x = pd.to_datetime(df['procesdag']).map(dt.datetime.toordinal).to_numpy().reshape(-1, 1)
y = df['aantal_pakketten'].to_numpy().reshape(-1, 1)

# Define train and test datasets
x_train, x_test, y_train, y_test = splitter.train_test_split(x, y, test_size=0.1, random_state=0)

# Fit model
model = lm.LinearRegression()
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate model
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R squarred on test set:', model.score(x_test, y_test))

# Plot the result
fig, ax = plt.subplots()
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred, color='blue')
plt.show()