'''
In SQL,In order to group by and perform an aggregation on that front:we use:

select colm,sum(colm)
from <table_name>
group by colm
order by sum(colm)
'''

'''
In python,we need to make use of groupby function where we need specify the column we want to groupby
then we concat the 'agg' short for aggregate method and pass the column we want aggregation on along with the 
type of aggregation we want
'''

import pandas as pd

df=pd.read_csv('age_income.csv')

#Grouping by Marital status to find the sum of income different marital status

print(df.groupby('Marital Status').agg({'Income':'sum'}))