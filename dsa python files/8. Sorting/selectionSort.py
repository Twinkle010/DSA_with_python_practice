# find out the min ele of the unsorted array
# replace the min ele with the frst ele, i.e to get sorted array



def selectionsort(customList):
    for i in range(len(customList)):
        # iterate throught each step and find min element
        min_index = i
        for j in range(i+1, len(customList)):
            # find min of rest
            if customList[min_index] > customList[j]:
                min_index=j
        # swap
        customList[min_index], customList[i] = customList[i], customList[min_index]
    
    print(customList)

customList = [10,9,8,6,3]
selectionsort(customList)

# time: O(n^2)
# space: O(1)
# avoid when time is a concern
# use when we have insufficient memory