##比较函数
##2025.8.24
import numpy as np
arr=[3,4,5,6]
# print(np.greater(arr,4))
# print(np.less(arr,5))
# print(np.equal(arr,5))

arr1=[1,0,1,0]
arr2=[1,1,0,1]
print(np.equal(arr1,arr2))

print(np.logical_and(arr1,arr2))
print(np.logical_or(arr1,arr2))
print(np.logical_not(arr1))
print(np.logical_xor(arr1,arr2))

print(np.any(arr1))
print(np.all(arr1))

###np.where(条件，符合条件，不符合条件)
arr=np.array([1,2,3,4,5])
print(np.where(arr>3,arr,0))

arr=np.random.randint(1,50,20)
print(arr)
print(np.sort(arr))
print(np.argsort(arr))

print(np.unique(arr))

print(np.concatenate((arr1,arr2)))
