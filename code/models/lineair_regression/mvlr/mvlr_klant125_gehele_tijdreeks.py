# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as dates
from sklearn.linear_model import LinearRegression
from datetime import datetime
from sklearn.metrics import mean_squared_error, r2_score
import holidays

# Read CSV file
df_postnl = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20201014_300_klanten.csv', parse_dates=[0])

# Select every row where cust_id is equal to "klant_125"
custfilter = df_postnl['cust_id'] == 'klant_125'
df_postnl = df_postnl.where(custfilter).dropna()

# Select features
df_postnl.insert(loc=1, column='weekdag', value=df_postnl['procesdag'].dt.dayofweek)
df_postnl = pd.get_dummies(df_postnl, columns=['weekdag'])
df_postnl['aantal_pakketten_vorige_week'] = df_postnl['aantal_pakketten'].shift(7)
df_postnl['aantal_pakketten_vorige_week'].fillna(0, inplace=True)
holidays = holidays.Netherlands()
df_postnl['is_feestdag'] = df_postnl['procesdag'].isin(holidays['2015-01-02':'2019-12-31'])

# Split whole df
start = df_postnl['procesdag'] >= datetime(year=2015, month=1, day=2)
end = df_postnl['procesdag'] <= datetime(year=2019, month=12, day=31)

df_postnl = df_postnl.where(start & end).dropna()

# Split train and test
train_filter = df_postnl['procesdag'] <= datetime(year=2019, month=11, day=30)
test_filter = df_postnl['procesdag'] >= datetime(year=2019, month=12, day=1)

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

# Plot actual vs. predicted
fig, ax = plt.subplots()
ax.plot(test['procesdag'], y_test, label='Actual', marker='o')
ax.plot(test['procesdag'], pred, label='Predicted', marker='o')
ax.set(
    xlabel='Dag',
    ylabel='Aantal pakketten',
    title='Werkelijke en voorspelde aantal pakketten voor klant 125')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.show()

# Evaluate model
rmse = (np.sqrt(mean_squared_error(y_test, pred)))
r2 = r2_score(y_test, pred)

print('Root Mean Squared Error:', rmse)
print('R2 score:', r2)











