<h1>3.1. Multivariate Lineair Regression</h1>

- Why multivariate linear regression?



- How has the model been configured.



**Important**: For the sake of completion and consistency, i will be using the most complete notebook covering multivariate lineair regression. This notebook can be found [here](https://github.com/Rikku77/datascience/blob/master/notebooks/multi_variate_lineair_regression/mvlr_klant_125_gehele_tijdsreeks_compleet.ipynb).

<h2>Training</h2>

Before training the model, i split the dataset into the following sets:

- Train
- Validation
- Test

The train set is used to train the model, the validation set is used to validate how the training process went and the test set is used for an unbiased evaluation on unseen data. Splitting up the dataset like this, is called *Cross validation*. In my case i decided to use data until 2018 for training, data from the year 2018 for validation and data from the year 2019 for test. I chose this split because its an approximate "60-20-20 split", which is a common ratio to use ([according to this article](https://glassboxmedicine.com/2019/09/15/best-use-of-train-val-test-splits-with-tips-for-medical-data/)), and i wanted to use whole years to train and validate on to see how predictions would be for different months and seasons. Looking at the 

<h2>Evaluation</h2>

For the evaluation

<h2>Visualization</h2>

- 
