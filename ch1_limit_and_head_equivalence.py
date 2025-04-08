# SQL LIMIT TO PANDAS HEAD() EQUIVALENCE

'''
## SQL Limit 

In SQL, if we have N number of records and want to view only first few records, We use the Limit keyword
The Limit Keyword followed by a numerical value specifies the number of rows that we want to view.

The basic syntax of limit is:

select *
from <table_name>
Limit N;

-- Here , N specifies the number of records we want to view

'''

'''
## Python head()

In python, If we have N number of records in our dataframe and want to view only first few records,
we can use head() function . By default , head function provides us with 5 records. We can specify
argument inside the head() function if we want to view more than 5 records.

'''

## Loading the csv into pandas dataframe

import pandas as pd

df=pd.read_csv('age_income.csv')

## Using the head() function to view the first 10 records

print(df.head(10))

