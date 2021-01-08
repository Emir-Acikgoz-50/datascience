<h1>Data science personal portfolio</h1>

**Student**: Rick Hagenaar<br/>
**Student ID**: 17141869<br/>
**Date**: ...<br/>

<h1>Introduction</h1>

<h1>Table of content</h1>

1. Research project
2. Domain knowledge
3. Predictive analysis
4. Data preprocessing
5. Communication
6. REflection and Evaluation


<h1>1. Research project</h1>



1.1. [Task Definition](https://github.com/Rikku77/datascience/blob/master/portfolio/research_project/task_definition.md)</br>
1.2. [Planning and Approach](https://github.com/Rikku77/datascience/blob/master/portfolio/research_project/planning.md)</br>
1.3. [Evaluation](https://github.com/Rikku77/datascience/blob/master/portfolio/research_project/evaluation.md)</br>
1.4. [Conclusions](https://github.com/Rikku77/datascience/blob/master/portfolio/research_project/conclusions.md)</br>

<h1>2. Domain knowledge</h1>

2.1. [Literature research](https://github.com/Rikku77/datascience/blob/master/portfolio/domain_knowledge/literature_research.md)</br>
2.2. [Courses](https://github.com/Rikku77/datascience/blob/master/portfolio/domain_knowledge/courses.md)</br>
2.3. [Jargon and terminology](https://github.com/Rikku77/datascience/blob/master/portfolio/domain_knowledge/jargon_and_terminology.md)</br>

<h1>3. Predictive analysis</h1>



[3.1. Multi variate regression](https://github.com/Rikku77/datascience/blob/master/portfolio/predictive_analysis/multivariate_lineair_regression.md)</br>
[3.2. Neural networks](https://github.com/Rikku77/datascience/blob/master/portfolio/predictive_analysis/neural_networks.md)</br>

<h1>4. Data preprocessing</h1>

Data preprocessing is all about preparing the data in such a way, that the model can produce tangible results. Preprocessing is also about understanding the data you're working with. I've done a couple of things to prepare the data.

<h2>4.1. Data exploration</h2>

When it comes to data exploration i've done a couple of things. I've namely:

- explored the main datasets
- looked at google trend functionality
- looked at other datasets like weather data (knmi)

<h3>4.1.1. Exploring the main dataset</h3>
At the first of the project we received a dataset from our project owner. This dataset was in csv (comma's separated values) format and consisted of nearly ten-thousand rows and 5 columns. The column definitions were as follows.

1. **index column**: Signifies the index of each row, starting from zero
2. **process day**: Indicates the day in which a certain amount of packages were processed.
3. **customer id**: The id of the customer
4. **package amount**: the amount of packages for that day
5. **package amount next day**: the amount of packages for the next day
  
<h2>4.2. Data cleansing</h2>

When it comes to cleaning the data, i haven't realy done much. This is because the dataset was already quite clean. For example, the dataset didn't contain any missing or inconsistent values. The only cleansing that i've realy done was parsing date types and setting the index to the process day, for easier time slicing.

```
# Read CSV file
df_postnl = pd.read_csv('/datc/parcel/notebooks/data/postnl/20201014_300_klanten.csv', parse_dates=[0], index_col=[0])
```

<h2>4.3. Data preparation</h2>



<h2>4.4. Data explanation</h2>



<h2>4.5. Data visualization</h2>



<h1>5. Communication</h1>



<h1>6. Reflection and Evaluation</h1>

