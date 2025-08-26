import pandas as pd
import numpy as np
print("############")
s=pd.Series([10,2,np.nan,None,3,4,5],index=['A','B''C','D','E','F','G','H'])
print(s)
print(s.head())
print(s.head(3))

print(s.tail())
print(s.tail(2))

a=s.describe()
print(a)
b=s.count()
print(b)
c=s.keys()
print(c)
d=s.index
print(d)

print(s.isna())

print(s.isin([4]))

print(s.mean())
print(s.std())
print(s.var())
print(s.sum())
print(s.max())
print(s.min())
print(s.median())
print(s.sort_values())
print(s.quantile(0.75))
print(s.drop_duplicates())

