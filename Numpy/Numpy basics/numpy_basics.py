import numpy as np

arr=np.array([1,2,3,4,5,6,7,8])

print(arr[2]+arr[3])
print(type(arr))
print(arr.dtype) #return arr data type

print(arr[1::2])
print(arr[6:1:-2])

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a.ndim)
print(f'2nd element of 3rd row {a[2,2]}')
print(f'thre row element in the array {a[1,2]}')

b=np.array(['agv','bjf','guc'])
print(b)
print(b.dtype)
