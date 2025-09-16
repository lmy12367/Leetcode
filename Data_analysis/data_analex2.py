import pandas as pd
import numpy as np

s=pd.Series([1,2,np.nan,None,pd.NA])
print(s)
print(s.isna())
print(s.isnull())
print(s.isna().sum())
df=pd.DataFrame([[1,pd.NA,2],[2,3,4],[None,4,6]],columns=['one','two','three'])
print(df.isna())
print(df.isna().sum())
print('*'*30)
print(s.dropna())
print(df.dropna())

print(df.dropna(how='all'))
print(df.dropna(thresh=3))
print(df.dropna(axis=1))

df=pd.read_csv('.\\data\\data_anal\\weather_withna.csv')
print(df.tail())
print(df.isna().sum(axis=0))
print(df.fillna({'temp_max':20,'wind':2.5}).tail())
print(df.fillna(df[['wind']].mean()).tail(10))
print(df.ffill().tail())
print(df.bfill().tail())