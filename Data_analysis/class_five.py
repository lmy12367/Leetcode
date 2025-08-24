##numpy统计函数
##2025.8.24
import numpy as np

np.random.seed(0)
arr=np.random.randint(1,20,8)
print(arr)
print(np.sum(arr))
print(np.mean(arr))

arr1=np.sort(arr)
print(arr1)
print(np.median(arr1))

arr2=np.var(arr1)
arr3=np.std(arr1)
print(arr2)
print(arr3)

arr4=np.max(arr1)
print(arr4)
arr5=np.min(arr1)
print(arr5)
print(np.argmax(arr))

arr6=np.random.randint(0,100,6)
print(arr6)
print(np.sort(arr6))
print(np.percentile(arr6,25))

arr=np.array([1,2,3])
print(np.cumsum(arr))
print(np.cumprod(arr))
