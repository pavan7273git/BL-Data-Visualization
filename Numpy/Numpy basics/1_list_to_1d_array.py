import numpy as np

lst=[]

length_of_lst=int(input('Enter the length of list: '))

for i in range(length_of_lst):
    user_input=float(input(f'Enter the {i}th element: '))
    lst.append(user_input)

print(f'The List is: {lst}')

arr=np.array(lst)
print(f'The 1d array is: {arr}')
print(arr.dtype)
print(type(arr))