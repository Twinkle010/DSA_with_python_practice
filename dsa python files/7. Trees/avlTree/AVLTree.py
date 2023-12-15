from QueueLinkedList import Queue
class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
    
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
        
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        return "Value found"
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            return "value found"
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild:
            if rootNode.rightChild.data == nodeValue:
                return "value found"
            else:
                searchNode(rootNode.rightChild, nodeValue)
    return "value not found"

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftchild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, newNode):
    if not rootNode:
        return AVLNode(newNode)                                             # ----> O(1)
    elif newNode < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, newNode)        #------>O(logN)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, newNode)      #------O(logN)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and newNode < rootNode.leftChild.data:
        # left left condition
        return rightRotate(rootNode)                                           # O(1)
    if balance > 1 and newNode > rootNode.leftChild.data:
        # left right condition
        # left rotate root node's left child
        # right rotate root node
        rootNode.leftChild = leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance < -1 and newNode > rootNode.rightChild.data:
        # right right condition
        return leftRotate(rootNode)
    if balance < -1 and newNode < rootNode.rightChild.data:
        # right left condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
    # time: O(logN), space: O(logN)

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, delNode):
    if not rootNode:
        return
    elif delNode < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, delNode)
    elif delNode > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, delNode)
    else:
        # when node to del has one child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # when node to del has two children
        minNode = getMinValueNode(rootNode.rightChild)
        rootNode.data = minNode.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, minNode.data)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    # when rotation is required
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        # left left condition
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        # right right condition
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0 :
        # left right condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        # right left condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def delAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None


newAVLTree = AVLNode(5)
# levelOrderTraversal(newAVLTree)
# print(searchNode(newAVLTree, 5))
# print(searchNode(newAVLTree, 15))
newAVLTree = insertNode(newAVLTree, 10)
newAVLTree = insertNode(newAVLTree, 15)
newAVLTree = insertNode(newAVLTree, 20)
newAVLTree = insertNode(newAVLTree, 25)
# print(getMinValueNode(newAVLTree).data)
levelOrderTraversal(newAVLTree)
print("***")
newAVLTree = deleteNode(newAVLTree, 20)
levelOrderTraversal(newAVLTree)
delAVL(newAVLTree)
print("------")
levelOrderTraversal(newAVLTree)