#Single where clause statement in SQL equivalence in python-pandas

'''

When using Where clause , we specify a condition and the records are loaded once the condition is satisfied.

The syntax for where clause is:

select *
from <table_name>
where <condn>;


'''

'''
In pandas,we can do this by specify the condition within the df as:

df[df['Column_name']=='Condn']

'''

#Importing pandas as pd
import pandas as pd

#Loading csv into python dataframe

df=pd.read_csv('age_income.csv')

#Performing the where clause equivalence

print(df[df['Marital Status']=='Married'].head(10)) ## Displays the first 10 records where marital status is 'married'