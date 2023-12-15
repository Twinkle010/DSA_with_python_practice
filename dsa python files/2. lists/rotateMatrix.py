# function to rotate a matric by 90deg
# 1 2 3
# 4 5 6
# 7 8 9

# res
# 7 4 1
# 8 5 2
# 9 6 3

# N*N matrix
import numpy as np
my_array=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(my_array)
new_array =[]
def rotateMatrix(my_array):
    N, M = len(my_array), len(my_array[0])
    for i in range(len(my_array)):
        for j in range(len(my_array[0])):
            new_array[len(my_array)-1] = my_array[i][j]



rotateMatrix(my_array)