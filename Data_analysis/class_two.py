##numpy的arry的创建
##2025.8.22
import numpy as np
arr=np.array([1,2,3],dtype=float)
print(arr)
print(arr.ndim)

arr1=np.copy(arr)
arr1[1]=5
print(arr1)

arr2=np.zeros((2,3))
print(arr2)
arr3=np.ones((5,3),dtype=int)
print(arr3)
arr4=np.empty((3,2),dtype=float)
print(arr4)
arr4=np.empty((3,2),dtype=int)
print(arr4)
arr4=np.empty((3,2))
print(arr4)

arr5=np.full((3,4),2026)
print(arr5)
 
arr6=np.zeros_like(arr5)
print(arr6)
arr6=np.ones_like(arr5)
print(arr6)
arr6=np.full_like(arr5,4)
print(arr6)
