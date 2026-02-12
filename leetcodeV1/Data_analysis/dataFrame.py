##create
import pandas as pd
import numpy as np

s1=pd.Series([1,2,3,4,5])
s2=pd.Series([4,5,6,7,8])
df=pd.DataFrame({"one":s1,"two":s2})
print(df)
print(type(df))

df=pd.DataFrame(
    {
        'id':[1,2,3,4,5],
        'name':['tome','jack','bob','alex','jack'],
        'age':[12,15,16,26,30],
        "score":[60,70,80,90,100]

    },index=[1,2,3,4,5],columns=['name','score','age']
)
# print(df)

# print(df.index)
# print(df.columns)

# print(df.values)
# print(df.ndim)
# print(df.dtypes)
# print(df.shape)
# print(df.T)
# print(df.loc[4])
# print(df.iloc[4])
print(df.loc[:,'name'])
print(df.iloc[:,0])

print(type(df['name']))
print(df[['name','age']])
print(type(df[['name']]))
print(df[(df.age>15)&(df.score<100)])

print(df.tail(1))
print(df.isin(['Jack']))
print(df.isna())
print(df['score'].sum())
print(df.count())