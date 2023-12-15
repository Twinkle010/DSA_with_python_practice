class Heap:
    # using an array
    # O(1), O(n)
    def __init__(self, size) -> None:
        self.customList = (size + 1) *[None]
        self.maxSize = size + 1
        self.heapSize = 0
    
def peek(rootNode):
    # peek: returns rootnode
    # O(1), O(1)
    if not rootNode:
        return None
    return rootNode.customList[1]

def sizeOfHeap(rootNode):
    #O(1), O(1)
    if not rootNode:
        return 
    return rootNode.heapSize

def levelOrderTraversal(rootNode):
    #O(n), O(1)
    if not rootNode:
        return 
    for i in range(1,rootNode.maxSize):
        print(rootNode.customList[i])

def HeepifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return 
    if heapType == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # swap
            temp = rootNode.customList[index]
            rootNode.customList[index]= rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        HeepifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index]= rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        HeepifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, newNode, heapType):
    # O(logN), O(logN)
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "Heap is already full"
    rootNode.customList[rootNode.heapSize + 1] = newNode
    rootNode.heapSize += 1
    HeepifyTreeInsert(rootNode, rootNode.heapSize, heapType) #O(logN), O(logN)
    return "inserted node"


def heepifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapSize < leftIndex:
        # node to extract has no children
        return 
    elif rootNode.heapSize == leftIndex:
        # has one child
        if heapType == 'Min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                # swap
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return 
        else:
            # max heap
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                # swap
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
    else:
        # node has two children
        if heapType == 'Min':
            # get min of both children
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # check condition with swap child and swap
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            # get max of both children
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = rightIndex
            else:
                swapChild = leftIndex
            # check condition with swap child and swap
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heepifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    # O(logN), O(logN)
    if rootNode.heapSize == 0:
        return 
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heepifyTreeExtract(rootNode, 1, heapType) #O(logN), O(logN)
    return extractedNode

def deleteEntireHeap(rootNode):
    # O(1), O(1)
    rootNode.customList = [None]
    rootNode.heapSize = 0
    rootNode.maxSize = 0
    return 

nHeap = Heap(5)
# print(sizeOfHeap(BinaryHeap))
insertNode(nHeap, 30, 'Min')
insertNode(nHeap, 20, 'Min')
insertNode(nHeap, 10, 'Min')
insertNode(nHeap, 5, 'Min')
levelOrderTraversal(nHeap)
print("--------")
nHeap2 = Heap(4)
insertNode(nHeap2, 5, 'Max')
insertNode(nHeap2, 15, 'Max')
insertNode(nHeap2, 25, 'Max')
insertNode(nHeap2, 20, 'Max')
levelOrderTraversal(nHeap2)
print("-------")
print(extractNode(nHeap, 'Min'))
print(extractNode(nHeap, 'Min'))
print("*")
levelOrderTraversal(nHeap)
print("----------")
deleteEntireHeap(nHeap)
levelOrderTraversal(nHeap)
