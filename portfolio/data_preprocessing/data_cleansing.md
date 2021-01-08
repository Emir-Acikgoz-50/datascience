<h1>Data Cleansing</h1>

When it comes to cleaning the data, i haven't realy done much. This is because the dataset was already quite clean. For example, the dataset didn't contain any missing or inconsistent values. The only cleansing that i've realy done was parsing date types and setting the index to the process day, for easier time slicing.

```
# Read CSV file
df_postnl = pd.read_csv('/datc/parcel/notebooks/data/postnl/20201014_300_klanten.csv', parse_dates=[0], index_col=[0])
```

