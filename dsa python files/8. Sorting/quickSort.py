def swap(customList, index, swapindex):
    customList[index], customList[swapindex] = customList[swapindex], customList[index]

def pivot(customList, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        # swap if the ele is greater than pivot
        if customList[i] < customList[pivotIndex]:
            # swap
            swapIndex += 1
            swap(customList, i, swapIndex)
    # once evrything is done, swap the pivot index and now swap index
    swap(customList, pivotIndex, swapIndex)
    return swapIndex # so as to get left and rifht sublists

def quickSortHelper(mylist, leftIndex, rightIndex):
    if leftIndex < rightIndex: # iterate recursively, base condition to break the loop
        pivotIndex = pivot(mylist, leftIndex, rightIndex)
        quickSortHelper(mylist, leftIndex, pivotIndex-1)
        quickSortHelper(mylist, pivotIndex+1, rightIndex)
    return mylist

def quickSort(mylist):
    return quickSortHelper(mylist, 0, len(mylist)-1)


mylist = [3,4,0,5,1]
print(pivot(mylist, 0, 4))
print(mylist)
print("--")
print(quickSort(mylist))