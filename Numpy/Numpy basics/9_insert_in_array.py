'''9. Write a Python program to append values to the end of an array.
Expected Output:
Original array:
[10, 20, 30]

After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]'''

import numpy as np

arr=np.array([10,20,30])
print(arr)

new_arr=np.insert(arr,len(arr),[40,50,60,70,80,90])
print(new_arr)