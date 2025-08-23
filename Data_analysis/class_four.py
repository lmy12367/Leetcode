##函数
##2025.8.23
##基本数学函数
import numpy as np

print(np.sqrt(9))
print(np.sqrt([1,4,9]))
arr=np.array([1,25,81])
print(np.sqrt(arr))
print(np.exp(1))
print(np.exp(arr))
print(np.log(arr))
print(np.log(2.71))
print(np.sin(arr))
print(np.cos(np.pi))
print(np.sin(np.pi/2))
arr=[-1,-10,-100]
print(np.abs(arr))
print(np.power(arr,3))
arr=[5.8,5.2,10.5,9.5]
print(np.round(arr))
print(np.ceil(arr))
print(np.floor(arr))

print(np.isnan([1,2,3,np.nan]))