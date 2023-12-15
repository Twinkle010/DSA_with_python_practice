# find pairs of numbers in a list equal to a target number

my_list = [2, 4, 6, 1, 3, 0, 3]
target = 6

def findPairs(my_list, target):
    res_pairs = []
    for i in range(0,len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] + my_list[j] == target:
                res_pairs.append(tuple([my_list[i],my_list[j]]))
    return res_pairs

def IndexPairs(my_list, target):
    res_pairs = []
    for i in range(0,len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] + my_list[j] == target:
                res_pairs.append(tuple([i,j]))
    return res_pairs

def findDistinctPairs(my_list, target):
    res_pairs = []
    for i in range(0,len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] + my_list[j] == target and my_list[i]!=my_list[j]:
                res_pairs.append(tuple([my_list[i],my_list[j]]))

    return res_pairs

def findPairsInAllOrders(my_list, target):
    res_pairs = []
    for i in range(0,len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] + my_list[j] == target:
                res_pairs.append(tuple([my_list[i],my_list[j]]))
                res_pairs.append(tuple([my_list[j],my_list[i]]))


    return res_pairs
print(findPairs(my_list, target))
print(findDistinctPairs(my_list, target))
print(findPairsInAllOrders(my_list, target))
print("***")
print(IndexPairs(my_list, target))
