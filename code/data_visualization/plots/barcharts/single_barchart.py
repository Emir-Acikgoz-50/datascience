# Import packages
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Helper methodes
def millions_formatter(x, pos) :
    '''Format X for a given position to millions notation'''
    return '%1.1fM' % (x * 1e-6)

# Import data
df = pd.read_csv('C:\\School\\Blok13\\Project\\Repos\\PostNL\\code\\datasets\\20200904_Sample.csv',  index_col=0, parse_dates=[1])

# Manipulate data
df['jaar'] = df['procesdag'].dt.year
new_df = df.groupby([df['cust_id'], df['jaar']]).agg(
    totaal_aantal_pakketten = ('aantal_pakketten', 'sum'),
    totaal_aantal_pakketten_volgende_dag = ('aantal_pakketten_volgende_dag', 'sum')
).reset_index()

# Filter DataFrame (df) for, 'klant_2'
df_klant2 = new_df.where(new_df['cust_id'] == 'klant_2').dropna()

# Plot barchart
fig, ax = plt.subplots()
ax.bar(df_klant2['jaar'], df_klant2['totaal_aantal_pakketten'])
ax.set(
    xlabel='Jaar',
    ylabel='Aantal pakketten',
    title='Aantal pakketten per jaar voor klant 2')
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions_formatter))
plt.show()