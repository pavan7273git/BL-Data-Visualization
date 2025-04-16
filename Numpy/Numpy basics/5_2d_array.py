'''5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
Expected Output:
Original array:
[[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]]

1 on the border and 0 inside in the array
[[ 1. 1. 1. 1. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 1. 1. 1. 1.]]'''

import numpy as np

arr=np.full((5,5),1)

print(arr)

print()
arr=np.zeros((5,5),dtype=int)

arr[0,:]=1
arr[4,:]=1
arr[:,0]=1
arr[:,4]=1
print(arr)