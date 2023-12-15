# The sorted part contains the first element of the array and other unsorted subpart contains the rest of the array. The first element in the unsorted array is compared to the sorted array so that we can place it into a proper sub-array.

# It focuses on inserting the elements by moving all elements if the right-side value is smaller than the left side.

# It will repeatedly happen until the all element is inserted at correct place.

def insertionsort(customList):
    for i in range(1, len(customList)): 
        #starting from index1
        # iterate from 1 to len: since the first ele is in sorted
        # store curr value in a temp variable
        temp = customList[i]
        # get index of prev ele 
        j = i-1
        # compare with all the prev ele and move to the right if unsorted
        while j>= 0 and customList[j] > temp:
            # move to right if greater i.e not in order
            customList[j+1] = customList[j]
            j-=1
            # continue for all the ele  in reverse order
        # once out of the loop or unsort condition not met, replace the variable with temp value
        customList[j+1] = temp
        
    return customList

clist1 = [10,9,5,2,1]


print(insertionsort(clist1))
# time: (n^2)
# space: O(1)
# avoid when time is a concern
# use when there;s continuous inflow of numbers and want tokeep them sorted