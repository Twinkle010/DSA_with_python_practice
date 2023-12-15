# Linear Search
# loop over the array and check if the element is found or not
# return index if found 
# return -1 if doesnot exists

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearSearch([10,20,30,40,50], 40))
print(linearSearch([10,20,30,40,50], 15))

# time complexisty: O(N) iterating through all ele in worst case
# space: O(1)