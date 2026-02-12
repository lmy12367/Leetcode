import pandas as pd
import numpy as np
import matplotlib as plt

df=pd.read_csv('./data/data_anal/employees.csv')
print(df)
print(df.dtypes)
print(df.head())
df=df.tail()
df.to_csv('./data/data_anal/new.csv')

df=pd.read_json('./data/data_anal/data1.json')
print(df)

import json
with open('./data/data_anal/test.json') as f:
    data=json.load(f)
print(type(data))
df=pd.DataFrame(data['users'])
print(df)


