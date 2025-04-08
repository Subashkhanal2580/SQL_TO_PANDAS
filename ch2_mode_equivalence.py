'''
In SQL, mode() is not a recognized function. So,whenever we want to find the most repeated object within the dataset,
we usually query as below:

select age,count(age)
from
<table>
group by age
order by count(age) desc
limit 1

The query above counts the most repeating age and orders them in descending order. Once,limit is set to 1,we can find the
mode of the Age which is essentially given by using count() method here.

'''

'''
In python,There is indeed an inbuilt mode() method that helps us to find the mode for a particular column as :

df['col_name'].mode()


'''

import pandas as pd

df=pd.read_csv('age_income.csv')

#Finding the mode for Age and marital status column

print("The mode for the age column is:",df['Age'].mode(),"\nThe mode for Marital Status column is:",df['Marital Status'].mode())