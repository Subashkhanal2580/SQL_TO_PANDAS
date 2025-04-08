## Distinct and Drop Duplicates equivalence

'''
In SQL, The distinct keyword is used to filter out all the unique values in a particular column
In order to do this , We can take an example syntax below:

select distinct(column_name)
from <table_name>

The query above will return all the distinct values from the column as the output.

'''

'''
In python , The work done by distinct keyword in SQL is done by using the 'drop_duplicates()' method

The proper way for using drop_duplicates() method is:

df['column_name'].drop_duplicates()

The syntax above filters out the non-duplicate values present in that particular column
'''

import pandas as pd

#loading the csv into df

df=pd.read_csv('age_income.csv')

# View the first 10 rows of the df

# print("The first 10 records in the dataset are:",df.head(10))

# Find only the distinct values from 'Marital Status' column

print(df['Marital Status'].drop_duplicates())