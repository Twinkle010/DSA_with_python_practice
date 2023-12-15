# trverse through all the levels
from QueueLinkedList import Queue

class Tree():
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
def search(rootNode, value):
    if not rootNode:
        return "not found"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root= customQueue.dequeue()
            if root.value.data == value:
                return "value found"
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
    return "value not found"
# time and space: O(n)
newBT = Tree('Drinks')
hot = Tree('hot')
cold = Tree('cold')
newBT.leftChild = hot
newBT.rightChild = cold
hot_Type1 = Tree('Tea')
hot_Type2 = Tree('Coffee')
hot.leftChild = hot_Type1
hot.rightChild =hot_Type2

print(search(newBT, 'hot'))
print(search(newBT, 'xyz'))