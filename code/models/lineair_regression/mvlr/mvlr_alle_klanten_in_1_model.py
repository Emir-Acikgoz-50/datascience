# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
from sklearn.metrics import mean_squared_error, r2_score

# Read CSV file
df_postnl = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20201014_300_klanten.csv', parse_dates=[0])

# Get customers
cust = df_postnl.loc[:, 'cust_id']

# Encode customers and day of the week
df_postnl.insert(loc=1, column='weekdag', value=df_postnl['procesdag'].dt.dayofweek)
df_postnl = pd.get_dummies(df_postnl, columns=['weekdag', 'cust_id'])

# Reinsert customers
df_postnl.insert(loc=1, column='cust_id', value=cust)

# Split whole df
start = df_postnl['procesdag'] >= datetime(year=2018, month=11, day=1)
end = df_postnl['procesdag'] <= datetime(year=2018, month=11, day=30)
df_postnl = df_postnl.where(start & end).dropna()

# Split train and test
train_filter = df_postnl['procesdag'] <= datetime(year=2018, month=11, day=23)
test_filter = df_postnl['procesdag'] >= datetime(year=2018, month=11, day=24)

train = df_postnl.where(train_filter).dropna()
test = df_postnl.where(test_filter).dropna()

# Define X train and test
x_train = train[train.columns[5:]]
x_test = test[test.columns[5:]]

# Define Y train and test
y_train = train.loc[:,'aantal_pakketten']
y_test = test.loc[:,'aantal_pakketten']

# Fit model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Make prediction
pred = lr.predict(x_test)

# Create result df
df_result = pd.DataFrame({'procesdag':test['procesdag'], 'cust_id':test['cust_id'], 'actual':y_test, 'predicted': pred})

# Filter customer
df_postnl = df_postnl.where((df_postnl['cust_id'] == 'klant_125')).dropna()
df_result = df_result.where((df_result['cust_id'] == 'klant_125')).dropna()

# Plot actual vs. predicted
fig, ax = plt.subplots()
ax.plot(df_result['procesdag'], df_result['actual'], label='Actual', marker='o')
ax.plot(df_result['procesdag'], df_result['predicted'], label='Predicted', marker='o')
ax.set(
    xlabel='Dag',
    ylabel='Aantal pakketten',
    title='Werkelijke en voorspelde aantal pakketten voor klant 125')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.show()

# Evaluate model
rmse = (np.sqrt(mean_squared_error(df_result['actual'], df_result['predicted'])))
r2 = r2_score(df_result['actual'], df_result['predicted'])

print('Root Mean Squared Error:', rmse)
print('R2 score:', r2)