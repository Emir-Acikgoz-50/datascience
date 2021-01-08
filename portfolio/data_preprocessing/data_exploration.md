<h1>Data Exploration</h1>

When it comes to data exploration i've also mainly looked at the main dataset and google trends data. 

Notebooks:
1. [Weekly average per weekday, per customer](https://github.com/Rikku77/datascience/blob/master/notebooks/exploratory_visuals/gem_pakketten_per_klant_per_weekdag.ipynb)
2.  

<h2>Exploring the main datasets</h2>

At the start of the project we received a dataset from our project owner. This dataset was in csv (comma's separated values) format and consisted of nearly ten-thousand rows and 5 columns. The column definitions were as follows.

1. **index column**: Signifies the index of each row, starting from zero.
2. **process day**: Indicates the day in which a certain amount of packages were processed.
3. **customer id**: The id of the customer.
4. **package amount**: the amount of packages for that day.
5. **package amount next day**: the amount of packages for the next day.
 
This dataset includes data of 5 different customers from January 2015 up until June 2019. Sometime later, we received another dataset that included data for 300 customer, had around 500.000 rows and had an additional column. This column indicated whether a row was meant for training, validation or testing. However, since i wanted to define my own split, i decided to drop this column. 

For my initial exploration, before we got the bigger dataset, i started to make exploratory visualizations of each customer to understand general patterns in the amount of packages that needed to be processed for each customer. I started out with plotting the average amount of packages for each day in the week, for each customer (***see notebook 1***). Because of these visualizations, i knew that the weekend (especially saturday) was something to keep in mind with regarding the amount of processed packages. For example, i the following graph, you can see that the average amount of packages on Saturday for this customer is almost zero, which is reoccurend for other customers as well. 

![weekly_klant1](https://github.com/Rikku77/datascience/blob/master/portfolio/data_preprocessing/images/gem_wekelijks_klant1.png)

<h2>Google Trends and KNMI data</h2>

