# implement an algo to determine if a list has all unique charecters

import numpy as np

my_list = np.array([1,2,3,4,5,6,7,8,2,9])
res_list =[]

def IsUnique(my_list):
    for i in my_list:
        if i not in res_list:
            res_list.append(i)
        else:
            print(i)
            return False
    return True


print(IsUnique(my_list))
