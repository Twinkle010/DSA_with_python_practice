# iterate over the pair of ele and swap if not in order
# consider the last ele as sorted in every iter

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)

# time complexity : O(n^2) since have to iterate for every pair
# space complexity: O(1) since no extra space is used
# choose if time is not a concern and space is a concern
# when input is already sorted
# easy to implement

input_list = [10,9,8,7,6,5]
bubbleSort(input_list)