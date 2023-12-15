class Tree():
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
def preOrderTraversal(rootNode):
    # root -> left node -> right node
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    # left node -> rootnode -> right node
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    # left -> right -> root
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

from QueueLinkedList import Queue
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

newBT = Tree('Drinks')
hot = Tree('hot')
cold = Tree('cold')
newBT.leftChild = hot
newBT.rightChild = cold
hot_Type1 = Tree('Tea')
hot_Type2 = Tree('Coffee')
hot.leftChild = hot_Type1
hot.rightChild =hot_Type2
print("**preorder**")
preOrderTraversal(newBT)
print("**done**")
print("**inorder**")
inOrderTraversal(newBT)
print("**done**")
print("**postorder**")
postOrderTraversal(newBT)
print("**done**")
print("**levelorder**")
levelOrderTraversal(newBT)
print("**done**")

