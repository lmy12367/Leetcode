##2025.9.27
##DataFrame
import numpy as np
import pandas as pd

s1=pd.Series([1,2,3,4,5])
s2=pd.Series([6,7,8,9,10])
df=pd.DataFrame({'第一列':s1,'第二列':s2})
print(df)
print(df.dtypes)
print(type(df))

df=pd.DataFrame(
    {
        'id':[1,2,3,4,5],
        'name':['tom','jack','alex','bob','alen'],
        'age':[15,16,17,18,19],
        'score':[65.5,85.8,99.5,77.43,88.65]
    }
)
print(df)

df=pd.DataFrame(
    {
        'id':[1,2,3,4,5],
        'name':['tom','jack','alex','bob','alen'],
        'age':[15,16,17,18,19],
        'score':[65.5,85.8,99.5,77.43,88.65]
    },index=[1,2,3,4,5],columns=['name','score','age']
)
print(df)