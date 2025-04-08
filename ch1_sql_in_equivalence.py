# SQL in equivalence in pandas

'''
In SQL, if we want to filter out the records by searching for existence of some values, we use 'in' keyword i.e.

consider i want to have records of 'Gisela,Bradley,Hiroko' . I can use the 'in' keyword in this way:

select *
from <table_name>
where Name in ('Gisela','Bradley','Hiroko');
'''

'''
In pandas, we can achieve the same result by using 'isin()' method.

The basic syntax is:

df[df.<column_name>.isin(<What you are searching for>)]

'''

import pandas as pd

df=pd.read_csv('age_income.csv')


#creating a list of names we want

names=['Gisela','Bradley','Hiroko']

print(df[df.Name.isin(names)])