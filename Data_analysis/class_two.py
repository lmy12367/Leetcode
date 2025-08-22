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

arr=np.arange(1,10,2)
print(arr)
arr=np.arange(1,10,1)
print(arr)

arr=np.arange(1,21,1)
arr.reshape(2,10)
print(arr.reshape(2,10))

app=np.linspace(1,10,5)
print(app)

app=np.linspace(0,50,10)
print(app)

app=np.arange(0,101,25)
print(app)

agg=np.logspace(0,2,5,base=10)
print(agg)

