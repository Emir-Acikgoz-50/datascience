<h1>4.3. Data Preparation</h1>

Notebooks:

1. [Multivariate Lineair Regression](https://github.com/Rikku77/datascience/blob/master/notebooks/multi_variate_lineair_regression/mvlr_klant_125_gehele_tijdsreeks_compleet.ipynb)

I have done a couple of things to prepare the data in an adequate way. First i loaded the data in via pandas *ReadCSV* function, parsed the first column to a datetime object and set that first column as the index (***see notebook 1, section 1.1***). I did this because setting a datetime index makes workinng with timeseries a lot easier.
```
# Read CSV file
df_postnl = pd.read_csv('/datc/parcel/notebooks/data/postnl/20201014_300_klanten.csv', parse_dates=[0], index_col=[0])
```

Afterwards, i filtered out the year 2020 and selected the customer that i wanted to generate predictions for (***see notebook 1, section 1.2***). After each manipulation, i dropped all the rows that included *NaN* values. I knew this was save to do because i knew there were no *NaN* values when i initially imported the dataset. Lastly, i also dropped both the *cust_id* and *validation_column* columns, because i didn't need the former anymore and i wasn't going to use the latter.

```
# Select every row where cust_id is equal to "klant_125"
custfilter = df_postnl['cust_id'] == 'klant_125'
df_postnl = df_postnl.where(custfilter).dropna()

# Remove data for the year 2020, since we'll not includes this
df_postnl = df_postnl[:'2019'].dropna()

# Delete columns: cust_id and validation column.
df_postnl = df_postnl.drop(['cust_id', 'validation_column'], axis=1)
```







