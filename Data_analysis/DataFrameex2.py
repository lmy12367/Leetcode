import pandas as pd
data = {
    '产品名称': ['A', 'B', 'C', 'D'],
    '单价': [100, 150, 200, 120],
    '销量': [50, 30, 20, 40]
}
df=pd.DataFrame(data,index=[1,2,3,4])
print(df)
df['total']=df['单价']*df['销量']
print(df)
print(df.nlargest(1,columns=['total']))
print(df.sort_values('total',ascending=False))