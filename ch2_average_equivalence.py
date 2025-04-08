'''
In order to find the average value for a particular column in SQL,

select avg(column_name)
from
<table_name>;

'''

'''
But in case of pandas, we have inbuilt method known as 'mean()'
which computes the average value for the specified column.
'''


import pandas as pd

df=pd.read_csv('age_income.csv')

##Finding the average of age column

print(df['Age'].mean())