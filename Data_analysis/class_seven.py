##2025年8月26日
##panadas开始
import pandas as pd
s=pd.Series([10,25,38,44,59])
print(s)

s=pd.Series([10,25,40,58,6],index=['a','b','c','d','e'])
print(s)

s = pd.Series([10, 25, 40, 58, 6], index=['a', 'b', 'c', 'd', 'e'], name='月份')
print(s)

s=pd.Series({'a':1,'b':2})
print(s)
s1=pd.Series(s,index=['b'])
print(s1)

