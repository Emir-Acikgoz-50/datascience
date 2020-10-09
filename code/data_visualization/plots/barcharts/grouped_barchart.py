# Import packages
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np

# Read CSV file
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20200904_Sample.csv', index_col=0, parse_dates=[1])

# Manipulate data
df['jaar'] = df['procesdag'].dt.year
new_df = df.groupby([df['cust_id'], df['jaar']]).agg(
    totaal_aantal_pakketten = ('aantal_pakketten', 'sum'),
    totaal_aantal_pakketten_volgende_dag = ('aantal_pakketten_volgende_dag', 'sum')
).reset_index()

cust1 = new_df['totaal_aantal_pakketten'].where(new_df['cust_id'] == 'klant_1').dropna().to_numpy()
cust2 = new_df['totaal_aantal_pakketten'].where(new_df['cust_id'] == 'klant_2').dropna().to_numpy()
cust3 = new_df['totaal_aantal_pakketten'].where(new_df['cust_id'] == 'klant_3').dropna().to_numpy()
cust4 = new_df['totaal_aantal_pakketten'].where(new_df['cust_id'] == 'klant_4').dropna().to_numpy()
cust5 = new_df['totaal_aantal_pakketten'].where(new_df['cust_id'] == 'klant_5').dropna().to_numpy()
cust6 = new_df['totaal_aantal_pakketten'].where(new_df['cust_id'] == 'klant_6').dropna().to_numpy()








