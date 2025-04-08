'''
In SQl,Consider that we want to categorize the 'experience' based on the age column values.

select *,
case
    when age<18 then 'newbie'
    when age>=30 then 'Intermediate'
    else 'Veteran'
End as experience_level
'''

'''
However, In order to replicate the Case statement functionality in python , The following steps are taken into consideration

1.Create a user defined function and specify the same conditions as in case statement using 'if-else' statements.
2.Create a new column and equate it with the column you want to categorize the values on followed by applying the lambda function as below:

--- df['experience'] = df['Age'].apply(lambda x: <user_defined_function_name>(x))


'''

import pandas as pd

df=pd.read_csv('age_income.csv')

#Creating a user-defined function

def age_exp(age):
    if age<=18:
        return 'newbie'
    elif age<=38:
        return 'Intermediate'
    elif age>39:
        return 'Senior'
    else:
        return 'veteran'


#Applying the lambda function on the new column 

df['experience']=df['Age'].apply(lambda x: age_exp(x))

print(df.head(10))