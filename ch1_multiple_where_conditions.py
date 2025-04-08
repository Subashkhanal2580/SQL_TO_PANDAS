'''
In SQL, we can specify multiple where clause in the select clause as

select *
from <table_name>
where condn1
and
condn2;
'''

'''
In python, we can specify the multiple conditions inside the dataframe as:

df[(df['col1']=='condition1') & (df['col2']=='condition2')].head()


'''

#importing pandas as pd

import pandas as pd

#loading the csv into pandas dataframe

df=pd.read_csv('age_income.csv')

#Filtering out the records for people who are married and are over age of 20 and earnign more than 70000

print(df[(df['Marital Status']=='Married') & (df['Age']>20) & (df['Income']>70000)].head(10))