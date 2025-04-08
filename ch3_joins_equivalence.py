'''
In SQL, we can join two tables based on a same column ids or multiple column ids.

For joining tables in SQL:

select a.name,c.childrens
from age_income a
join
name_children c
on
a.name=c.name

'''

'''
Pandas provides us with the inbuilt merge() function that helps us to merge 2 or more table
based on the same id bearing columns situated in such tables.

case1:If the joining column of both tables share the same name

-> pd.merge(df1,df2,how='inner',on='Name')

here, df1 and df2 are the two tables that are to be merged and the type of join is specified as inner
the joining column is 'Name' column that has the same name in both the tables

case2:If the joining column of both tables share the different name

->pd.merge(df1,df2,how='inner',left_on='left_col_name',right_on='right_col_name')

'''

import pandas as pd

#Loading the csv files into the pandas dataframe

df1=pd.read_csv('age_income.csv')
df2=pd.read_csv('name_children.csv')

#Now we will merging these two tables

merged_df=pd.merge(df1,df2,how='inner',on='Name')

print(merged_df.head(20))