# recursively break all the ele till it cannot be split further, then merge accordingly

def merge(customList, l, m, r):
    n1 = m-l+1 # number of ele in frst sub array
    n2 = r-m # number of ele in second sub array
    # intialise temp lists
    LA = [0] * n1
    RA = [0] * n2

    for i in range(0, n1):
        LA[i] = customList[l+i]
    for j in range(0, n2):
        RA[j] = customList[m+j+1]
    
    i = 0 # index of left sub array
    j = 0 # index of right
    k = l # index of merged
    while i < n1 and j < n2:
        # compare values and append
        if LA[i] <= RA[j]:
            customList[k] = LA[i]
            i+=1
        else:
            customList[k] = RA[j]
            j+=1
        k+=1
    
    while i<n1: # add if any ele left over
        customList[k] = LA[i]
        i+=1
        k+=1
    while j<n2:
        customList[k] = RA[j]
        j+=1
        k+=1
    
    return customList
def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        # call recursively to divide
        mergeSort(customList, l, m)# -t(N/2)
        mergeSort(customList, m+1, r)#-T(N/2)
        # is O(NlogN)
        # merge
        merge(customList, l, m, r)
    return customList


customlist = [2,3,9,7,6,1,4,5,8]
print(mergeSort(customlist, 0, 8))

# use merge sort when stable sort is needed and avoid when space is a conern