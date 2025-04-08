## Select Statement in SQL equivalence with Pandas

'''
Consider that there are N number of columns in the dataset and
we are interested to view only one or two specific columns.
In SQL,we can do this easily by using the select clause as:

select column_name1,column_name2
from <table_name>;
'''

'''
In order to get the same result in python. We need to specify the
name of columns inside the python dataframe by creating a list i.e.

df[['column1','column2']].head()
'''


#Importing pandas as pd

import pandas as pd

#Performing equivalence of SQL

df=pd.read_csv('age_income.csv') #loading the csv into pandas dataframe

print(df[['Name','Marital Status']].head(15))

