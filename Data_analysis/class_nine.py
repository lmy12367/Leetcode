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
        'age':[np.nan,16,17,18,19],
        'score':[65.5,85.8,99.5,77.43,88.65]
    },index=[1,2,3,4,5],columns=['name','score','age']
)
print(df)

print('row index')
print(df.index)
print('line ')
print(df.columns)

print('values')
print(df.values)

print('维度')
print(df.ndim)

print('values type')
print(df.dtypes)

print('形状')
print(df.shape)
print(df.size)

print(df.loc[4])
print(df.iloc[3])

print(df)
print(df.loc[:,'name'])
print(df.iloc[:,0])

print(df.at[3,'score'])
print(df.iat[2,1])

print(df['name'])
print(type(df['name']))
print(df.name)
print(type[df.name])
print(df[['name','score']])
print(df.head(2))
print(df.score>70)
print(df[df.score>70])
print(df[(df.score>70)&(df.age<17)])

print(df.sample())
print(df.isin(['jack',16]))
print(df['score'].sum())
print(df.age.min())
print(df.score.max())
print(df.score.mean())
print(df.score.std())
print(df.score.var())
print(df.describe())
print(df.count())
print(df.replace(np.nan,30))
print(df)
print(df.sort_values(by='age'))






