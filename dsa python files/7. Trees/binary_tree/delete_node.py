from QueueLinkedList import Queue
class Tree():
    def __init__(self, data) -> None:
        self.data = data
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

## Delete a node
# delete the deepest node
# if the node has dependents, delete the deepest and replace the required with deepest 

def get_deepest_node(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root= customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepest_node = root.value
        return deepest_node

def delete_deepest(rootNode, dNode):
    if not rootNode:
        return 
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return 
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return 
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return 
                else:
                    customQueue.enqueue(root.value.leftChild)
            
def delete_node(rootNode, dNode):
    if not rootNode:
        return 
    else:
        # get deepest node
        # assign cur node to deepest
        # delete deepest
        
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == dNode:
                deep_Node = get_deepest_node(rootNode)
                root.value.data = deep_Node.data
                delete_deepest(rootNode, deep_Node)
                return 
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
        return 'node not found'
# time complexity : O(n) iterating through all values and deleting one node at a time

def del_BT_tree(rootNode):
    if not rootNode:
        return 
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return 

# time complexity: O(1)
# space complexity: O(1)


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
cold.leftChild = cold_Type1
cold.rightChild =cold_Type2

newNode = get_deepest_node(newBT)
delete_deepest(newBT, newNode)
levelOrderTraversal(newBT)
print("**")
delete_node(newBT, 'Tea')
levelOrderTraversal(newBT)
print("**")

del_BT_tree(newBT)
levelOrderTraversal(newBT)
