'''6. Write a Python program to add a border (filled with 0's) around an existing array.
Expected Output:
Original array:
[[ 1. 1. 1.]
[ 1. 1. 1.]
[ 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 0. 0. 0. 0. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 0. 0. 0. 0.]]'''

import numpy as np

arr=np.full((3,3),1)

print(arr)

new_arr=np.zeros((5,5),dtype=int)

new_arr[1:4,1:4]=arr
print(new_arr)