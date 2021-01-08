<h1>3.1. Multivariate Lineair Regression</h1>

- Why multivariate linear regression?



- How has the model been configured.



**Important**: For the sake of completion and consistency, i will be using the most complete notebook covering multivariate lineair regression. This notebook can be found by clicking the following link.

- [Notebook](https://github.com/Rikku77/datascience/blob/master/notebooks/multi_variate_lineair_regression/mvlr_klant_125_gehele_tijdsreeks_compleet.ipynb).

Before training the model, i split the dataset into the following sets:

- Train
- Validation
- Test

The train set is used to train the model, the validation set is used to validate how the training process went and the test set is used for an unbiased evaluation on unseen data. Splitting up the dataset like this, is called *Cross validation*. In my case i decided to use data until 2018 for training, data from the year 2018 for validation and data from the year 2019 for test. I chose this split because its an approximate "60-20-20 split", which is a common ratio to use ([according to this article](https://glassboxmedicine.com/2019/09/15/best-use-of-train-val-test-splits-with-tips-for-medical-data/)), and i wanted to use whole years to train and validate on to see how predictions would be for different months and seasons. The split looks as follows. 
```
# Split train and test
train = df_postnl[:'2017'].dropna()
validation = df_postnl['2018'].dropna()
test= df_postnl['2019'].dropna()

# Define Y train, valid and test
y_train = train.loc[:, 'aantal_pakketten_volgende_dag']
y_valid = validation.loc[:, 'aantal_pakketten_volgende_dag']
y_test = test.loc[:, 'aantal_pakketten_volgende_dag']

# Define X train, valid and test
x_train = train.loc[:, train.columns != 'aantal_pakketten_volgende_dag']
x_valid = validation.loc[:, validation.columns != 'aantal_pakketten_volgende_dag']
x_test = test.loc[:, test.columns != 'aantal_pakketten_volgende_dag']
```
![Split Visual](https://github.com/Rikku77/datascience/blob/master/portfolio/predictive_analysis/images/split_visual.png)

*This codeblock and the corresponding visualization can be found in the notebook mentioned earlier, at section 1.4. (Train Validation Test split).* 

<h2>Training proces</h2>

So, as i mentioned before, i used all the data up until the year 2018 for the train set. This train set was then used to fit the model. Then predictions were made on the seperate validation dataset, to see how the model would perform. The result is the following visualization. 

![validation pred](https://github.com/Rikku77/datascience/blob/master/portfolio/predictive_analysis/images/prediction_validation.png)

*This image can be found in the notebook mentioned earlier, at section 2. (Model).*

<h2>Evaluation</h2>

For the evaluation i used 3 different metrics. These are:

- Root Mean Squared Error
- Mean Absolute Error
- R-Squared

<h2>Visualization</h2>

- 
