import pandas as pd
import numpy as np

# data = {
#     "name":['alice','alice','bob','alice','jack','bob'],
#     "age":[26,25,30,25,35,30],
#     'city':['NY','NY','LA','NY','SF','LA']
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.duplicated())
# print(df.drop_duplicates())
# print(df.drop_duplicates(subset=['name']))
# print(df.drop_duplicates(subset='age'))
# print(df.drop_duplicates(subset=['name'],keep='last'))

# df=pd.read_csv('./data/data_anal/sleep.csv')
# print(df.dtypes)
# df['age']=df['age'].astype('int16')
# print(df.dtypes)
# print(df.gender)
# df['gender']=df['gender'].astype('category')
# print(df.gender)
# df['is_male']=df['gender'].map({'Female':False,"Male":True})
# print(df.is_male)
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
month=["jan",'Feb','mar','apri']
sale=[200,256,523,85]
plt.plot(month,sale)
plt.title('sale totel')
plt.xlabel("month")
plt.ylabel('sale')
plt.legend(locals='upper left')

plt.show()

