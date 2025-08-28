##2025.8.28
import numpy as np
import pandas as pd

s=pd.Series([1,2,np.nan,None,pd.NA])
print(s)

df=pd.DataFrame([[1,pd.NA,2],[2,3,5],[None,4,6]],columns=['第一列','第二列','第三列'])
print(df)
print(s.isna())
print(df.isna())
print(df.isna().sum())
print(s.isna().sum())
print('x'*30)
print(s.dropna())
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(thresh=2))
print(df.dropna(axis=1))
print(df.dropna(subset='第一列'))
print(df.fillna({'第一列':5}))
print(df.fillna(df[['第二列']].mean()))
print(df)
df = df.convert_dtypes()
df['第二列'] = df['第二列'].astype('float64')
mean_value = df['第二列'].mean()
df['第二列'] = df['第二列'].fillna(mean_value)

print(df)

