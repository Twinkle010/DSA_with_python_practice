class BST():
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BST(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue) #O(n/2)
    elif nodeValue >= rootNode.data:
        if rootNode.rightChild is None:
            rootNode.rightChild = BST(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue) # O(n/2)
    # time: O(logN), space: O(logN) bcs pushing n number of ele recursively?????

def preOrderTraversal(rootNode):
    # time: O(n) since all nodes are being visited
    # space: O(n) recursive calls , for stack memory
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

from QueueLinkedList import Queue
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
    # time: O(n)
    # space: O(n) for queue ds

def search_node(rootNode, nodeValue):
    if not rootNode:
        return "  "
    if nodeValue == rootNode.data:
        print(f"{nodeValue} found")
        return 
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None:
            if nodeValue == rootNode.leftChild.data:
                print(f"{nodeValue} found")
                return 
            else:
                search_node(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild is not None:
            if rootNode.rightChild.data==nodeValue:
                print(str(nodeValue)+" found")
                return 
            else:
                search_node(rootNode.rightChild, nodeValue)
    return f"{nodeValue} not found"

def minValueNode(rootNode):
    while rootNode.leftChild is not None:
        rootNode = rootNode.leftChild
    return rootNode

def deleteNode(rootNode, dNode):
    # 1. when node to delete is leaf -> deletr
    # 2. when node to delete has one child -> swap the child and root
    # 3. when node to delete has two child -> find the successor of root and replace root with successor, delete successor
    if not rootNode:
        return rootNode
    elif dNode < rootNode.data:
        # left
        rootNode.leftChild = deleteNode(rootNode.leftChild, dNode)
    elif dNode > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, dNode)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # when two children are present
        minNode = minValueNode(rootNode.rightChild)
        rootNode.data = minNode.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, minNode.data)
    return rootNode
    # time and space: O(logN)

def deleteST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    
newBT = BST(40)
insertNode(newBT, 50)
insertNode(newBT, 25)
insertNode(newBT, 60)
insertNode(newBT, 80)
# print(newBT.data)
# print(newBT.leftChild.data)
# print(newBT.rightChild.data)
preOrderTraversal(newBT)
print("------")
inOrderTraversal(newBT)
print("------")
postOrderTraversal(newBT)
print("------")
levelOrderTraversal(newBT)
print("-----")
print(search_node(newBT, 10))
search_node(newBT, 40)
search_node(newBT, 25)
search_node(newBT, 80)
print("-------")
deleteNode(newBT, 80)
levelOrderTraversal(newBT)
deleteNode(newBT, 40)
print("---")
levelOrderTraversal(newBT)
print("----")
deleteST(newBT)
levelOrderTraversal(newBT)