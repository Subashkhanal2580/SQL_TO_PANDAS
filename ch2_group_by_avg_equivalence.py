'''
In SQl,in order to find the average of a column after performing group by
we use:

select avg(age)
from
<table_name>
group by colm_name;

'''

'''
In pandas, Its relatively easy by using the mean method where we only need to pass the colm_name we want to group by
followed by mean() method.

Doing so, It generates the average of all the numerical column once grouped by a particular column


'''

import pandas as pd

df=pd.read_csv('age_income.csv')

#Finding the average age and income for different marital status

print(df.groupby('Marital Status',dropna=False).agg({'Income':'mean','Age':'mean'})) #Dropna=False so that it avoids overlooking the null state