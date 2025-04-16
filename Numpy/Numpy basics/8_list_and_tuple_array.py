'''8. Write a Python program to convert a list and tuple into arrays.
List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
[1 2 3]]'''

import numpy as np

lst=[1,2,3,4,5]
print(f'List is:{lst}')
print(type(lst))

arr=np.array(lst)
print(f'The array is:{arr}')
print(type(arr))

my_tuple=(1,2,3,4,5,6,7,8)
print(my_tuple)
print(type(my_tuple))

arra=np.array(my_tuple)
print(arra)
print(type(arra))