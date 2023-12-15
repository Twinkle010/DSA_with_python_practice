# faster than linear search
# useful for sorted arrays
import math
def binarySearch(array, value):
    # get start and end pointers
    # calc middle value
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    # if the value to be search is greater than middle pointer, move left pointer up
    # if the value to be searched is less than middle pointer, move right pointer down 
    while start <= end:
        if array[middle] == value:
            return middle
        elif value < array[middle]:
            end = middle - 1 
        else: 
            start = middle+1
        middle = math.floor((start+end)/2)
    return -1 # if not found

print(binarySearch([10,20,30,40,50,60], 70))
print(binarySearch([10,20,30,40,50,60], 40))
# time complexisty: O(1) in bestcase
# worst case: O(logN)
# i.e as the number of elements in the array are doubled, number of steps to get result increases by 1
# if the array is sorted, binary search is the best search algo.