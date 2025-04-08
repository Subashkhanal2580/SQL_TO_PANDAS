#SQL not in equivalencce

''' 
In SQL, if we want to filter out the records by searching for existence of other values rather than some values, we use 'not in' keyword i.e.

consider i want to have other records than of 'Gisela,Bradley,Hiroko' . I can use the 'not in' keyword in this way:

select *
from <table_name>
where Name not in ('Gisela','Bradley','Hiroko');'
'''

'''
In pandas, This can be done by applying '~' inverse operator in the 'isin()' operation as

df[~df.Name.isin('Gisela','Bradley','Hiroko')]  --> This script provides all the records for all other names except the
three names mentioned.
'''

import pandas as pd

df=pd.read_csv('age_income.csv')


names=['Gisela','Bradley','Hiroko']

print(df[~df.Name.isin(names)])