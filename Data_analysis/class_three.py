##索引切片
##25.8.23
##一位数组
import numpy as np
np.random.seed(0)
arr=np.random.randint(1,100,20)
print(arr)
print(arr[10])
print(arr[1:5])
print(arr[arr>10])
print(arr[(arr>10)&(arr<50)])
print(arr[slice(1,10,2)])

##二维数据
arr=np.random.randint(1,100,(10,10))
print(arr)

print(arr[1,2])
print(arr[2:5,3:5])
print(arr[slice(1,10,2),slice(1,10,2)])
print(arr[arr>50])
print(arr[2][arr[2]>50])



