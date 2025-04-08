'''
In SQL, max and min functions are used to find the maximum and minimum value for specified column/s.

We use max and min in SQL as:

select max(col1),min(col1)
from
<table_name>;

'''


'''
In python , This can be done using the same approach as 'mean()'.
This is demonstrated in code below:
'''

import pandas as pd

df=pd.read_csv('age_income.csv')

print("The maximum value for age is:",df['Age'].max(),"\nThe minimum value for age is:",df['Age'].min())