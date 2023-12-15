from QueueLinkedList import Queue
class Tree():
    def __init__(self, data) -> None:
        self.data= data
        self.leftChild = None
        self.rightChild = None
    
def levelOrderTraversal(rootNode):
    # traverse level by level 
    if not rootNode:
        return 
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)

def insertNode(rootNode, newNode):
    if not rootNode:
        # if tree doesnot exiss, create
        rootNode = newNode
        return "Inserted"
    else:
        # iterate through levels and insert at the first vacant position
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Inserted"
            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Inserted"
            
newBT = Tree('Drinks')
hot = Tree('hot')
cold = Tree('cold')
newBT.leftChild = hot
newBT.rightChild = cold
hot_Type1 = Tree('Tea')
hot_Type2 = Tree('Coffee')
hot.leftChild = hot_Type1
hot.rightChild =hot_Type2
cold_Type1 = Tree('Maaza')
cold_Type2 = Tree('xyz')
insertNode(newBT, cold_Type1)
levelOrderTraversal(newBT)
insertNode(newBT, cold_Type2)
levelOrderTraversal(newBT)