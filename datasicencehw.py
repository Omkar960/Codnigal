import numpy as np
arr = np.arange(10,dtype=float)
print(arr)
new_arr = arr.copy()
new_arr[new_arr%2==1] = -1
print(new_arr)
arr2d = arr.reshape(2,5)
print(arr2d)
sum = 0
for i in arr:
    if i % 2 == 0:
        sum += i
print(sum)
