# create individula buckets according to the number of ele in andlists and then sort the buckets individually
# calc number of buckets; round(root(num_of_ele))
# calc which ele has to go to which bucket: ceil(value*num_of_buckets/max_value)
import math
from insertionSort import insertionsort
def bubbleSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    output = []
    for i in range(numberOfBuckets):
        output.append([]) # create number of buckets
    for j in customList:
        to_go = math.ceil((j*numberOfBuckets/maxValue))
        output[to_go-1].append(j)
    # use any sorting algo to sort individual buckets
    for i in range(numberOfBuckets):
        output[i] = insertionsort(output[i])
    #merge buckets
    # output_final = []
    # for i in range(len(output)):
    #     output_final.extend(output[i])
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(output[i])):
            customList[k] = output[i][j]
            k+=1
    return customList


customList = [10,3,2,1,5,7,9,4,8]
print(customList)
print(bubbleSort(customList))


# since insertion sort is being used, timecomplexisty is o(n^2)
# use this sort when input data is uniformly distributed
# avoid when space is concern