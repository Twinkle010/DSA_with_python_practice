# find max product of two integers in an array where all int are positive


import numpy as np

my_list = np.array([1,23,44, 65, 10, 23, 34])

def findMaxProduct(my_list):
    max_product = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] * my_list[j] > max_product:
                max_product = my_list[i] * my_list[j]
    return max_product

print(findMaxProduct(my_list))
