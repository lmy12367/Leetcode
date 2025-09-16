import numpy as np
import pandas as pd

np.random.seed(0)
values=np.random.randint(50,101,10)
print(values)
index=[]
for i in range(1,11):
    index.append('学生'+str(i))

scored=pd.Series(values,index)
print(scored)
print(scored.mean())
print(scored.max())
print(scored.min())

mean=scored.mean()
print(scored[scored>mean])
print(len(scored[scored>mean]))
print(scored[scored>mean].count())
