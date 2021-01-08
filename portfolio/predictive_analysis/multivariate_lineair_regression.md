<h1>3.1. Multivariate Lineair Regression</h1>

- Why multivariate linear regression?
- How has the model been configured.

<h2>Training</h2>

Before training the model, i split the dataset into the following sets:

- Train
- Validation
- Test

The train set is used to train the model, the validation set is used to validate how the training process went and the test set is used for an unbiased evaluation on unseen data. Splitting up the dataset like this, is called *Cross validation*. In my case i decided to use data until 2018 for training, data from the year 2018 for validation and data from the year 2019 for test. I chose this split because its an approximate "60-20-20 split", which is a common ratio to use, and i wanted to use whole years to train and validate on to see how predictions would be for different months and seasons. 

```
# Split train and test
train = df_postnl[:'2017'].dropna()
validation = df_postnl['2018'].dropna()
test= df_postnl['2019'].dropna()
```

<h2>Evaluation</h2>

- Metrics

<h2>Visualization</h2>

- 
