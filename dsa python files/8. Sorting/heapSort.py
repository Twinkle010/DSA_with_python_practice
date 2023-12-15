
def heepify(mylist, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and mylist[l] < mylist[smallest]:
        smallest = l
    if r < n and mylist[r] < mylist[smallest]:
        smallest = r
    
    if smallest != i:
        mylist[smallest], mylist[i] = mylist[i], mylist[smallest]
        heepify(mylist, n, smallest)

def heapsort(mylist):
    n= len(mylist)
    # rearrange the heap ele first
    for i in range(int(n/2)-1, -1, -1):
        heepify(mylist, n, i)
    # extract
    for i in range(n-1, 0, -1):
        mylist[i], mylist[0] = mylist[0], mylist[i]
        heepify(mylist, i, 0) # puttig in descending
    mylist.reverse()
    return mylist

cutomList = [3,2,5,6,1,10]
print(heapsort(cutomList))
# time: O(NlogN)
# space: O(1)