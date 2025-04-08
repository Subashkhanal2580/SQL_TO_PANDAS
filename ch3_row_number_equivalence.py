'''
In SQL, The row number is calculated as:

select row_number() over(partition by colm_name order by colm_name) as rn
from <table_name>;

This helps us to sort the values based on the partition followed by the order.

'''

'''
In python, We can find the row_number in following steps:
1.Sort the columns that you want the row_number to be on the basis of
2.Group by the desired column that works similar to the partitioned column in sql
3.use the 'cumcount()+1' logic to print the row number in cummulative order based on the partition
4.Lastly,Sort the values based on the columns that you want row number on basis of.
'''
import pandas as pd

df=pd.read_csv('age_income.csv')

#Find the row number on age and name column once the partition is done in basis of marital status

df['rn']=df.sort_values(['Name','Age']).groupby(['Marital Status']).cumcount() + 1 #this gives unsorted row_numbers in order

print(df.sort_values(by=['Marital Status','Name','Age']))
