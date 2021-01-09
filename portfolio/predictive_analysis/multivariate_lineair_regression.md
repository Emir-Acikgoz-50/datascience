<h1>3.1. Multivariate Lineair Regression</h1>

The primary model that i've worked on was multivariate lineair regression. I decided to use this model because our problem was a regression problem and i wanted to use multiple features, like: the day of the week, holidays and the amount of packages from last week. For the implementation, i used the *LinearRegression* function from *sklearn*. 

Notebooks:

1. [Multivariate Linear Regression](https://github.com/Rikku77/datascience/blob/master/notebooks/multi_variate_lineair_regression/mvlr_klant_125_gehele_tijdsreeks_compleet.ipynb).

<h2>Feature Selection</h2>

Since i was going to use, multivariate linear regression, i was most certainly going to use multi features (***see notebook 1, section 1.3***). When it came to feature selection, i had used the following:

- The amount of packages
- the day of the week
- the month
- the amount of packages from 7 days earlier 
- the rolling average of 7 days

Corresponding to the selection of these features, i had constructed a correlation matrix. From this correlation matrix i concluded that the weekday, the rolling average and the amount of packaged from 7 days earlier were quite well correlated with the amount of packages for the next day, compared to the month and holiday. I reckon that the reason for this is because there aren't a lot examples of holidays in a period of 3 years and, if this case, the month itself might not say a lot about a daily prediction. Nevertheless i used all of these features for the model.

<h2>Train, validation, test split</h2>

Before defining the model, i split the dataset into the following sets:

- Train
- Validation
- Test

The train set is used to train the model, the validation set is used to validate how the training process went and the test set is used for an unbiased evaluation on unseen data. Splitting up the dataset like this, is called *Cross validation*. In my case i decided to use data until 2018 for training, data from the year 2018 for validation and data from the year 2019 for test. I chose this split because its an approximate "60-20-20 split", which is a common ratio to use ([according to this article](https://glassboxmedicine.com/2019/09/15/best-use-of-train-val-test-splits-with-tips-for-medical-data/)), and i also wanted to use whole years to validate and evaluate on to see how predictions would be for different months and seasons. The split looks as follows (***see notebook 1, section 1.4***). 
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

<h2>Training</h2>

So, as i mentioned before, i used all the data up until the year 2018 for the train set. This train set was then used to fit the model. Then predictions were made on the seperate validation dataset, to see how the model would perform. The result is the following visualization (***see notebook 1, section 2***). 

![validation pred](https://github.com/Rikku77/datascience/blob/master/portfolio/predictive_analysis/images/prediction_validation.png)

From this visualization, we can conclude that there is no indication of the model overfitting nor underfitting. Moreover, to check how well the model performs, i also used some different evaluation metrics. these metrics are:

- Root Mean Squared Error
- Mean Absolute Error
- R-Squared

The scores are as follows:

- Root Mean Squared Error: 737.815339168826</br>
- Mean Absolute Error: 435.90606774816166</br>
- R2_Score 0.8075204801379219</br>

<h2>Evaluation</h2>

For the evaluation i used the test set, to get a final unbiased evaluation (***see notebook 1, Conclusion***). Just like with the validation data, i used the same  metrics as before to evaluate the model's performance on the test set. The results are as follows.

![test pred](https://github.com/Rikku77/datascience/blob/master/portfolio/predictive_analysis/images/prediction_test.png)

Root Mean Squared Error: 693.3821141491522</br>
Mean Absolute Error: 394.50638401761995</br>
R2_Score 0.8577826214275516</br>
